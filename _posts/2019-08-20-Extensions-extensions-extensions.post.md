---
layout: post
title:  It's all extensions baby!
excerpt: The dream of the engine for-loop
author: Björn Ritzl
---

# Extensions, extensions, extensions

We have made several steps towards our goal of a lean engine core which basically only updates a bunch of systems every frame. The systems, or at least some of them, should reside in separate external extension projects, and the developer can chose which ones to use. Oh, so you want Facebook SDK support? Sure, add the Facebook extension? Ah, you want to send push notifications? Add the Push extension? A webview you say? Well, there's an extension for that as well!
