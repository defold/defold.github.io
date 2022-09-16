---
layout: post
title:  The feature request journey
excerpt: In this blog post we describe the development process for feature requests
author: Björn Ritzl
tags: ["code", "engine", "open-source"]
---

We were recently asked about the development process for feature requests. How are features requested and what is the process from initial request to released feature? In this blog post we'll describe the process on a high level. If you have questions about the process then please don't hesitate to reach out to us on [Discord server](https://defold.com/discord) or the [user forum](https://forum.defold.com/).


### Feature request
Everything starts with a problem and and a missing solution. Feature requests usually originate from a Defold user, corporate partner or from the Defold development team. Feature requests can be raised on our [user forum](https://forum.defold.com/), [Discord server](https://defold.com/discord) or directly on [GitHub](https://github.com/defold/defold/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=). We want all feature requests on GitHub and will usually ask the person requesting the feature to submit the request on GitHub. We require the following information to be able to evaluate a feature request:

**Is your feature request related to a problem?**
Here we ask for a clear and concise description of what the problem is. Example: I'm always frustrated when [...]

**Describe the solution you'd like**
Please give a clear and concise description of what you want to happen.

**Describe alternatives you've considered**
Perhaps there is a workarond? If so, we appreciate a clear and concise description of any alternative solutions or features you've considered.

It is important to also search for already submitted feature requests before submitting a new feature request. Maybe someone has already suggested the same thing or something only slightly different? If there is an already submitted feature request we appreciate if you add additional information instead of creating a new feature request. We will close any duplicate feature requests.


### Review
When the feature request has been posted on GitHub it be reviewed and we may ask follow-up questions. During the review process we factor in many different things:

* **Is the feature request solving a real problem?** While it can sometimes be good to plan ahead and try to anticipate problems down the road it can also lead to speculation and solutions that are larger than they actually need to be. Every line of code you add will increase the build time, the complexity and the size of the code base, all of which are things you want to avoid in a game engine (or actually in all software).

* **Is the feature request solving a frequent and complex problem?** The reason game developers use game engines instead of creating games completely from scratch is that game engines provide solutions to complex and frequent problems. This allows game developers to focus on creating games instead of solving technology problems. Game engines exist to solve problems, but game engines can not solve all problems. Some problems require solutions that have more to do with the game than with the engine and some problems are easy to solve and can be left for the developer or a third party library to solve.

* **Is the feature request solving a game engine problem?** Game developers are faced with many different kinds of problems when developing games. Some are obviously game related, like how to best code the enemy behaviour or how to present the player inventory. Some problems are not as obvious, like how to do pathfinding efficiently or how to create a scrolling list of UI elements. It is tempting to expect these kinds of problems to be solved by the engine, and some game engines go down that route and provide solutions to fairly high-level Problems. The design philosophy in Defold is to not solve these problems but instead provide low-level building blocks that can be used to create solutions for high-level problems.

If we are not able to confidently answer yes to the questions above we will close the feature request and either recommend the developer to solve the problem in their game or through an extension.


### The waiting game
Now is the time to let the feature request mature together with all of the other feature requests. Users can upvote (using the thumbs-up emoji) the feature and provide additional information to the feature request. At some point an external contributor or the Defold team may pick up the feature request and start working on an implementation.


### Planning
At this point we have decided to start working on the feature request. We review all comments and information in the feature request and the feature request is assigned to an upcoming release project on GitHub ([example](https://github.com/defold/defold/projects/69)).


### Design
We almost always start with a design document where we answer the following questions:

* **What do we want to do?**
"We want to add frustum culling for labels"

* **Why do we want to do it?**
"To increase rendering performance in games with a lot of offscreen labels"

* **What are the different solutions and the pros and cons of each?**
"Cull using the same system as sprites, ie using a sphere", "Cull using a rectangle" etc

* **What are the future improvements?**
"Cull individual glyphs instead of the whole label"

This design document is reviewed and discussed by the development team and the best solution is decided on.


### Implementation
Once the design document has been discussed and we agree on a solution we can finally start the implementation. The development work is done on a feature branch which we name to match the feature request (example: `Issue-1234-add-culling-of-labels`).


### Pull request
When development is done we create a pull request. The pull request will link to the issue it solves and it will be reviewed one or more members of the development team. During the review process things such as unit test coverage, code convention and naming standards are checked. The pull request is merged when it has been approved and all checks (unit tests) pass.


### Release
The feature will be included in the next release when the merged code make it into the beta and master (stable) branch. At the moment we have a four week development cycle, then a two week beta period which ends with a release to the stable branch of Defold.


We hope this sheds some light on the development process. If you have questions about the process then please don't hesitate to reach out to us on [Discord server](https://defold.com/discord) or the [user forum](https://forum.defold.com/).
