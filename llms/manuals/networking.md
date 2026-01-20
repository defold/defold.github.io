# Networking {#manuals:networking}

It is not uncommon for games to have some kind of connection to a backend service, perhaps to post scores, handle match making or store saved games in the cloud. Many games also have peer to peer connections where game clients communicate directly with each other, without involvement of a central server. Network connections and the exchange of data can be made using several different protocols and standards. Learn more about the different ways to use network connections in Defold:

* [HTTP Requests](https://defold.com/llms/manuals/http-requests.md)
* [Socket connections](https://defold.com/llms/manuals/socket-connections.md)
* [WebSocket connections](https://defold.com/llms/manuals/websocket-connections.md)
* [Online services](https://defold.com/llms/manuals/online-services.md)

## Technical details

### IPv4 and IPv6

Defold supports IPv4 and IPv6 connections for sockets and HTTP requests.

### Secure connections

Defold supports secure SSL connections for sockets and HTTP requests.

Defold can optionally also verify the SSL certificate of any secure connection. SSL verification will be enabled when a PEM file containing public CA-root certificate keys or a self-signed certificate public key is provided in the [SSL Certificates setting](https://defold.com/llms/manuals/project-settings.md)) field of the Network section in *game.project*. A list of CA-root certificates is included in `builtins/ca-certificates`, but it is recommended to create a new PEM file and copy-paste the needed CA-root certificates depending on the server(s) the game connects to.