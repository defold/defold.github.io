# Collision object

**Namespace:** `physics`
**Language:** Lua
**Type:** Defold Lua
**File:** `physics_ddf.proto`
**Source:** `engine/gamesys/proto/gamesys/physics_ddf.proto`

Collision object physics API documentation

## API

### angular_damping
*Type:* PROPERTY
The angular damping value for the collision object. Setting this value alters the damping of
angular motion of the object (rotation). Valid values are between 0 (no damping) and 1 (full damping).

**Examples**

How to decrease a collision object component's angular damping:
```
-- get angular damping from collision object "collisionobject" in gameobject "floater"
local target = "floater#collisionobject"
local damping = go.get(target, "angular_damping")
-- decrease it by 10%
go.set(target, "angular_damping", damping * 0.9)

```

### angular_velocity
*Type:* PROPERTY
The current angular velocity of the collision object component as a vector3.
The velocity is measured as a rotation around the vector with a speed equivalent to the vector length
in radians/s.

**Replaces:** request_velocity and velocity_response

**Examples**

How to query and modify a collision object component's angular velocity:
```
-- get angular velocity from collision object "collisionobject" in gameobject "boulder"
local velocity = go.get("boulder#collisionobject", "angular_velocity")
-- do something interesting
if velocity.z < 0 then
    -- clockwise rotation
    ...
else
    -- counter clockwise rotation
    ...
end
-- decrease it by 10%
velocity.z = velocity.z * 0.9
go.set("boulder#collisionobject", "angular_velocity", velocity * 0.9)

```

### apply_force
*Type:* MESSAGE
Post this message to a collision-object-component to apply the specified force on the collision object.
The collision object must be dynamic.

**Parameters**

- `force` (vector3) - the force to be applied on the collision object, measured in Newton
- `position` (vector3) - the position where the force should be applied

**Examples**

Assuming the instance of the script has a collision-object-component with id "co":
```
-- apply a force of 1 Newton towards world-x at the center of the game object instance
msg.post("#co", "apply_force", {force = vmath.vector3(1, 0, 0), position = go.get_world_position()})

```

### collision_event
*Type:* MESSAGE
See physics.set_event_listener.
This message is sent to a function specified in physics.set_event_listener
when two collision objects collide.
This message only reports that a collision has occurred and will be sent once per frame and per colliding pair.
For more detailed information, check for the contact_point_event.

**Parameters**

- `a` (message.physics.collision_info) - collision information for object A
- `b` (message.physics.collision_info) - collision information for object B

**Examples**

How to take action when a collision occurs:
```
physics.set_event_listener(function(self, event, data)
  if event == hash("collision_event") then
      pprint(data)
      -- {
      --  a = {
      --          group = hash: [default],
      --          position = vmath.vector3(183, 666, 0),
      --          id = hash: [/go1]
      --      },
      --  b = {
      --          group = hash: [default],
      --          position = vmath.vector3(185, 704.05865478516, 0),
      --          id = hash: [/go2]
      --      }
      -- }
  end
end)

```

### collision_response
*Type:* MESSAGE
This message is broadcasted to every component of an instance that has a collision object,
when the collision object collides with another collision object. For a script to take action
when such a collision happens, it should check for this message in its on_message callback
function.
This message only reports that a collision actually happened and will only be sent once per
colliding pair and frame.
To retrieve more detailed information, check for the contact_point_response instead.

**Parameters**

- `other_id` (hash) - the id of the instance the collision object collided with
- `other_position` (vector3) - the world position of the instance the collision object collided with
- `other_group` (hash) - the collision group of the other collision object
- `own_group` (hash) - the collision group of the own collision object

**Examples**

How to take action when a collision occurs:
```
function on_message(self, message_id, message, sender)
    -- check for the message
    if message_id == hash("collision_response") then
        -- take action
    end
end

```

### contact_point_event
*Type:* MESSAGE
See physics.set_event_listener.
This message is sent to a function specified in physics.set_event_listener when
a collision object has contact points with another collision object.
Since multiple contact points can occur for two colliding objects, this event can be sent
multiple times in the same frame for the same two colliding objects. To only be notified once
when the collision occurs, check for the collision_event event instead.

**Parameters**

- `applied_impulse` (number) - the impulse the contact resulted in
- `distance` (number) - the penetration distance between the objects, which is always positive
- `a` (message.physics.contact_point_info) - contact point information for object A
- `b` (message.physics.contact_point_info) - contact point information for object B

**Examples**

How to take action when a contact point occurs:
```
physics.set_event_listener(function(self, events)
  for _,event in ipairs(events) do
    if event['type'] == hash("contact_point_event") then
        pprint(event)
        -- {
        --  applied_impulse = 310.00769042969,
        --  distance = 0.0714111328125,
        --  a = {
        --      position = vmath.vector3(446, 371, 0),
        --      relative_velocity = vmath.vector3(1.1722083854693e-06, -20.667181015015, -0),
        --      mass = 0,
        --      group = hash: [default],
        --      id = hash: [/flat],
        --      normal = vmath.vector3(-0, -1, -0)
        --  },
        --  b = {
        --      position = vmath.vector3(185, 657.92858886719, 0),
        --      relative_velocity = vmath.vector3(-1.1722083854693e-06, 20.667181015015, 0),
        --      mass = 10,
        --      group = hash: [default],
        --      id = hash: [/go2],
        --      normal = vmath.vector3(0, 1, 0)
        --  },
        --  type = hash: [contact_point_event]
        -- }
     end
   end
end)

```

### contact_point_response
*Type:* MESSAGE
This message is broadcasted to every component of an instance that has a collision object,
when the collision object has contact points with respect to another collision object.
For a script to take action when such contact points occur, it should check for this message
in its on_message callback function.
Since multiple contact points can occur for two colliding objects, this message can be sent
multiple times in the same frame for the same two colliding objects. To only be notified once
when the collision occurs, check for the collision_response message instead.

**Parameters**

- `position` (vector3) - world position of the contact point
- `normal` (vector3) - normal in world space of the contact point, which points from the other object towards the current object
- `relative_velocity` (vector3) - the relative velocity of the collision object as observed from the other object
- `distance` (number) - the penetration distance between the objects, which is always positive
- `applied_impulse` (number) - the impulse the contact resulted in
- `life_time` (number) - life time of the contact, <strong>not currently used</strong>
- `mass` (number) - the mass of the current collision object in kg
- `other_mass` (number) - the mass of the other collision object in kg
- `other_id` (hash) - the id of the instance the collision object is in contact with
- `other_position` (vector3) - the world position of the other collision object
- `other_group` (hash) - the collision group of the other collision object
- `own_group` (hash) - the collision group of the own collision object

**Examples**

How to take action when a contact point occurs:
```
function on_message(self, message_id, message, sender)
    -- check for the message
    if message_id == hash("contact_point_response") then
        -- take action
    end
end

```

### linear_damping
*Type:* PROPERTY
The linear damping value for the collision object. Setting this value alters the damping of
linear motion of the object. Valid values are between 0 (no damping) and 1 (full damping).

**Examples**

How to increase a collision object component's linear damping:
```
-- get linear damping from collision object "collisionobject" in gameobject "floater"
local target = "floater#collisionobject"
local damping = go.get(target, "linear_damping")
-- increase it by 10% if it's below 0.9
if damping <= 0.9 then
    go.set(target, "linear_damping", damping * 1.1)
end

```

### linear_velocity
*Type:* PROPERTY
The current linear velocity of the collision object component as a vector3.
The velocity is measured in units/s (pixels/s).

**Replaces:** request_velocity and velocity_response

**Examples**

How to query and modify a collision object component's linear velocity:
```
-- get linear velocity from collision object "collisionobject" in gameobject "ship"
local source = "ship#collisionobject"
local velocity = go.get(source, "linear_velocity")
-- decrease it by 10%
go.set(source, "linear_velocity", velocity * 0.9)
-- apply the velocity on target game object "boulder"'s collision object as a force
local target = "boulder#collisionobject"
local pos = go.get_position(target)
msg.post(target, "apply_force", { force = velocity, position = pos })

```

### mass
*Type:* PROPERTY
READ ONLY Returns the defined physical mass of the collision object component as a number.

**Examples**

How to query a collision object component's mass:
```
-- get mass from collision object component "boulder"
local mass = go.get("#boulder", "mass")
-- do something useful
assert(mass > 1)

```

### message.physics.collision_info
*Type:* STRUCT
collision object information

**Members**

- `position` (vector3) - object position in world space
- `id` (hash) - object identifier
- `group` (hash) - object collision group

### message.physics.contact_point_info
*Type:* STRUCT
contact-point object information

**Members**

- `position` (vector3) - contact point position in world space
- `instance_position` (vector3) - object position in world space
- `normal` (vector3) - contact normal pointing from the other object toward this object
- `relative_velocity` (vector3) - object velocity relative to the other object
- `mass` (number) - object mass in kilograms
- `id` (hash) - object identifier
- `group` (hash) - object collision group

### message.physics.trigger_info
*Type:* STRUCT
trigger interaction object information

**Members**

- `id` (hash) - object identifier
- `group` (hash) - object collision group

### physics.create_joint
*Type:* FUNCTION
Create a physics joint between two collision object components.
Note: Currently only supported in 2D physics.

**Parameters**

- `joint_type` (physics.JOINT_TYPE) - the joint type
- `collisionobject_a` (string | hash | url) - first collision object
- `joint_id` (string | hash) - id of the joint
- `position_a` (vector3) - local position where to attach the joint on the first collision object
- `collisionobject_b` (string | hash | url) - second collision object
- `position_b` (vector3) - local position where to attach the joint on the second collision object
- `properties` (physics.joint_properties) (optional) - optional joint-specific properties

### physics.destroy_joint
*Type:* FUNCTION
Destroy an already physics joint. The joint has to be created before a
destroy can be issued.
Note: Currently only supported in 2D physics.

**Parameters**

- `collisionobject` (string | hash | url) - collision object where the joint exist
- `joint_id` (string | hash) - id of the joint

### physics.event
*Type:* TYPEDEF
An event delivered to a physics world listener. Inspect its type field to
determine which event-specific fields are available.

**Parameters**

- `value` (message.physics.contact_point_event | message.physics.collision_event | message.physics.trigger_event | message.physics.ray_cast_response | message.physics.ray_cast_missed) - physics event data

### physics.get_gravity
*Type:* FUNCTION
Get the gravity in runtime. The gravity returned is not global, it will return
the gravity for the collection that the function is called from.
Note: For 2D physics the z component will always be zero.

**Returns**

- `gravity` (vector3) - gravity vector of collection

**Examples**

```
function init(self)
    local gravity = physics.get_gravity()
    -- Inverse gravity!
    gravity = -gravity
    physics.set_gravity(gravity)
end

```

### physics.get_group
*Type:* FUNCTION
Returns the group name of a collision object as a hash.

**Parameters**

- `url` (string | hash | url) - the collision object to return the group of.

**Returns**

- `group` (hash) - hash value of the group.

**Examples**

```
local function check_is_enemy()
    local group = physics.get_group("#collisionobject")
    return group == hash("enemy")
end

```

### physics.get_joint_properties
*Type:* FUNCTION
Get a table for properties for a connected joint. The joint has to be created before
properties can be retrieved.
Note: Currently only supported in 2D physics.

**Parameters**

- `collisionobject` (string | hash | url) - collision object where the joint exist
- `joint_id` (string | hash) - id of the joint

**Returns**

- `properties` (physics.joint_properties_info) - joint properties

### physics.get_joint_reaction_force
*Type:* FUNCTION
Get the reaction force for a joint. The joint has to be created before
the reaction force can be calculated.
Note: Currently only supported in 2D physics.

**Parameters**

- `collisionobject` (string | hash | url) - collision object where the joint exist
- `joint_id` (string | hash) - id of the joint

**Returns**

- `force` (vector3) - reaction force for the joint

### physics.get_joint_reaction_torque
*Type:* FUNCTION
Get the reaction torque for a joint. The joint has to be created before
the reaction torque can be calculated.
Note: Currently only supported in 2D physics.

**Parameters**

- `collisionobject` (string | hash | url) - collision object where the joint exist
- `joint_id` (string | hash) - id of the joint

**Returns**

- `torque` (number) - the reaction torque on bodyB in N*m.

### physics.get_maskbit
*Type:* FUNCTION
Returns true if the specified group is set in the mask of a collision
object, false otherwise.

**Parameters**

- `url` (string | hash | url) - the collision object to check the mask of.
- `group` (string) - the name of the group to check for.

**Returns**

- `maskbit` (boolean) - boolean value of the maskbit. 'true' if present, 'false' otherwise.

**Examples**

```
local function is_invincible()
    -- check if the collisionobject would collide with the "bullet" group
    local invincible = physics.get_maskbit("#collisionobject", "bullet")
    return invincible
end

```

### physics.get_shape
*Type:* FUNCTION
Gets collision shape data from a collision object

**Parameters**

- `url` (string | hash | url) - the collision object.
- `shape` (string | hash) - the name of the shape to get data for.

**Returns**

- `table` (physics.shape_data) - collision shape data

**Examples**

```
local function get_shape_meta()
    local sphere = physics.get_shape("#collisionobject", "my_sphere_shape")
    -- returns a table with sphere.diameter
    return sphere
end

```

### physics.joint_properties
*Type:* STRUCT
The available fields depend on the joint type.

**Members**

- `collide_connected?` (boolean) - whether the connected objects should collide
- `length?` (number) - Natural spring length between the anchor points.
- `frequency?` (number) - Mass-spring-damper frequency in Hertz; zero disables softness.
- `damping?` (number) - Damping ratio, where zero is no damping and one is critical damping.
- `max_length?` (number) - Maximum fixed-joint rope length.
- `local_axis_a?` (vector3) - Local translation unit axis in the first body.
- `reference_angle?` (number) - Angle of the second body relative to the first body, in radians.
- `lower_angle?` (number) - Lower angular limit in radians.
- `upper_angle?` (number) - Upper angular limit in radians.
- `lower_translation?` (number) - Lower translation limit, usually in meters.
- `upper_translation?` (number) - Upper translation limit, usually in meters.
- `max_motor_torque?` (number) - Maximum motor torque used to reach the desired speed, usually in N-m.
- `max_motor_force?` (number) - Maximum motor force used to reach the desired speed.
- `motor_speed?` (number) - Desired motor speed.
- `enable_limit?` (boolean) - Whether joint limits are enabled.
- `enable_motor?` (boolean) - Whether the joint motor is enabled.

### physics.joint_properties_info
*Type:* STRUCT
The available optional fields depend on the joint type.

**Members**

- `collide_connected` (boolean) - whether the connected objects collide
- `length?` (number) - spring length
- `frequency?` (number) - spring frequency
- `damping?` (number) - damping ratio
- `max_length?` (number) - fixed-joint maximum length
- `local_axis_a?` (vector3) - local joint axis
- `reference_angle?` (number) - reference angle
- `lower_angle?` (number) - lower angular limit
- `upper_angle?` (number) - upper angular limit
- `lower_translation?` (number) - lower translation limit
- `upper_translation?` (number) - upper translation limit
- `max_motor_torque?` (number) - maximum motor torque
- `max_motor_force?` (number) - maximum motor force
- `motor_speed?` (number) - motor speed
- `enable_limit?` (boolean) - whether limits are enabled
- `enable_motor?` (boolean) - whether the motor is enabled
- `joint_angle?` (number) - Read-only current hinge angle in radians.
- `joint_speed?` (number) - Read-only current hinge angular speed or slider/wheel translation speed.
- `joint_translation?` (number) - Read-only current slider or wheel translation, usually in meters.

### physics.JOINT_TYPE
*Type:* ENUM
Joint types

**Members**

- `physics.JOINT_TYPE_FIXED` - Fixed joint; uses <code>max_length</code> from <a href="/ref/physics#physics.joint_properties">physics.joint_properties</a>.
- `physics.JOINT_TYPE_HINGE` - Hinge joint; uses the angular-limit and motor fields from <a href="/ref/physics#physics.joint_properties">physics.joint_properties</a>.
- `physics.JOINT_TYPE_SLIDER` - Slider joint; uses the translation-limit and motor fields from <a href="/ref/physics#physics.joint_properties">physics.joint_properties</a>.
- `physics.JOINT_TYPE_SPRING` - Spring joint; uses <code>length</code>, <code>frequency</code>, and <code>damping</code> from <a href="/ref/physics#physics.joint_properties">physics.joint_properties</a>.
- `physics.JOINT_TYPE_WELD` - Weld joint; uses <code>reference_angle</code>, <code>frequency</code>, and <code>damping</code> from <a href="/ref/physics#physics.joint_properties">physics.joint_properties</a>.
- `physics.JOINT_TYPE_WHEEL` - Wheel joint; uses the axis, motor, frequency, and damping fields from <a href="/ref/physics#physics.joint_properties">physics.joint_properties</a>.

### physics.raycast
*Type:* FUNCTION
Ray casts are used to test for intersections against collision objects in the physics world.
Collision objects of types kinematic, dynamic and static are tested against. Trigger objects
do not intersect with ray casts.
Which collision objects to hit is filtered by their collision groups and can be configured
through groups.
NOTE: Ray casts will ignore collision objects that contain the starting point of the ray. This is a limitation in Box2D.

**Parameters**

- `from` (vector3) - the world position of the start of the ray
- `to` (vector3) - the world position of the end of the ray
- `groups` (hash[]) - a lua table containing the hashed groups for which to test collisions against
- `options` (physics.raycast_options) (optional) - optional ray-cast options

**Returns**

- `result` (message.physics.ray_cast_response[] | message.physics.ray_cast_response | nil) - It returns a list. If missed it returns <code>nil</code>. See <a href="#ray_cast_response">ray_cast_response</a> for details on the returned values.

**Examples**

How to perform a ray cast synchronously:
```
function init(self)
    self.groups = {hash("world"), hash("enemy")}
end

function update(self, dt)
    -- request ray cast
    local result = physics.raycast(from, to, self.groups, {all=true})
    if result ~= nil then
        -- act on the hit (see 'ray_cast_response')
        for _,result in ipairs(results) do
            handle_result(result)
        end
    end
end

```

### physics.raycast_async
*Type:* FUNCTION
Ray casts are used to test for intersections against collision objects in the physics world.
Collision objects of types kinematic, dynamic and static are tested against. Trigger objects
do not intersect with ray casts.
Which collision objects to hit is filtered by their collision groups and can be configured
through groups.
The actual ray cast will be performed during the physics-update.

If an object is hit, the result will be reported via a ray_cast_response message.
If there is no object hit, the result will be reported via a ray_cast_missed message.

NOTE: Ray casts will ignore collision objects that contain the starting point of the ray. This is a limitation in Box2D.

**Parameters**

- `from` (vector3) - the world position of the start of the ray
- `to` (vector3) - the world position of the end of the ray
- `groups` (hash[]) - a lua table containing the hashed groups for which to test collisions against
- `request_id` (integer) (optional) - a number in range [0,255]. It will be sent back in the response for identification, 0 by default

**Examples**

How to perform a ray cast asynchronously:
```
function init(self)
    self.my_groups = {hash("my_group1"), hash("my_group2")}
end

function update(self, dt)
    -- request ray cast
    physics.raycast_async(my_start, my_end, self.my_groups)
end

function on_message(self, message_id, message, sender)
    -- check for the response
    if message_id == hash("ray_cast_response") then
        -- act on the hit
    elseif message_id == hash("ray_cast_missed") then
        -- act on the miss
    end
end

```

### physics.raycast_options
*Type:* STRUCT
Ray-cast options

**Members**

- `all?` (boolean) - Return every hit instead of only the closest hit.

### physics.set_event_listener
*Type:* FUNCTION
Only one physics world event listener can be set at a time.

**Parameters**

- `callback` (fun(self:script_instance, events:physics.event[]) | nil) - A callback that receives information about all physics interactions in this physics world. Pass <code>nil</code> to remove the listener.
<dl>
<dt class="api-lua-v2-type-definition"><code>self:<a href="../builtins-lua/#script_instance">script_instance</a></code></dt>
<dd>The calling script instance</dd>
<dt class="api-lua-v2-type-definition"><code>events:<a href="#physics.event">physics.event</a>[]</code></dt>
<dd>An array of event tables. Each event table contains a <code>type</code> field with the hashed name of one of these messages, together with fields specific to that event type:</dd>
</dl>
<ul>
<li><a href="#contact_point_event">contact_point_event</a></li>
<li><a href="#collision_event">collision_event</a></li>
<li><a href="#trigger_event">trigger_event</a></li>
<li><a href="#ray_cast_response">ray_cast_response</a></li>
<li><a href="#ray_cast_missed">ray_cast_missed</a></li>
</ul>

**Examples**

```
local function physics_world_listener(self, events)
  for _,event in ipairs(events) do
      local event_type = event["type"]
      if event_type == hash("contact_point_event") then
          pprint(event)
          -- {
          --  distance = 2.1490633487701,
          --  applied_impulse = 0
          --  a = { --[[0x113f7c6c0]]
          --    group = hash: [box],
          --    id = hash: [/box]
          --    mass = 0,
          --    normal = vmath.vector3(0.379, 0.925, -0),
          --    position = vmath.vector3(517.337, 235.068, 0),
          --    instance_position = vmath.vector3(480, 144, 0),
          --    relative_velocity = vmath.vector3(-0, -0, -0),
          --  },
          --  b = { --[[0x113f7c840]]
          --    group = hash: [circle],
          --    id = hash: [/circle]
          --    mass = 0,
          --    normal = vmath.vector3(-0.379, -0.925, 0),
          --    position = vmath.vector3(517.337, 235.068, 0),
          --    instance_position = vmath.vector3(-0.0021, 0, -0.0022),
          --    relative_velocity = vmath.vector3(0, 0, 0),
          --  },
          -- }
      elseif event_type == hash("collision_event") then
          pprint(event)
          -- {
          --  a = {
          --          group = hash: [default],
          --          position = vmath.vector3(183, 666, 0),
          --          id = hash: [/go1]
          --      },
          --  b = {
          --          group = hash: [default],
          --          position = vmath.vector3(185, 704.05865478516, 0),
          --          id = hash: [/go2]
          --      }
          -- }
      elseif event_type ==  hash("trigger_event") then
          pprint(event)
          -- {
          --  enter = true,
          --  b = {
          --      group = hash: [default],
          --      id = hash: [/go2]
          --  },
          --  a = {
          --      group = hash: [default],
          --      id = hash: [/go1]
          --  }
          -- },
      elseif event_type ==  hash("ray_cast_response") then
          pprint(event)
          --{
          --  group = hash: [default],
          --  request_id = 0,
          --  position = vmath.vector3(249.92222595215, 249.92222595215, 0),
          --  fraction = 0.68759721517563,
          --  normal = vmath.vector3(0, 1, 0),
          --  id = hash: [/go]
          -- }
      elseif event_type ==  hash("ray_cast_missed") then
          pprint(event)
          -- {
          --  request_id = 0
          --},
      end
end

function init(self)
    physics.set_event_listener(physics_world_listener)
end

```

### physics.set_gravity
*Type:* FUNCTION
Set the gravity in runtime. The gravity change is not global, it will only affect
the collection that the function is called from.
Note: For 2D physics the z component of the gravity vector will be ignored.

**Parameters**

- `gravity` (vector3) - the new gravity vector

**Examples**

```
function init(self)
    -- Set "upside down" gravity for this collection.
    physics.set_gravity(vmath.vector3(0, 10.0, 0))
end

```

### physics.set_group
*Type:* FUNCTION
Updates the group property of a collision object to the specified
string value. The group name should exist i.e. have been used in
a collision object in the editor.

**Parameters**

- `url` (string | hash | url) - the collision object affected.
- `group` (string) - the new group name to be assigned.

**Examples**

```
local function change_collision_group()
     physics.set_group("#collisionobject", "enemy")
end

```

### physics.set_hflip
*Type:* FUNCTION
Flips the collision shapes horizontally for a collision object

**Parameters**

- `url` (string | hash | url) - the collision object that should flip its shapes
- `flip` (boolean) - <code>true</code> if the collision object should flip its shapes, <code>false</code> if not

**Examples**

```
function init(self)
    self.fliph = true -- set on some condition
    physics.set_hflip("#collisionobject", self.fliph)
end

```

### physics.set_joint_properties
*Type:* FUNCTION
Updates the properties for an already connected joint. The joint has to be created before
properties can be changed.
Note: Currently only supported in 2D physics.

**Parameters**

- `collisionobject` (string | hash | url) - collision object where the joint exist
- `joint_id` (string | hash) - id of the joint
- `properties` (physics.joint_properties) - joint specific properties table
Note: The <code>collide_connected</code> field cannot be updated/changed after a connection has been made.

### physics.set_maskbit
*Type:* FUNCTION
Sets or clears the masking of a group (maskbit) in a collision object.

**Parameters**

- `url` (string | hash | url) - the collision object to change the mask of.
- `group` (string) - the name of the group (maskbit) to modify in the mask.
- `maskbit` (boolean) - boolean value of the new maskbit. 'true' to enable, 'false' to disable.

**Examples**

```
local function make_invincible()
    -- no longer collide with the "bullet" group
    physics.set_maskbit("#collisionobject", "bullet", false)
end

```

### physics.set_shape
*Type:* FUNCTION
Sets collision shape data for a collision object. Please note that updating data in 3D
can be quite costly for box and capsules. Because of the physics engine, the cost
comes from having to recreate the shape objects when certain shapes needs to be updated.

**Parameters**

- `url` (string | hash | url) - the collision object.
- `shape` (string | hash) - the name of the shape to get data for.
- `table` (physics.shape_data) - updated collision shape data
Hull and mesh geometry cannot be changed with this function.

**Examples**

```
local function set_shape_data()
    -- set capsule shape data
    local data = {}
    data.type = physics.SHAPE_TYPE_CAPSULE
    data.diameter = 10
    data.height = 20
    physics.set_shape("#collisionobject", "my_capsule_shape", data)

    -- set sphere shape data
    data = {}
    data.type = physics.SHAPE_TYPE_SPHERE
    data.diameter = 10
    physics.set_shape("#collisionobject", "my_sphere_shape", data)

    -- set box shape data
    data = {}
    data.type = physics.SHAPE_TYPE_BOX
    data.dimensions = vmath.vector3(10, 10, 5)
    physics.set_shape("#collisionobject", "my_box_shape", data)
end

```

### physics.set_vflip
*Type:* FUNCTION
Flips the collision shapes vertically for a collision object

**Parameters**

- `url` (string | hash | url) - the collision object that should flip its shapes
- `flip` (boolean) - <code>true</code> if the collision object should flip its shapes, <code>false</code> if not

**Examples**

```
function init(self)
    self.flipv = true -- set on some condition
    physics.set_vflip("#collisionobject", self.flipv)
end

```

### physics.shape_data
*Type:* STRUCT
The available geometry fields depend on type.

**Members**

- `type` (physics.SHAPE_TYPE) - shape type
- `diameter?` (number) - sphere diameter or capsule pole diameter
- `dimensions?` (vector3) - box dimensions
- `height?` (number) - capsule height

### physics.SHAPE_TYPE
*Type:* ENUM
Shape types

**Members**

- `physics.SHAPE_TYPE_BOX` - Box shape.
- `physics.SHAPE_TYPE_CAPSULE` - Capsule shape; supported only by 3D physics.
- `physics.SHAPE_TYPE_HULL` - Convex hull shape.
- `physics.SHAPE_TYPE_MESH` - Triangle mesh shape; supported only by the Bullet 3D backend.
- `physics.SHAPE_TYPE_SPHERE` - Sphere shape.

### physics.update_mass
*Type:* FUNCTION
The function recalculates the density of each shape based on the total area of all shapes and the specified mass, then updates the mass of the body accordingly.
Note: Currently only supported in 2D physics.

**Parameters**

- `collisionobject` (string | hash | url) - the collision object whose mass needs to be updated.
- `mass` (number) - the new mass value to set for the collision object.

**Examples**

```
 physics.update_mass("#collisionobject", 14)

```

### physics.wakeup
*Type:* FUNCTION
Collision objects tend to fall asleep when inactive for a small period of time for
efficiency reasons. This function wakes them up.

**Parameters**

- `url` (string | hash | url) - the collision object to wake.

**Examples**

```
function on_input(self, action_id, action)
    if action_id == hash("test") and action.pressed then
        physics.wakeup("#collisionobject")
    end
end

```

### ray_cast_missed
*Type:* MESSAGE
This message is sent back to the sender of a ray_cast_request, or to the physics world listener
if it is set (see physics.set_event_listener), if the ray didn't hit any collision object.
See physics.raycast_async for examples of how to use it.

**Parameters**

- `request_id` (integer) - id supplied when the ray cast was requested

### ray_cast_response
*Type:* MESSAGE
This message is sent back to the sender of a ray_cast_request, or to the physics world listener
if it is set (see physics.set_event_listener), if the ray hits a collision object.
See physics.raycast_async for examples of how to use it.

**Parameters**

- `fraction` (number) - the fraction of the hit measured along the ray, where 0 is the start of the ray and 1 is the end
- `position` (vector3) - the world position of the hit
- `normal` (vector3) - the normal of the surface of the collision object where it was hit
- `id` (hash) - the instance id of the hit collision object
- `group` (hash) - the collision group of the hit collision object as a hashed name
- `request_id` (integer) - id supplied when the ray cast was requested

### trigger_event
*Type:* MESSAGE
See physics.set_event_listener.
This message is sent to a function specified in physics.set_event_listener
when a collision object interacts with another collision object and one of them is a trigger.
This message only reports that an interaction actually happened and will be sent once per colliding pair and frame.
For more detailed information, check for the contact_point_event.

**Parameters**

- `enter` (boolean) - if the interaction was an entry or not
- `a` (message.physics.trigger_info) - interaction information for object A
- `b` (message.physics.trigger_info) - interaction information for object B

**Examples**

How to take action when a trigger interaction occurs:
```
physics.set_event_listener(function(self, event, data)
 if event ==  hash("trigger_event") then
     if data.enter then
        -- take action for entry
     else
        -- take action for exit
     end
     pprint(data)
     -- {
     --  enter = true,
     --  b = {
     --      group = hash: [default],
     --      id = hash: [/go2]
     --  },
     --  a = {
     --      group = hash: [default],
     --      id = hash: [/go1]
     --  }
     -- },
  end
end)

```

### trigger_response
*Type:* MESSAGE
This message is broadcasted to every component of an instance that has a collision object,
when the collision object interacts with another collision object and one of them is a trigger.
For a script to take action when such an interaction happens, it should check for this message
in its on_message callback function.
This message only reports that an interaction actually happened and will only be sent once per
colliding pair and frame. To retrieve more detailed information, check for the
contact_point_response instead.

**Parameters**

- `other_id` (hash) - the id of the instance the collision object collided with
- `enter` (boolean) - if the interaction was an entry or not
- `other_group` (hash) - the collision group of the triggering collision object
- `own_group` (hash) - the collision group of the own collision object

**Examples**

How to take action when a trigger interaction occurs:
```
function on_message(self, message_id, message, sender)
    -- check for the message
    if message_id == hash("trigger_response") then
        if message.enter then
            -- take action for entry
        else
            -- take action for exit
        end
    end
end

```
