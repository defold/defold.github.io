---
layout: manual
language: en
github: https://github.com/defold/extension-webmonetization
title: Web Monetization in Defold
brief: Web Monetization is an exciting new and non-intrusive way for game developers to monetize their web games while at the same time offering premium content to their paying players.
---

# Web Monetization

[Web Monetization](https://webmonetization.org/) is an open technology that allows someone viewing a webpage or playing a web game to stream very small payments (micropayments) to the creator in real time. It is an exciting new and non-intrusive way for game developers to monetize their web games while at the same time offering premium content to their paying players.

Web Monetization is being [proposed as a W3C standard](https://discourse.wicg.io/t/proposal-web-monetization-a-new-revenue-model-for-the-web/3785). It is based on the [Interledger](https://interledger.org/) protocol which is an open, neutral protocol for transferring money of any currency, including digital currencies such as Bitcoin.


## How does it work?

Three things are required in order to send and receive payments:

1. A player must have an account with a **Web Monetization Provider** - The provider streams payments from the player.
2. The developer must have a **Web Monetization Wallet** - The wallet holds received payments.
3. The developer must add a **Payment Pointer** on the webpage containing content that should be monetized - The payment pointer tells the provider which wallet to send the money to.


### Payment Pointers

The wallet provider will assign a payment pointer to the wallet. The payment pointer is a public address for a wallet that can be shared with anyone that wants to make a payment to the owner of the wallet. Learn more at [paymentpointers.org](https://paymentpointers.org/). The format of a payment pointer is similar to a URL, but starts with a $:

```
$ilp.uphold.com/QkG86UgXzKq8
```

The payment pointer is added to the website content using a `<meta>` tag in the `<head>` of the website:

```html
<meta name="monetization" content="$ilp.uphold.com/QkG86UgXzKq8">
```


## How to set up Web Monetization in Defold

Enabling Web Monetization in a Defold game is a straightforward process. The steps involved depend on if you are adding Web Monetization to an existing project or if you are starting a new project.


### Creating a payment pointer

Start by registering for a [Web Monetization enabled wallet](#web-monetization-wallets) and copy your payment pointer as you will need it when you configure your Defold project.


### Starting a new project

If you are starting a new project it is recommended that you use the Web Monetization project template from the Defold editor Welcome screen. The Web Monetization template includes the [Web Monetization extension](https://github.com/defold/extension-webmonetization) and it will automatically set up the payment pointer in the generated webpage for your game:

![Web Monetization template](web-monetization-template.png)


Add your payment pointer to the Web Monetization section of the **game.project** file:

![Adding payment pointer to game.project](payment-pointer.png)



### Configuring an existing project

If you wish to add the extension to an existing project you can open the **game.project** file and in the [Dependencies field in the Project section](https://defold.com/manuals/project-settings/#dependencies) add:

```
https://github.com/defold/extension-webmonetization/archive/master.zip
```

Open the **game.project** file using a text editor and add a new section with your payment pointer:

```
[webmonetization]
payment_pointer = ADD PAYMENT POINTER HERE
```


## How to use Web Monetization in Defold

When you have the Web Monetization extension and payment pointer added to your project you are ready to start using Web Monetization in your game. The API consists of only two functions:

Check if a player is monetized (ie is streaming payments to you):

```lua
local monetized = webmonetization.is_monetized()
if monetized then
	print("The user has an active payment stream")
end
```

Set up a listener to get updates on the current monetization state of the player:

```lua
webmonetization.set_listener(function(self, event, details)
	if event == webmonetization.EVENT_PENDING then
		print("The user is trying to make a first payment")
	elseif event == webmonetization.EVENT_START then
		print("The user has started paying")
	elseif event == webmonetization.EVENT_PROGRESS then
		print("The user is still paying")
	elseif event == webmonetization.EVENT_STOP then
		print("The user has stopped paying")
	end
end)
```

The details table contains additional information about the event. Example:

```lua
{
  paymentPointer = "$ilp.uphold.com/QkG86UgXzKq8",
  assetScale = 9,
  amount = "26009",
  requestId = "a1f728aa-21e0-4376-ae99-0ccb22642956",
  assetCode = "XRP"
}
```

## Best practices

* Offer exclusive content to web monetized players. What you offer depends on the type of game. Some examples:
  * New skins or other cosmetic changes such as unique in-game decals or stickers
  * New game modes
  * Additional levels
* If your game contains ads you should also consider removing the ads for web monetized players
