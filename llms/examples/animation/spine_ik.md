# Handle Spine IK constraints

Learn how to control Spine IK constraints by assigning a game object as the IK target.

[Project files](https://github.com/defold/examples/tree/master/animation/spine_ik)

This example demonstrates how to control Spine Inverse Kinematics (IK) constraints in Defold by assigning a game object as the IK target.

Move the mouse or touch in the active area (white rectangle in the background) to move the robot's arm with IK constraints.

## Project Structure
```
- root
  - active_area.go
    - collisionobject
    - area.script
    - sprite
  - cursor.go
    - collisionobject
    - cursor.script
  - manipulator.script
  - spinemodel
```

## How It Works
The `cursor.go` game object is controlled by the user and has a collision object configured as a trigger.
When the cursor overlaps with the trigger in `active_area.go`, it sends a message to `manipulator.script`.
The script uses the Defold Spine API to assign `cursor.go` as the target of an IK constraint with spine.set_ik_target().
When the target is no longer needed, spine.reset_ik_target() resets the constraint to its original target position.

## Scripts

### area.script

```lua
local NORMAL_ALPHA = 0.8
local ALPHA_PROPERTY = hash("tint.w")

function init(self)
	go.set("#sprite", ALPHA_PROPERTY, NORMAL_ALPHA)
end
```

### cursor.script

```lua
local MSG_TRIGGER = hash("trigger_response")
local MSG_PARENT = hash("parent")

function init(self)
	msg.post(".", "acquire_input_focus")
end

function final(self)
	msg.post(".", "release_input_focus")
end

function on_input(self, action_id, action)
	if action.x and action.y then
		go.set_position(vmath.vector3(action.x, action.y, 1))
	end
end

function on_message(self, message_id, message, sender)
	if message_id == MSG_TRIGGER then
		msg.post("/root#manipulator", MSG_PARENT, { parent = message.enter })
	end
end
```

### manipulator.script

```lua
local IK_BONE = hash("RED_IK")
local SPINE_COMPONENT = "#spinemodel"
local MSG_PARENT = hash("parent")

function init(self)
	self.target = go.get_id("cursor")
end

function on_message(self, message_id, message, sender)
	if message_id == MSG_PARENT then
		if message.parent then
			spine.set_ik_target(SPINE_COMPONENT, IK_BONE, self.target)
		else
			spine.reset_ik_target(SPINE_COMPONENT, IK_BONE)
		end
	end
end
```
