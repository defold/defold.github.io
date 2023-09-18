---
layout: post
title:  Working with public and private repos
excerpt: We'll explain a bit about how we maintain both a public and private repositories while complying with non disclosure agreements from several different vendors.
author: Mathias Westerdahl
tags: ["code", "engine", "repos", "github", "consoles"]
---

## Defold and the many platforms

The [Defold game engine](https://www.defold.com) is maintained by the Defold Foundation, and it's code [is available on GitHub](https://github.com/defold/defold) under a permissive source available license for anyone to use. It supports the common major platforms for desktop, mobile and web platforms.

It also support console platforms, which require private code access.

To work with certain partners, you have to enter written non disclosure agreements that you won't share any implementation details with the public.
The Defold Foundation is a registered middleware provider, and have access to platform specific api's and sdk's under the non-diclosure agreements.

These agreements of course affect what may or may not be visible in the public facing code.

Knowing this, we had to come up with an approach that was not too far from our current workflow, or at least was as low maintenance as possible.

## Different approaches

Depending on your resources and experience, your approach may of course vary.
Here I'm describing what we considered and tried. I'm not suggesting it is the ultimate approach, only that it works for us currently.

The Defold team is a small group of 6 people so we need to minimize the time spent on maintaining code. This means it was natural to start looking at workflows we are already familiar with.

### Mono repo

One way would be to have a big private mono repository, with support for all platforms.
From there, we could do releases of the public parts into a public facing "mirrored" repository.

In our case, it wouldn't work, since our users also need source code access. We can't give everyone access since the might only have signed agreements from some of the supported platform vendors.

It would however make refactorings easier which would be a plus.

### Public + private repos

When starting out porting to our first console platform, we tested a simple approach: to copy the public repo into a private one.

The reason we didn't want to use forks, was that we didn't want to risk any commit messages etc to divulge any implementations under NDA.

We're using Git, and since the repositories would then be unrelated, it might make merging code trickier, but we decided to try it.

The initial phase for porting to any platform consists of porting some lower level systems, such as file I/O, network, input, user handling, sound and graphics.

Since each platform vendor often chooses to implement things slightly differently, it also implies we need to refactor some of our own code. These changes need to go back to the public repository, so that we can benefit from the improvements, and also to make it easier for future code merges.

After the initial porting phase, we don't generally see many code changes in the platform's lower level libraries, and we didn't expect it to be any different with console support.

All in all, this approach turned out to work quite well for us, and we decided to start using it.

## Engine plugins

Our engine also has a plugin functionality which allows the developers to add native code to the engine. It is available for all platforms.
For each private platform, we have a plugin our users can use to add more Lua bindings to the platforms' private api.

We support these plugins via a build server in the cloud, that builds any custom code for the platform. When building the cloud server, we include the required sdk's for all the platforms.

For users that wish to build their own server, we have instructions on how to set it up, using the same code as we use. They might also simply remove support for platforms they don't need (to make the server size smaller).

The source code for the cloud builder is available under MIT license in our [extender repository](https://github.com/defold/extender).

## Technical details

### SDK's

Each vendor has their own SDK, which you need to hide from public eyes.
They also have their own custom toolchains to produce object files and a linker to produce the executable. Very high level info such as the platform triplet are generally considered public knowledge, but more detailed info than that should be kept private.

The vendors we currently work with support the standard C and C++ libraries.
They don't want their platform to be singled out when it comes to implementation details. So, either stick with common code paths, using standard C/C++ code, or take a vendor agnostic code path (details further down)

And that's one of the key takeaways from this work, to hide even the platform name from the public code!

### GitHub

We've used GitHub for a while now, and we use GitHub Actions as our continuous integration.
For our private repos, we publish our built artefacts to the releases page of that repo, making it available for our registered users.

We also use GitHub's user groups to manage the permissions between the repos:
 one group for our free platform plugin, and another group for full source code access.


### Our current workflow

#### Updating the private repos

When updating the private repository, we have added an `upstream` remote url and merge as usual, you may need the '--allow-unrelated-histories'

    git fetch upstream
    git merge upstream/dev

#### Merging back to public repo

It is perhaps possible to do some git magic to merge back from the private branch, into a new branch+PR, without including vendor specific code, but I'm not aware of it currently.

Instead we use a simple approach of copying files from the private repo to a public repo branch:

    $ ./copy_from_private_repo.py /path/to/private /path/to/public

In this script, we do a simple pattern match for any files that are considered private. In our case it's files with platform name and "vendor":

    sys_vendor.h
    sys_<PLATFORM>.h

We also do this exclusion for directories that match the platform name.

    sys/<PLATFORM>/file.h

Once the files are copied, you can create a pull request with the changes. As with any pull request, you need to make sure that nothing private is submitted to the PR. But if you stick to placing the private code in files/folders with a simple naming scheme, it should be easily avoidable.

One major drawback is that you won't get any git history from those changes. This fact can be remedied somewhat if you do regular merges, so that they get their own commit messages.

#### Header files

In the actual headers, we hide away any mention of the actual platform.
This is an extra step to simply avoid the entire discussion if it is ok or not to have the platform name in the public code. Here is an actual example from our [thread.h](https://github.com/defold/defold/blob/dev/engine/dlib/src/dmsdk/dlib/thread.h#L22-L28):

```c++
#if defined(DM_PLATFORM_VENDOR)
    #include <dmsdk/dlib/thread_native_vendor.h>
#elif defined(_WIN32)
    #include <dmsdk/dlib/thread_native_win32.h>
#else
    #include <dmsdk/dlib/thread_native_posix.h>
#endif
```

Internally, the `*_vendor.h` will then use any platform specific defines and any includes as necessary.

### Build scripts

We use the `waf` build system, which is Python based.
It allows us to dynamically check for existing build scripts that we can augment the build with.

In our case, we check for e.g. `build_vendor.py`, in which we setup platform specific paths and variables. And, since it is named "vendor" it won't be copied back into the public repository.

#### Defines and code blocks

Another option to control the code is to enable/disable code blocks by setting defines from the build scripts. That way code path remains generic. E.g:

```c++
#if defined(DM_SUPPORTS_POSIX_FEATURE)
    #include <some_posix_header.h>
    int feature_func(int) {
        return some_posix_func();
    }
#else
    int feature_func(int) {
        return 0;
    }
#endif
```

### Future improvements

#### Automated integrations

It has happened sometimes that during our bi-weekly release cycle, we forget to do a release from a private repository. Or that we forget to merge good changes back to the public repository.

An idea we'd like to try is to do automatic merges from our public repo to the private one. If it works, the code could be checked in. And if it fails, we'd know about it each morning.

## Wrapping it up

All in all, I'm quite happy with how well this works.

We currently maintain three private repos for our console support. The number may grow if we enter other agreements with new partners.

While the initial setup of keeping extra headers is a little bit cumbersome at first, once it is done, it has been quite easy to work with. And it also completely eliminates the discussion if it's private code or not.

The biggest workflow bump is keeping the the public and private repositories in sync by merging code back and forth, but I hope we can streamline that too.

#### Keep a dialog!

The vendors we work with are slowly opening up their ways of working with open source codebases, and are very interested in the topic. Be aware that these are large corporations and not very fast moving in terms of decisions.

But if you have questions, make sure you ask them questions in their forums about such related questions so you at least get the ball rolling!


Thanks for reading!
