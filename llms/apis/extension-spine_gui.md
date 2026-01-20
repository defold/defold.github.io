# extension-spine

**Namespace:** `gui`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Spine models in GUI

## API

### gui.new_spine_node
*Type:* FUNCTION
Dynamically create a new spine node.

**Parameters**

- `pos` (vector3 | vector4) - node position
- `spine_scene` (string | hash) - spine scene id

### gui.play_spine_anim
*Type:* FUNCTION
Starts a spine animation.

**Parameters**

- `node` (node) - spine node that should play the animation
- `animation_id` (string | hash) - id of the animation to play
- `playback` (constant) - playback mode - `gui.PLAYBACK_ONCE_FORWARD` - `gui.PLAYBACK_ONCE_BACKWARD` - `gui.PLAYBACK_ONCE_PINGPONG` - `gui.PLAYBACK_LOOP_FORWARD` - `gui.PLAYBACK_LOOP_BACKWARD` - `gui.PLAYBACK_LOOP_PINGPONG`
- `play_properties` (table) - optional table with properties
  - `blend_duration` (number) - The duration of a linear blend between the current and new animation
  - `offset` (number) - The normalized initial value of the animation cursor when the animation starts playing
  - `playback_rate` (number) - The rate with which the animation will be played. Must be positive
- `complete_function` (function(self, node)) - function to call when the animation has completed

### gui.cancel_spine
*Type:* FUNCTION
cancel a spine animation

**Parameters**

- `node` (node) - spine node that should cancel its animation

### gui.get_spine_bone
*Type:* FUNCTION
The returned node can be used for parenting and transform queries. This function has complexity O(n), where n is the number of bones in the spine model skeleton.

**Parameters**

- `node` (node) - spine node to query for bone node
- `bone_id` (string | hash) - id of the corresponding bone

### gui.set_spine_scene
*Type:* FUNCTION
Set the spine scene on a spine node. The spine scene must be mapped to the gui scene in the gui editor.

**Parameters**

- `node` (node) - node to set spine scene for
- `spine_scene` (string | hash) - spine scene id

### gui.get_spine_scene
*Type:* FUNCTION
Returns the spine scene id of the supplied node. This is currently only useful for spine nodes. The returned spine scene must be mapped to the gui scene in the gui editor.

**Parameters**

- `node` (node) - node to get texture from

### gui.set_spine_skin
*Type:* FUNCTION
Sets the spine skin on a spine node.

**Parameters**

- `node` (node) - node to set the spine skin on
- `spine_skin` (string | hash) - spine skin id

**Examples**

Change skin of a Spine node
```
function init(self)
  gui.set_spine_skin(gui.get_node("spine_node"), "monster")
end

```

### gui.add_spine_skin
*Type:* FUNCTION
Add a spine skin on a spine node to another skin on the same node.

**Parameters**

- `node` (node) - node having both skins
- `spine_skin_a` (string | hash) - spine skin id that recieves other skin
- `spine_skin_b` (string | hash) - spine skin id that will be added

**Examples**

Add skin of a Spine node to another skin
```
function init(self)
  gui.add_spine_skin(gui.get_node("spine_node"), "monster_head", "monster_body")
end

```

### gui.copy_spine_skin
*Type:* FUNCTION
Copy a spine skin on a spine node to another skin on the same node.

**Parameters**

- `node` (node) - node having both skins
- `spine_skin_a` (string | hash) - spine skin id that copies other skin
- `spine_skin_b` (string | hash) - spine skin id that will be copied

**Examples**

Copy skin of a Spine node to another skin
```
function init(self)
  gui.copy_spine_skin(gui.get_node("spine_node"), "monster_head", "monster_body")
end

```

### gui.clear_spine_skin
*Type:* FUNCTION
Clear a spine skin on a spine node of all attachments and constraints

**Parameters**

- `node` (node) - node having both skins
- `spine_skin` (string | hash) - spine skin id

**Examples**

Clear skin of a Spine node
```
function init(self)
  gui.clear_spine_skin(gui.get_node("spine_node"), "monster")
end

```

### gui.get_spine_skin
*Type:* FUNCTION
Gets the spine skin of a spine node

**Parameters**

- `node` (node) - node to get spine skin from

### gui.get_spine_animation
*Type:* FUNCTION
Gets the playing animation on a spine node

**Parameters**

- `node` (node) - node to get spine skin from

### gui.set_spine_cursor
*Type:* FUNCTION
This is only useful for spine nodes. The cursor is normalized.

**Parameters**

- `node` (node) - spine node to set the cursor for
- `cursor` (number) - cursor value

### gui.get_spine_cursor
*Type:* FUNCTION
This is only useful for spine nodes. Gets the normalized cursor of the animation on a spine node.

**Parameters**

- `node` (node) - spine node to get the cursor for (node)

### gui.set_spine_playback_rate
*Type:* FUNCTION
This is only useful for spine nodes. Sets the playback rate of the animation on a spine node. Must be positive.

**Parameters**

- `node` (node) - spine node to set the cursor for
- `playback_rate` (number) - playback rate

### gui.get_spine_playback_rate
*Type:* FUNCTION
This is only useful for spine nodes. Gets the playback rate of the animation on a spine node.

**Parameters**

- `node` (node) - spine node to set the cursor for

### gui.set_spine_attachment
*Type:* FUNCTION
This is only useful for spine nodes. Sets an attachment to a slot on a spine node.

**Parameters**

- `node` (node) - spine node to set the slot for
- `slot` (string | hash) - slot name
- `attachment` (string | hash) - attachment name. May be nil.

### gui.set_spine_slot_color
*Type:* FUNCTION
This is only useful for spine nodes. Sets a tint for all attachments on a slot

**Parameters**

- `node` (node) - spine node to set the slot for
- `slot` (string | hash) - slot name
- `color` (vector4) - target color.

### gui.spine_physics_translate
*Type:* FUNCTION
Apply a physics-based translation to the Spine GUI node.

**Parameters**

- `node` (node) - The Spine GUI node to translate.
- `translation` (vector3) - The translation vector to apply to the Spine GUI node.

### gui.spine_physics_rotate
*Type:* FUNCTION
Apply a physics-based rotation to the Spine GUI node.

**Parameters**

- `node` (node) - The Spine GUI node to rotate.
- `center` (vector3) - The center point around which to rotate.
- `degrees` (number) - The rotation angle in degrees.

### gui.set_spine_ik_target_position
*Type:* FUNCTION
Sets a static (vector3) target position of an inverse kinematic (IK) object.

**Parameters**

- `node` (node) - the Spine GUI node containing the object
- `ik_constraint_id` (string | hash) - id of the corresponding IK constraint object
- `position` (vector3) - target position

**Examples**

The following example assumes that the Spine GUI node has id "spine_node".
How to set the target IK position of the right_hand_constraint constraint object of the player object
```
function init(self)
  local pos = vmath.vector3(1, 2, 0)
  gui.set_spine_ik_target_position(gui.get_node("spine_node"), "right_hand_constraint", pos)
end

```

### gui.set_spine_ik_target
*Type:* FUNCTION
Sets a GUI node as target position of an inverse kinematic (IK) object. As the target GUI node's position is updated, the constraint object is updated with the new position.

**Parameters**

- `node` (node) - the Spine GUI node containing the object
- `ik_constraint_id` (string | hash) - id of the corresponding IK constraint object
- `target_node` (node) - target GUI node

**Examples**

The following example assumes that the Spine GUI node has id "spine_node".
How to set the target IK position of the right_hand_constraint constraint object to follow the position of GUI node with id "target_node"
```
function init(self)
  local spine_node = gui.get_node("spine_node")
  local target_node = gui.get_node("target_node")
  gui.set_spine_ik_target(spine_node, "right_hand_constraint", target_node)
end

```

### gui.reset_spine_ik_target
*Type:* FUNCTION
Resets any previously set IK target of a Spine GUI node, the position will be reset to the original position from the spine scene.

**Parameters**

- `node` (node) - the Spine GUI node containing the object
- `ik_constraint_id` (string | hash) - id of the corresponding IK constraint object

**Examples**

The following example assumes that the Spine GUI node has id "spine_node".
A player no longer has an item in hand, that previously was controlled through IK, let's reset the IK of the right hand.
```
function player_lost_item(self)
  gui.reset_spine_ik_target(gui.get_node("spine_node"), "right_hand_constraint")
end

```
