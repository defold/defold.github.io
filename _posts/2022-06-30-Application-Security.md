---
layout: post
title:  Application Security
excerpt: This post covers a number of important security related topics related to the use of the Defold engine, tools and services.
author: Björn Ritzl
tags: ["security", "engine"]
---

Note: This is a post initially shared in June 2022 as a [security related manual](https://defold.com/manuals/application-security/) in the Learn section of the Defold website.

Application security is a broad topic which covers everything from secure development practices to securing your game content after it has been released. This post will cover a number of areas and put them in the context of application security when using the Defold engine, tools and services:

* Intellectual property protection
* Anti-cheat solutions
* Secure network communication
* Use of third-party software
* Use of cloud build servers
* Downloadable content


## Securing your intellectual property from theft
A concern most developers have is how to protect their creations from theft. Copyright, patents and trademarks can from a legal standpoint be used to protect the different aspects of the intellectual property of video games. Copyright gives its owner the exclusive right to distribute the creative work, Patents protects any inventions and Trademarks protects names, symbols and logos.

It may also be desirable to take technical precautions to protect the creative work of a game. It is however important to keep in mind that once the game is in the hands of the player it is possible to find ways to extract the assets. This can be achieved by reverse engineering the game application and files, but also by using tools to extract texture and models as they are sent to the GPU or when other assets are loaded into memory.

For this reason it is our general stance that if users are determined to extract the assets of a game, they will be able to do so.

Developers can add their own protection to make it harder, __but not impossible__, to extract the assets. This typically includes various means of encryption and obfuscation to protect and hide game assets.

### Source code obfuscation
Applying source code obfuscation is an automated process where the source code is deliberately made difficult for humans to understand, without impacting the program’s output. The purpose is usually to protect against theft, but also to make cheating harder.

It is possible to apply source code obfuscation in Defold either as a pre-build step or as an integrated part of the Defold build process. With pre-build obfuscation the source code is obfuscated using an obfuscation tool before the Defold build process is started.

Build-time obfuscation on the other hand is integrated into the build process using a Lua builder plugin. A Lua builder plugin takes the raw source code as input and returns an obfuscated version of the source code as output. One example of build-time obfuscation is shown in the [Prometheus extension](https://github.com/defold/extension-prometheus), based on the Prometheus Lua obfuscator available on GitHub.


### Resource encryption
During the Defold build process the game resources are processed and transformed into formats suitable for runtime consumption by the Defold engine. Textures are compiled into the Basis Universal format, the collections, game objects and components are converted from human readable text representation to binary counterparts and the Lua source code is processed and compiled into bytecode. Other assets such as sound files are used as-is.

When this process is completed the assets are added to the game archive, one by one. The game archive is a large binary file and the location of each resource within the archive is stored in an archive index file. The format is documented [here](https://github.com/defold/defold/blob/dev/engine/docs/ARCHIVE_FORMAT.md).

Before Lua source files are added to the archive they are also optionally encrypted. The default encryption provided in Defold is a simple block cipher used to  prevent strings in the code from being immediately visible if the game archive is inspected using a binary file viewer tool. It should not be considered cryptographically secure since the Defold source code is available on GitHub with the cipher key visible in the source code.

It is possible to add custom encryption to Lua source files by implementing a Resource encryption plugin. A Resource encryption plugin consists of a build-time part to encrypt resources as part of the build process and a runtime part to decrypt resources when they are read from the game archive. A basic Resource Encryption plugin which can be used as the starting point for your own encryption is [available on GitHub](https://github.com/defold/extension-resource-encryption).


## Securing your game against cheaters
Cheating in video games has existed for as long as the games industry itself. Cheat codes used to be shared in popular video games magazines and special cheat cartridges were sold for the early home computers. As the industry and the games have evolved so have the cheaters and their methods. Some of the most popular cheating mechanism for games are:

* Repackaging of game content to inject custom logic
* Speed hacks to make a game run faster or slower than normal
* Automation and visual analysis for auto aiming and bots
* Code and memory injection to modify scores, lives, ammo etc

Protecting against cheaters is hard, bordering on impossible. Even cloud gaming, where games are run on remote servers and streamed directly to a user's device are not fully exempt from cheaters.

Defold does not provide any anti-cheat solutions in the engine or tools and instead defer any such work to one of the many companies specialize in providing anti-cheat solutions for games.


## Securing your network communication
Defold socket and HTTP communication support secure socket connections. It is recommended to use secure connections for any server communication to authenticate the server and to protect the privacy and integrity of any exchanged data while in transit from client to server and vice versa. Defold uses the popular and widely adopted open source [Mbed TLS](https://github.com/Mbed-TLS/mbedtls) implementation of the TLS and SSL protocols. Mbed TLS is developed by ARM and their technology partners.

### SSL certificate validation
To prevent man in the middle attacks on your network communication it is possible to validate the certificate chain during the SSL handshake when negotiating a connection with a server. This can be done by providing a list of public keys to the network client in Defold. For more information on securing your network communication please read the section about SSL verification in the [network manual](https://defold.com/manuals/networking/#secure-connections).


## Securing your use of third-party software
While it is not necessary to use any third-party libraries or native extensions to create a game it has become a very common practice among developers to use assets from the official [Asset Portal](https://defold.com/assets/) to speed up development. The Asset Portal contains a large selection of assets, ranging from integrations with third-party SDKs, to screen managers, UI libraries, cameras and much more.

None of the assets in the Asset Portal have been reviewed by the Defold Foundation and we do not take responsibility for any damage to your computer system or other device or loss of data that results from use of any asset obtained through the Asset Portal. You can read the fine print in our [Terms and Conditions](https://defold.com/terms-and-conditions/#3-no-warranties).

We recommend that you review any asset before use, and once you have deemed that it is suitable for use in your project you create a fork or copy of the asset to ensure that it doesn’t change without you noticing it.


## Securing your use of cloud build servers
The Defold cloud build servers (aka extender servers) were created to help developers add new functionality to the Defold engine without requiring a rebuild of the engine itself. When a Defold project containing native code is built for the first time the native code and any associated resources are sent to the cloud build servers where a custom version of the Defold engine is created and sent back to the developer. The same process is applied when a project is built using a custom application manifest to remove unused components from the engine.

The cloud build servers are hosted with AWS and created according to security best practices. The Defold Foundation does however not guarantee that the cloud build servers will meet your requirements, be free from defects, virus free, secure or error free, or that your use of the servers will be uninterrupted or secure. You can read the fine print in our [Terms and Conditions](https://defold.com/terms-and-conditions/#3-no-warranties).

If the security and availability of the builds servers are of concern to you we recommend that you set up your own private build servers. Instructions on how to set up your own server can be found in the [main readme file](https://github.com/defold/extender) of the extender repository on GitHub.


## Securing your downloadable content
The Defold Live Update system allows developers to exclude content from the main game bundle for download and use at a later time. A typical use case is to download additional levels, maps or worlds as the player progresses through the game.

When excluded content is downloaded and prepared for use in a game, the content will be cryptographically verified by the engine before use to ensure that it has not been tampered with. The verification consists of a number of checks:

* Is the binary format correct?
* Is the downloaded content supported by the currently running engine version?
* Is the downloaded content signed with the correct public-private key pair?
* Is the downloaded content complete and not missing any files?

You can read more about this process in the [Live Update manual](https://defold.com/manuals/live-update/#manifest-verification).

