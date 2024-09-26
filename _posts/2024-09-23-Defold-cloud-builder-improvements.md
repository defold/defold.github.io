---
layout: post
title:  Defold cloud builder improvements
excerpt: We are happy to announce that we've finished a large overhaul of the build servers to simplify development, maintenance and the setup of local build servers.
author: Björn Ritzl
tags: ["news", "gcp", "extender"]
---

When the Defold extension system and the cloud builders were launched eight years ago it marked a milestone for Defold when game developers no longer had to rely on the Defold development team to provide integrations to third party services and platform specific features. Instead developers could write native code and add Lua bindings and have the code seamlessly integrated into the engine without installing any additional tools or SDKs. 

The release of the extension system has resulted in a large ecosystem of plugins, available from the [Asset Portal](/assets) and integrated into games in a few simple steps. Many of the plugins are maintained by the Defold Foundation, but there are also plenty of examples of popular community created plugins. The extension system has without a doubt been a large contributing factor to the continued adoption and use of Defold among game developers!

One problem with the extension system is the development and operation of the build servers themselves. Up until now the build servers have been large monolithic servers with unwieldy setup scripts, running on [Amazon Web Services](https://aws.amazon.com/) (AWS). This setup has been a source of frustration for the development team and it has without a doubt prevented many developers from contributing improvements to the build servers and from setting up their own local or cloud hosted servers. Another concern is that the build servers are provided for free to all of our users and as our userbase has grown year over year we've also seen our AWS costs increase significantly. The servers are running 24/7 which means a fixed cost for the servers, but network traffic and storage costs have gone up, and there's been a general price increase for the servers themselves.

A couple of months ago we made the decision to try and improve the situation by simplifying the setup and operation while at the same time trying to reduce costs. We are now happy to announce that we've finished a large overhaul of the build servers. The servers are now split up into multiple instances where each instance is serving builds for a single platform. This will give us flexibility to quickly scale servers up and down depending on use, and even suspend servers that are inactive for a period of time.

The servers have also been migrated from AWS to [Google Cloud Platform](https://cloud.google.com/) (GCP) and the containers for each platform are available from a public container registry on GCP. The public container registry greatly simplifies the work involved in setting up your own local build servers or servers running on your own GCP account.

Finally, we have also started using [Terraform](https://www.terraform.io/) to describe the cloud builder infrastructure as code, which makes it easier to track and deploy changes.

The new system has been running for a month and we are very happy with the results. The setup is easier to maintain and operate and it will help us save money. It is now also a lot easier for users to set up their own build servers in a few easy steps. Have a look at the [instructions in the official manual](https://defold.com/manuals/extender-local-setup/) and try it out yourself!


## Getting help and reporting problems

The system has been up and running for a while now but if you encounter any problems or have discovered a bug, please report them in the [build server repository](https://github.com/defold/extender) or reach out on the [Defold forum](https://forum.defold.com/).