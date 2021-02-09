---
layout: post
title:  Developer case study - Interrogation
excerpt: In this developer case study we'll look at the Defold game 'Interrogation - You will be deceived.' by Critique Gaming.
author: Björn Ritzl
tags: ["developer case study", "interview"]
---

In this developer case study we'll look at the Defold game ["Interrogation: You will be deceived"](https://interrogation-game.com/) by [Critique Gaming](https://critique-gaming.com/).

Interrogation was first released on December 5th, 2019 on Steam and GoG and later also for mobile and Nintendo Switch. The game has a very distinct graphical style and a deep narrative gameplay. Critique Gaming describes the game like this:

"Interrogation is a difficult noire detective game about ethics, morality, radicalisation and the nature of authority. Strategically manage the special police department tasked with bringing down a terrorist organisation which threatens the very structure of society: *The Liberation Front*. Uncover their mysteries in iconic movie-like Interrogation scenes, using a complex conversation simulation system. Solve hard conversational puzzles by psychologically manipulating realistic suspects. Decide their fate, your fate and the city’s."

The game features deep and increasingly difficult conversational puzzles, resource management where you need to balance your active cases, team and budget as well as public relations. The game has multiple endings and many complex and realistic characters, created from real actor footage.

Here's an example of some gameplay:

![Animation showing Interrogation gameplay](/images/posts/developer-case-study-interrogation/1_question_asking.gif)

To help us understand the development process of Interrogation we have invited [Marius Petcu](https://defold.com/2020/09/02/Creator-spotlight-Marius/), lead developer for Interrogation. Welcome!

**Björn**: Marius, let's start with the workflow for the developers in your team. I know you've said that the fact that **Defold has all scene metadata in Protobuf Text Format** has been very helpful throughout the development process. Can you tell us how it has helped you when developing Interrogation?

**Marius**: (Easy to modify. Batch modify with simple scripts. Merge friendly. Nice diffs)

![Image showing the Protobuf Text Format](/images/posts/developer-case-study-interrogation/protobuf.png)
(Example of a gui scene created in Defold and stored in a human-readable merge-friendly format)

![Image showing a file diff](/images/posts/developer-case-study-interrogation/diff.png)
(Nice looking diff)


**Björn**: That's great! It sure does make the day to day work a lot smoother when there are no proprietary binary formats for any metadata. Another thing you mentioned as an advantage is **the [Defold Asset Portal](/assets) with a lot of useful extensions, plugins and libraries that are available for free**. Can you tell us about your experience using assets from the Asset Portal?

**Marius**: (Community supported. Easy to use. Easy to contribute to.)

* Defold-RichText - Format and output flowing text with different styles.
* Defold-Input - Input utilities
* Steamworks - Vital integration with Steam
* DefNet - Networking utilities
* In-app Review extension - iOS and Android review popups

(We even created some extensions of our own)

* FMOD integration
* Discord integration
* GOG Galaxy integration
* Android APK Extension Files extension
* Contributions to DefOS - Window management
* Crit - A collection of reusable scripts


**Björn**: In May of 2020 when Defold became independently owned by the Defold Foundation we also made **all of the engine source code available**. Did the fact that the source code was available impact you in any way while working on the game?

**Marius**: (Fix things yourself and not have to wait on the Defold team)

---

**Björn**: What was the experience like to **port from desktop to mobile, and also later to Nintendo Switch**?

**Marius**: (Porting was relatively easy)

---

**Björn**: I understand that you have created several build scripts to help with application bundling, distribution and other build tasks. Can you please share what you created to automate a lot of tedious manual work for the team?

**Marius**:

* Bundling for multiple platforms and distribution methods
* macOS notarization
* Packs custom non-Defold-managed resources
* Removes design-time metadata from levels
* Extracts internationalization strings
* Compiles our DSL to Lua code
* Archives binaries and debug symbols
* Runs in a GitHub Actions CI/CD

---

**Björn**: It sounds like the overall experience for the developers of Interrogation was positive. How was it to create a game of that size using Lua? Did you have prior experience with Lua?

**Marius**: (Lua)

---

**Björn**: Ok, so what about the artists, game designers and anyone else on the team. What was good and what, if anything was bad?

**Marius**: (Everyone can do basic git)

**Marius**: (zero-setup philosophy)

---

**Björn**: When I play the game I'm **really impressed by the amount of art you've managed to fit into the game**. What was the animation workflow like and how did you manage to also make the game run on an old iPhone?

**Marius**:

(27 chars * approx 40 frames)
(15 chars * approx 10 frames)
(Whole game 400Mb. Runs on iPhone 6)

![Animation showing side by side real life actor and end result in game](/images/posts/developer-case-study-interrogation/animations.gif)

---

**Björn**: What was your approach to external tooling? We've already seen how you created some really useful build scripts to help with automation, but what about tools for content creation? How did you create all of the very complex conversational trees you find in the game?

**Marius**: (React app. Hot reload server.)

![Image of the Interrogation editor](/images/posts/developer-case-study-interrogation/editor.png)

**Marius**: (Fuior: Narrative design DSL)

* tree-sitter grammar
* Compiles to Lua
* Atom plugin
* Compiler as a NE in debug builds
* Compiled Lua in release builds

---

**Björn**: It doesn't sound like the non-developers in your team had a hard time with Defold either! Before we wrap things up I have a few more questions.

**Björn**: The first version of Interrogation was released at the end of 2019, when Defold was at version 1.2.164. Defold has had 12 releases since then and new versions of Interrogation has also been released. What has been your game engine update strategy for Interrogation? Have you stayed at Defold version 1.2.164 or have you kept up to date, and if so, have you had any problems with breaking changes for the game?

**Marius**: (answer on update strategy)

---

**Björn**: If anything, what would you have made differently during the development process if you had to do it all over again?

**Marius**: (answer on update strategy)

---

**Björn**: And now that I think of it, I know that you are actually doing it all over again, but with a new game, Domains of Dusk! Also made with Defold and scheduled for release when?

**Marius**: (Domains of Dusk)

---

**Björn**: Thank you Marius for sharing some of your learnings from Interrogation! I hope to have you back for another interview when Domains of Dusk has been released!
