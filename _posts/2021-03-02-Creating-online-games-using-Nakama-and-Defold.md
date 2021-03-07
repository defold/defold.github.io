---
layout: post
title:  Creating online games using Nakama and Defold
excerpt: In this post we will look at how to create online multiplayer games in Defold using the open-source Nakama game server from Heroic Labs
author: Björn Ritzl
tags: ["nakama", "tutorial"]
---

# Introduction

In this post we will look at how to create online multiplayer games in Defold using the open-source Nakama game server from [Heroic Labs](https://heroiclabs.com/). Nakama is a feature packed game server with a clean API and excellent documentation. You can have Nakama up and running on your local machine in just a couple of minutes.


## XOXO

Throughout this post we will use a Tic-Tac-Toe game which we have decided to call XOXO as an example of how to setup and use the Nakama APIs.

![](/images/posts/creating-online-games-using-nakama-and-defold/xoxo-matchmaker-registration.png)

The source code for the game is available on GitHub and we will refer to the code throughout this article:

* [Game client](https://github.com/defold/game-xoxo-nakama-client)
* [Game server](https://github.com/defold/game-xoxo-nakama-server)

The server uses authoritative multiplayer code which means that the moves made by the players are validated by the server and the updated game state is sent back to the players when it changes.

[Try the game in your browser](https://defold.com/game-xoxo-nakama-client/) (ask a friend to do the same or open two browser tabs to play against yourself).


### A note on the two ways to call Nakama functions

Nakama includes lots of built-in APIs for various features of the game server. These can be accessed with the methods which either use a callback function to return a result (ie. asynchronous) or yield until a result is received (ie. synchronous and must be run within a Lua coroutine):

```Lua
local client = nakama.create_client(config)

-- using a callback
nakama.get_account(client, function(account)
    print(account.user.id);
    print(account.user.username);
    print(account.wallet);
end)

-- if run from within a coroutine
local account = nakama.get_account(client)
print(account.user.id);
print(account.user.username);
print(account.wallet);
```

The Nakama client provides a convenience function for creating and starting a coroutine to run multiple requests synchronously one after the other:

```Lua
nakama.sync(function()
    local account = nakama.get_account(client)
    local result = nakama.update_account(client, request)
end)
```


## Server setup

Let's get started! The first step is to set up a Nakama server that we can connect to. The quickest way to get up and running is to follow the setup guide for running Nakama using Docker on your own machine. This will run an instance of Nakama and an associated database in a Docker container, with all configuration taken care of. Follow the [Nakama Docker quickstart](https://heroiclabs.com/docs/install-docker-quickstart/) and you'll be ready in a matter of minutes!

Note that for production use it is recommended to use a binary install on your server. Heroic Labs also provide hosted instances of Nakama through Heroic Cloud. A perfect setup if you want to focus on your game and let Heroic Labs manage and scale the infrastructure as your user base grows.


## Defold integration

Integrating Nakama in Defold is also a straightforward process. You add Nakama to your list of project dependencies together with the official WebSocket extension for Defold:

![](/images/posts/creating-online-games-using-nakama-and-defold/add-dependencies.png)


## Configuration

Next step is to configure your Defold game to use Nakama. We need to tell Namaka the URL of our server, the port number to connect to and a few other settings. The code to configure Nakama looks like this:

```Lua
local defold = require "nakama.engine.defold"

-- The Nakama server configuration
local config = {}
config.host = 127.0.0.1 -- localhost, ie your own machine
config.port = 7350
config.use_ssl = (config.port == 443)
config.username = "defaultkey" -- your Nakama server key, default is "defaultkey"
config.password = ""
config.engine = defold -- Tell Nakama to use Defold (it can theoretically also work with other Lua based engines)

local client = nakama.create_client(config)
```

Server config in XOXO: [https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L136-L146](https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L136-L146)


## Authentication

We are now ready to get your game online, but first we need a way for players to login and authenticate themselves. Nakama supports many [different ways of authenticating a user](https://heroiclabs.com/docs/authentication/). You can authenticate using a Facebook login token, using a Google or Apple account, using a username and password, a Steam account and in a number of other ways. Another way to authenticate is through a generated device identifier which is bound to the hardware of the user. Let’s try it!

We generate a UUID (Unique User Id), based on the MAC address of the network adapter, and use it to authenticate with:

```Lua
-- our login function using a device token
local function device_login(client)
	local body = nakama.create_api_account_device(defold.uuid())
	-- login using the token and create an account if the user
	-- doesn't already exist
	local result = nakama.authenticate_device(client, body, true)
	if result.token then
		-- store the token and use it when communicating with the server
		nakama.set_bearer_token(client, result.token)
		return true
	end
	print("Unable to login")
	return false
end
```

Device login in XOXO: [https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L19-L32](https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L19-L32)


## Creating a socket connection

We are now connected to the Nakama server and have authenticated the user. The last step before we can use the full range of Nakama APIs is to create a socket connection. We need the socket connection for matchmaking, real-time multiplayer games, chat and notifications.

```Lua
local socket = nakama.create_socket(client)
local ok, err = nakama.socket_connect(socket)
if not ok then
	print("Unable to connect: ", err)
	return
end
```

Creating the socket in XOXO: [https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L162-L171](https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L162-L171)


## Finding an opponent using the matchmaker

Nakama's [matchmaker](https://heroiclabs.com/docs/gameplay-matchmaker/) allows users to find opponents and teammates for matches, groups, and other activities. The matchmaker maintains a pool of users that are currently looking for opponents and places them together whenever a good match is possible.

In our game we will use simple matchmaking to find any other player also looking to play a game of Tic-Tac-Toe. The Nakama matchmaker can do much more advanced things and match players on a number of different criteria using an easy to learn [query syntax](https://heroiclabs.com/docs/gameplay-matchmaker/#query).


### Adding the user to the matchmaker

The first step is to add the player to the matchmaking pool of users:

```Lua
-- find a match with any other player
-- make sure the match contains exactly 2 users (min 2 and max 2)
local message = nakama.create_matchmaker_add_message("*", 2, 2)
local result = nakama.socket_send(socket, message)
if result.error then
	print(result.error.message)
end
```

Adding the player to the matchmaker in XOXO: [https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L80-L87](https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L80-L87)


### Getting matched

Now that we have added the authenticated user to the matchmaking pool we also need to make sure we are notified when a match is found. Nakama has a number of different events which you can subscribe to and among them is an event when the matchmaker has found a match:

```Lua
nakama.on_matchmakermatched(socket, function(message)
	-- make sure we got matched
	local matched = message.matchmaker_matched
	if matched then
		print(matched.match_id)
		print(matched.token)
	end
end)
```

Matched event listener in XOXO: [https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L70-L77](https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L70-L77)


### Joining the match

When a match has been found the player has a choice of either joining the match or declining. Here's how to join a match given a match id and a token:

```Lua
local message = nakama.create_match_join_message(match_id, token)
local result = nakama.socket_send(socket, message)
if result.match then
	print("Match joined!")
end
```

Joining the match in XOXO: [https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L38-L49](https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L38-L49)


## Playing a match of Tic-Tac-Toe

In a game of Tic-Tac-Toe the players take turns making moves until either player wins or the game board is filled and the game is a draw. Sending player moves and receiving game state updates are handled just like with the matchmaker. There is one function to send match data to the server and one match data event which is called whenever match data is received from the server.


### Sending a move

Moves are sent as match data messages. You are free to structure the data any way you like as long as the resulting data structure is encoded as a string (array of bytes) before it is sent.

In a Tic-Tac-Toe game the played row and column will be sent together with a user defined op-code which can be used on the server to differentiate between different type of match data:

```Lua
local data = json.encode({
	row = row,
	col = col,
})
local message = nakama.create_match_data_message(match_id, OP_CODE_MOVE, data)
local result = nakama.socket_send(socket, message)
if result.error then
	print(result.error.message)
	pprint(result)
end
```

Sending a move in XOXO: [https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L94-L104](https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L94-L104)


### Receiving match data

Your game will receive match data updates for as long as the match lasts. Just like with the moves you sent the received match data can also be in any format, as long as it can be encoded and decoded as a string of bytes. The match data also contain an op-code to tell different match data messages apart.

```Lua
nakama.on_matchdata(socket, function(message)
	local match_data = message.match_data
	local op_code = tonumber(match_data.op_code)
	local data = json.decode(match_data.data)
end)
```

Receiving match data in XOXO: [https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L94-L104](https://github.com/defold/game-xoxo-nakama-client/blob/main/main/xoxo_nakama.lua#L94-L104)


### Handle players leaving during a match

Online games must be able to handle players leaving in the middle of a match. In the case of a game of Tic-Tac-Toe it's not a very complex affair, but in a game with multiple players you may wish to allow players to rejoin a match they for some reason left.

Nakama can handle all of these scenarios on the server and on the client you can get notified as players leave and join an ongoing match. In XOXO the match is considered over as soon as a player disconnects.

```Lua
nakama.on_matchpresence(socket, function(message)
	local match_presence_event = message.match_presence_event
	pprint(match_presence_event.leaves) -- list of players that left
	pprint(match_presence_event.joins) -- list of players that joined
end)
```


## Wrapping up the client

On a high level the steps described above to handle configuration, authentication, matchmaking and sending and receiving match data is all there is to the game client integration of Nakama. For a more complex game you may also have to consider things such as improved user authentication and more robust error and reconnect handling.


# What about the server?

We have so far only looked at the game client and the integration with Defold. We have not considered what is required of the server for the matchmaking and more importantly how the server authoritative game logic of a Tic-Tac-Toe game is handled.

The Nakama server includes a fast embedded code runtime where you can write custom logic with Go plugins, **Lua modules**, or as a JavaScript bundle. This can be used to register hooks to operate on the messages from the client and to execute custom logic on demand. Learn more about hooks [in the official documentation](https://heroiclabs.com/docs/runtime-code-basics/#register-hooks).


## Matchmaker matched hook

For server authoritative games we use a hook to run code when the matchmaker finds opponents. When a group of matched opponents are found we create a new match on the server and provide a match handler. The match handler contains the logic required to play the match (more on this below).

```Lua
-- called when the matchmaker finds opponents
local function makematch(context, matched_users)
    local match_handler_module = "tictactoe_match"
    local setupstate = { invited = matched_users }
    local matchid = nk.match_create(match_handler_module, setupstate)
    return matchid
end

nk.register_matchmaker_matched(makematch)
```

Matchmaker matched hook in XOXO: [https://github.com/defold/game-xoxo-nakama-server/blob/main/main.lua#L23-L40](https://github.com/defold/game-xoxo-nakama-server/blob/main/main.lua#L23-L40)


## Match handler

The match handler is a separate Lua module (or JavaScript or Go code) with the match logic. The match handler has a number of life-cycle functions, much like a Defold script file. There is one function that is run on init, another for when a player joins or leaves, one for the match loop and one when the match ends.

For XOXO we decided to separate the match handler from the actual Tic-Tac-Toe game logic. The responsibility of the match handler module is to react to the different life-cycle events of a match and to forward any received moves to the actual Tic-Tac-Toe game logic and send back an updated game state to the players.

* The match handler logic for XOXO: [https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua](https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua)
* The Tic-Tac-Toe game logic for XOXO: [https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_state.lua](https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_state.lua)

Separating the server side game logic from the match handler is useful since it allows you to run the game logic in isolation, for instance when running tests or when playing a local match against bots.


### Lifecycle functions

As we mentioned above the match handler has a number of different life-cycle functions to handle the states and events of a match. The life-cycle functions are passed a number of common arguments:

* `context` - information about the match and server for information purposes.
* `dispatcher` - a table with functions to broadcast messages and kick players.
* `tick` - match tick number, incrementing for each match loop.
* `state` -  the current game state.

Let's look at the life-cycle functions:


#### Match handler init

This function is called when the match handler is created. In this function we configure the tick rate of the match (how often the match should be updated) and we create the initial game state. The game state will be passed to the rest of the match handler life-cycle functions. To make another Defold analogy the match state can be seen as the `self` argument passed to all Defold script life-cycle functions.

```Lua
function M.match_init(context, setupstate)
    local gamestate = {}
    local tickrate = 1 -- one update per second
    local label = ""
    return gamestate, tickrate, label
end
```

Match handler init in XOXO: [https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L58-L64](https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L58-L64)


#### Match join attempt

This function is called when a player tries to join the match. In addition to the common match handler life-cycle function arguments the match join attempt function also receives information about the player attempting to join the match. You can use this function to decline a player that for some reason should not be permitted to join the match.

```Lua
function M.match_join_attempt(context, dispatcher, tick, gamestate, presence, metadata)
    local acceptuser = true
    return gamestate, acceptuser
end
```

Match join attempt in XOXO: [https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L66-L70]https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L66-L70


#### Match join

This function is called when one or more players join, after you have accepted the players in the match join attempt function above. In addition to the common match handler life-cycle function arguments the match join function also receives a list of the players that joined the match.

```Lua
function M.match_join(context, dispatcher, tick, gamestate, presences)
    for _, presence in ipairs(presences) do
        nk.logger_info(presence.username)
    end
    return gamestate
end
```

In the XOXO game the players are added to the match and when the match contains two players an initial game state (an empty Tic-Tac-Toe board) is sent to the connected clients: [https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L72-L81](https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L72-L81)


#### Match leave

This function is called when one or more players leave the match. In addition to the common match handler life-cycle function arguments the match leave function also receives a list of the players that left the match.

```Lua
function M.match_leave(context, dispatcher, tick, gamestate, presences)
    for _, presence in ipairs(presences) do
        nk.logger_info(presence.username)
    end
    return nil
end
```


#### The match loop

We have finally reached the real guts of a match, the match loop! This function will be run repeatedly at an interval specified by the tick rate set in the init function of the match.

In addition to the common match handler life-cycle function arguments the match loop function also receives a list of match data messages sent from the clients.

```Lua
function M.match_loop(context, dispatcher, tick, gamestate, messages)
    for _, message in ipairs(messages) do
        nk.logger_info(string.format("Received %s from %s", message.data, message.sender.username))
    end
    return gamestate
end
```

As XOXO is a server authoritative game any received player move is validated before the game state is updated and sent back to the players. If the game is finished a 10 second countdown is started before the board is cleared and a new game is started. Note that the new game is run in the same match handler but with a game state that has been reset.

The match loop in XOXO: [https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L83-L87](https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L83-L87)


### Ending a match

If you look at all of the lifecycle functions of the match handler you notice that all of them return a game state. The match will keep on running on the server for as long as you return a game state. This is true even after all players have left! The match will end immediately when you return nil from any of the lifecycle functions.

In the XOXO game this is used to end the match as soon as one of the players leave the match: [https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L85-L86](https://github.com/defold/game-xoxo-nakama-server/blob/main/tictactoe_match.lua#L85-L86)


# Conclusions

That's it! We hope this article has provided enough insights into online multiplayer game development using Defold and Nakama that you are ready to create something yourself.

If you run into any problems and need help don't hesitate to reach out on [Discord](https://defold.com/discord/), the [Defold forum](https://forum.defold.com/) or the [Nakama community forum](https://forum.heroiclabs.com/).
