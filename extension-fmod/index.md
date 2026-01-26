---
brief: This manual covers the integration of a game with the FMOD Studio.
github: https://github.com/defold/extension-fmod
language: en
layout: manual
title: Defold extension FMOD API documentation
toc:
- Defold FMOD extension API documentation
- Installation
- Getting started
- Loading banks
- Working with events
- Creating and playing events
- Stopping events
- Error handling
- 3D audio
- Setting up the listener
- Setting up event 3D positions
- Updating positions
- Parameters
- Event lifecycle
---

# Defold FMOD extension API documentation

This extension provides an interface to integrate a game with the adaptive audio engine FMOD Studio.

## Installation

To use FMOD in your Defold project, add a version of the  Defold FMOD extension to your `game.project` dependencies from the list of available [Releases](https://github.com/defold/extension-fmod/releases). Find the version you want, copy the URL to ZIP archive of the release and add it to the project dependencies.

![](add-dependency.png)

Select `Project->Fetch Libraries` once you have added the version to `game.project` to download the version and make it available in your project.

## Getting started

Check if FMOD is available on your platform:

```lua
if not fmod then
  -- Platform not supported, handle gracefully
  return
end
```

## Loading banks

Banks contain your audio events and metadata. Load the Master Bank and Master Bank.strings before loading other banks. The strings bank is required for event lookup by name.

```lua
fmod.studio.system:load_bank_memory(resource.load("/banks/Master Bank.bank"), fmod.STUDIO_LOAD_BANK_NORMAL)
fmod.studio.system:load_bank_memory(resource.load("/banks/Master Bank.strings.bank"), fmod.STUDIO_LOAD_BANK_NORMAL)
fmod.studio.system:load_bank_memory(resource.load("/banks/Vehicles.bank"), fmod.STUDIO_LOAD_BANK_NORMAL)
```

Load banks during initialization, ideally before creating any event instances. This ensures all required audio data is in memory when needed.

## Working with events

An event description represents a type of sound event, like an explosion or engine sound. An event instance is a specific playback of that event. You can create multiple instances from the same description.

### Creating and playing events

Get the event description by its path as defined in FMOD Studio, then create and start an instance:

```lua
local event_description = fmod.studio.system:get_event("event:/Vehicles/Basic Engine")
local event = event_description:create_instance()
event:start()
```

You can store event instances (perhaps in your script's `self` table) to keep them alive and control them throughout the game object's lifecycle.

### Stopping events

Events can be stopped immediately or allowed to finish naturally:

```lua
event:stop(fmod.STUDIO_STOP_IMMEDIATE)  -- Stops instantly
event:stop(fmod.STUDIO_STOP_ALLOWFADEOUT)  -- Stops with fade-out
```

When an event instance is no longer needed, call `event:release()` to free resources. 

Events automatically release themselves when they finish playing, but explicit release is useful for long-lived instances you stop manually.

## Error handling

FMOD operations can fail. Use `pcall` to catch errors and check error codes:

```lua
local ok, err = pcall(function ()
  local desc = fmod.studio.system:get_event("event:/Inexistent event")
end)

if not ok then
  local code = fmod.error_code[err]
  if code == fmod.ERR_EVENT_NOTFOUND then
    -- Handle missing event gracefully
  end
end
```

Common error codes include `ERR_EVENT_NOTFOUND`, `ERR_INVALID_HANDLE`, and `ERR_NOTREADY`. Validate operations that might fail, especially when loading banks or retrieving events.

## 3D audio

FMOD supports 3D spatial audio with listener and emitter positioning. Set up both the listener, typically the camera or player, and source positions.

### Setting up the listener

The listener represents where the audio is heard from. Create 3D attributes and update them in your update loop:

```lua
local listener_attr = fmod._3D_ATTRIBUTES()
listener_attr.position = go.get_world_position("listener") * world_scale
listener_attr.velocity = vmath.vector3(0.0)
listener_attr.forward = vmath.vector3(0.0, 1.0, 0.0)
listener_attr.up = vmath.vector3(0.0, 0.0, -1.0)
fmod.studio.system:set_listener_attributes(0, listener_attr)
```

Use a world scale factor like `0.01` to match FMOD's coordinate system with Defold's. FMOD expects distances in meters.

### Setting up event 3D positions

For 3D audio events, set their position attributes the same way:

```lua
local source_attr = fmod._3D_ATTRIBUTES()
source_attr.position = go.get_world_position("source") * world_scale
source_attr.velocity = vmath.vector3(0.0)
source_attr.forward = vmath.vector3(0.0, 1.0, 0.0)
source_attr.up = vmath.vector3(0.0, 0.0, -1.0)
event:set_3d_attributes(source_attr)
```

### Updating positions

Update 3D attributes every frame in your `update` function. Calculate velocity from position delta for Doppler effects:

```lua
local function update_attributes(attr, dt, new_position)
  local delta_pos = new_position - attr.position
  attr.position = new_position
  attr.velocity = delta_pos * (1.0 / dt)
end

function update(self, dt)
  if not fmod then return end

  local listener_pos = go.get_world_position("listener") * world_scale
  update_attributes(self.listener_attr, dt, listener_pos)
  fmod.studio.system:set_listener_attributes(0, self.listener_attr)

  local source_pos = go.get_world_position("source") * world_scale
  update_attributes(self.source_attr, dt, source_pos)
  self.event:set_3d_attributes(self.source_attr)
end
```

The extension calls the underlying FMOD Studio update from native code each frame, so you do not need to call `fmod.studio.system:update()` manually.

## Parameters

Events can have parameters that control playback behavior, like RPM for engine sounds or intensity for ambience. Set parameters before or during playback:

```lua
event:set_parameter_by_name("RPM", 650.0, false)
```

The third parameter controls whether the change is immediate (`false`) or seeks to the new value (`true`). Use seeking for musical transitions. Immediate changes work better for gameplay-driven parameters.

Parameters can be marked as global in FMOD Studio. When global, setting that parameter affects all instances of events using it, not just one. 

## Event lifecycle

Event instances remain valid until they finish playing or are explicitly released. You can query their state:

```lua
local playing = event:is_valid()  -- Check if instance is still valid
```

When an event finishes and reaches the end of its timeline, it releases itself automatically. For one-shot sounds, you typically don't need to manually release. For looping or long-running events you control manually, call `event:release()` when done.
## API reference
[API Reference - fmod](/extension-fmod/fmod_api)
