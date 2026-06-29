# b2d.joint

**Namespace:** `b2d.joint`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d_joint_v2.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/v2/script_box2d_joint_v2.cpp`

Functions for interacting with native Box2D joints.

## API

### b2d.joint.create_distance
*Type:* FUNCTION
Create a distance joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>length</code>, <code>frequency</code>, <code>damping_ratio</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_distance
*Type:* FUNCTION
Create a distance joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>length</code>, <code>min_length</code>, <code>max_length</code>, <code>enable_spring</code>, <code>hertz</code> or <code>frequency</code>, <code>damping_ratio</code>, <code>enable_limit</code>, <code>enable_motor</code>, <code>max_motor_force</code>, <code>motor_speed</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_filter
*Type:* FUNCTION
Create a filter joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition table

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_friction
*Type:* FUNCTION
Create a friction joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>max_force</code>, <code>max_torque</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_gear
*Type:* FUNCTION
Create a gear joint.

**Parameters**

- `joint1` (b2Joint) - first revolute or prismatic joint
- `joint2` (b2Joint) - second revolute or prismatic joint
- `definition` (table) - optional definition with <code>ratio</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_motor
*Type:* FUNCTION
Create a motor joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>linear_offset</code>, <code>angular_offset</code>, <code>max_force</code>, <code>max_torque</code>, <code>correction_factor</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_mouse
*Type:* FUNCTION
Create a mouse joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>target</code>, <code>max_force</code>, <code>frequency</code>, <code>damping_ratio</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_mouse
*Type:* FUNCTION
Create a mouse joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>target</code>, <code>hertz</code> or <code>frequency</code>, <code>damping_ratio</code>, <code>max_force</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_prismatic
*Type:* FUNCTION
Create a prismatic joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>local_axis_a</code>, <code>reference_angle</code>, <code>enable_limit</code>, <code>lower_translation</code>, <code>upper_translation</code>, <code>enable_motor</code>, <code>max_motor_force</code>, <code>motor_speed</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_prismatic
*Type:* FUNCTION
Create a prismatic joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>local_axis_a</code>, <code>reference_angle</code>, <code>enable_spring</code>, <code>hertz</code> or <code>frequency</code>, <code>damping_ratio</code>, <code>enable_limit</code>, <code>lower_translation</code>, <code>upper_translation</code>, <code>enable_motor</code>, <code>max_motor_force</code>, <code>motor_speed</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_pulley
*Type:* FUNCTION
Create a pulley joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>ground_anchor_a</code>, <code>ground_anchor_b</code>, <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>length_a</code>, <code>length_b</code>, <code>ratio</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_revolute
*Type:* FUNCTION
Create a revolute joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>reference_angle</code>, <code>enable_limit</code>, <code>lower_angle</code>, <code>upper_angle</code>, <code>enable_motor</code>, <code>max_motor_torque</code>, <code>motor_speed</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_revolute
*Type:* FUNCTION
Create a revolute joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>reference_angle</code>, <code>enable_spring</code>, <code>hertz</code> or <code>frequency</code>, <code>damping_ratio</code>, <code>enable_limit</code>, <code>lower_angle</code>, <code>upper_angle</code>, <code>enable_motor</code>, <code>max_motor_torque</code>, <code>motor_speed</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_rope
*Type:* FUNCTION
Create a rope joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>max_length</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_weld
*Type:* FUNCTION
Create a weld joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>reference_angle</code>, <code>frequency</code>, <code>damping_ratio</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_weld
*Type:* FUNCTION
Create a weld joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>reference_angle</code>, <code>linear_hertz</code>, <code>angular_hertz</code>, <code>linear_damping_ratio</code>, <code>angular_damping_ratio</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_wheel
*Type:* FUNCTION
Create a wheel joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>local_axis_a</code>, <code>enable_motor</code>, <code>max_motor_torque</code>, <code>motor_speed</code>, <code>frequency</code>, <code>damping_ratio</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.create_wheel
*Type:* FUNCTION
Create a wheel joint.

**Parameters**

- `body_a` (b2Body) - first body
- `body_b` (b2Body) - second body
- `definition` (table) - optional definition with <code>local_anchor_a</code>, <code>local_anchor_b</code>, <code>local_axis_a</code>, <code>enable_spring</code>, <code>hertz</code> or <code>frequency</code>, <code>damping_ratio</code>, <code>enable_limit</code>, <code>lower_translation</code>, <code>upper_translation</code>, <code>enable_motor</code>, <code>max_motor_torque</code>, <code>motor_speed</code>, and <code>collide_connected</code>

**Returns**

- `joint` (b2Joint) - created joint

### b2d.joint.destroy
*Type:* FUNCTION
Destroy a joint created by b2d.joint.

**Parameters**

- `joint` (b2Joint) - joint

### b2d.joint.destroy
*Type:* FUNCTION
Destroy a joint created by b2d.joint.

**Parameters**

- `joint` (b2Joint) - joint

### b2d.joint.enable_limit
*Type:* FUNCTION
Enable or disable joint limits.

**Parameters**

- `joint` (b2Joint) - prismatic or revolute joint
- `enable` (boolean) - true to enable limits

### b2d.joint.enable_limit
*Type:* FUNCTION
Enable or disable joint limits.

**Parameters**

- `joint` (b2Joint) - distance, prismatic, revolute, or wheel joint
- `enable` (boolean) - true to enable limits

### b2d.joint.enable_motor
*Type:* FUNCTION
Enable or disable the joint motor.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or wheel joint
- `enable` (boolean) - true to enable the motor

### b2d.joint.enable_motor
*Type:* FUNCTION
Enable or disable the joint motor.

**Parameters**

- `joint` (b2Joint) - distance, prismatic, revolute, or wheel joint
- `enable` (boolean) - true to enable the motor

### b2d.joint.enable_spring
*Type:* FUNCTION
Enable or disable joint spring behavior.

**Parameters**

- `joint` (b2Joint) - distance, prismatic, revolute, or wheel joint
- `enable` (boolean) - true to enable the spring

### b2d.joint.get_anchor_a
*Type:* FUNCTION
Get the world anchor on body A.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `anchor` (vector3) - world anchor

### b2d.joint.get_anchor_a
*Type:* FUNCTION
Get the world anchor on body A.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `anchor` (vector3) - world anchor

### b2d.joint.get_anchor_b
*Type:* FUNCTION
Get the world anchor on body B.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `anchor` (vector3) - world anchor

### b2d.joint.get_anchor_b
*Type:* FUNCTION
Get the world anchor on body B.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `anchor` (vector3) - world anchor

### b2d.joint.get_angular_damping_ratio
*Type:* FUNCTION
Get weld joint angular damping ratio.

**Parameters**

- `joint` (b2Joint) - weld joint

**Returns**

- `ratio` (number) - damping ratio

### b2d.joint.get_angular_hertz
*Type:* FUNCTION
Get weld joint angular frequency.

**Parameters**

- `joint` (b2Joint) - weld joint

**Returns**

- `hertz` (number) - frequency in hertz

### b2d.joint.get_angular_offset
*Type:* FUNCTION
Get motor joint angular offset.

**Parameters**

- `joint` (b2Joint) - motor joint

**Returns**

- `offset` (number) - angular offset in radians

### b2d.joint.get_body_a
*Type:* FUNCTION
Get the first body connected to a joint.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `body` (b2Body) - body A

### b2d.joint.get_body_a
*Type:* FUNCTION
Get the first body connected to a joint.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `body` (b2Body) - body A

### b2d.joint.get_body_b
*Type:* FUNCTION
Get the second body connected to a joint.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `body` (b2Body) - body B

### b2d.joint.get_body_b
*Type:* FUNCTION
Get the second body connected to a joint.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `body` (b2Body) - body B

### b2d.joint.get_collide_connected
*Type:* FUNCTION
Get whether connected bodies can collide.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `collide` (boolean) - true if connected bodies can collide

### b2d.joint.get_collide_connected
*Type:* FUNCTION
Get whether connected bodies can collide.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `collide` (boolean) - true if connected bodies can collide

### b2d.joint.get_correction_factor
*Type:* FUNCTION
Get motor joint correction factor.

**Parameters**

- `joint` (b2Joint) - motor joint

**Returns**

- `factor` (number) - correction factor

### b2d.joint.get_current_length
*Type:* FUNCTION
Get the current distance joint length.

**Parameters**

- `joint` (b2Joint) - distance joint

**Returns**

- `length` (number) - current length in project units

### b2d.joint.get_damping_ratio
*Type:* FUNCTION
Get spring damping ratio.

**Parameters**

- `joint` (b2Joint) - distance, mouse, weld, or wheel joint

**Returns**

- `ratio` (number) - damping ratio

### b2d.joint.get_damping_ratio
*Type:* FUNCTION
Alias for b2d.joint.get_spring_damping_ratio.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint

**Returns**

- `ratio` (number) - damping ratio

### b2d.joint.get_frequency
*Type:* FUNCTION
Get spring frequency.

**Parameters**

- `joint` (b2Joint) - distance, mouse, weld, or wheel joint

**Returns**

- `frequency` (number) - frequency in hertz

### b2d.joint.get_frequency
*Type:* FUNCTION
Alias for b2d.joint.get_spring_hertz.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint

**Returns**

- `frequency` (number) - frequency in hertz

### b2d.joint.get_ground_anchor_a
*Type:* FUNCTION
Get pulley ground anchor A.

**Parameters**

- `joint` (b2Joint) - pulley joint

**Returns**

- `anchor` (vector3) - world anchor

### b2d.joint.get_ground_anchor_b
*Type:* FUNCTION
Get pulley ground anchor B.

**Parameters**

- `joint` (b2Joint) - pulley joint

**Returns**

- `anchor` (vector3) - world anchor

### b2d.joint.get_hertz
*Type:* FUNCTION
Alias for b2d.joint.get_frequency.

**Parameters**

- `joint` (b2Joint) - distance, mouse, weld, or wheel joint

**Returns**

- `hertz` (number) - frequency in hertz

### b2d.joint.get_hertz
*Type:* FUNCTION
Alias for b2d.joint.get_spring_hertz.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint

**Returns**

- `hertz` (number) - frequency in hertz

### b2d.joint.get_joint1
*Type:* FUNCTION
Get the first joint connected to a gear joint.

**Parameters**

- `joint` (b2Joint) - gear joint

**Returns**

- `joint1` (b2Joint) - first connected joint

### b2d.joint.get_joint2
*Type:* FUNCTION
Get the second joint connected to a gear joint.

**Parameters**

- `joint` (b2Joint) - gear joint

**Returns**

- `joint2` (b2Joint) - second connected joint

### b2d.joint.get_joint_angle
*Type:* FUNCTION
Get revolute joint angle.

**Parameters**

- `joint` (b2Joint) - revolute joint

**Returns**

- `angle` (number) - angle in radians

### b2d.joint.get_joint_angle
*Type:* FUNCTION
Get revolute joint angle.

**Parameters**

- `joint` (b2Joint) - revolute joint

**Returns**

- `angle` (number) - angle in radians

### b2d.joint.get_joint_speed
*Type:* FUNCTION
Get joint speed.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or wheel joint

**Returns**

- `speed` (number) - joint speed

### b2d.joint.get_joint_speed
*Type:* FUNCTION
Get joint speed.

**Parameters**

- `joint` (b2Joint) - prismatic joint

**Returns**

- `speed` (number) - joint speed

### b2d.joint.get_joint_translation
*Type:* FUNCTION
Get joint translation.

**Parameters**

- `joint` (b2Joint) - prismatic or wheel joint

**Returns**

- `translation` (number) - translation in project units

### b2d.joint.get_joint_translation
*Type:* FUNCTION
Get joint translation.

**Parameters**

- `joint` (b2Joint) - prismatic joint

**Returns**

- `translation` (number) - translation in project units

### b2d.joint.get_length
*Type:* FUNCTION
Get the distance joint length.

**Parameters**

- `joint` (b2Joint) - distance joint

**Returns**

- `length` (number) - length in project units

### b2d.joint.get_length
*Type:* FUNCTION
Get the distance joint length.

**Parameters**

- `joint` (b2Joint) - distance joint

**Returns**

- `length` (number) - length in project units

### b2d.joint.get_length_a
*Type:* FUNCTION
Get pulley segment length A.

**Parameters**

- `joint` (b2Joint) - pulley joint

**Returns**

- `length` (number) - length in project units

### b2d.joint.get_length_b
*Type:* FUNCTION
Get pulley segment length B.

**Parameters**

- `joint` (b2Joint) - pulley joint

**Returns**

- `length` (number) - length in project units

### b2d.joint.get_limit_state
*Type:* FUNCTION
Get rope limit state.

**Parameters**

- `joint` (b2Joint) - rope joint

**Returns**

- `state` (number) - one of the <code>LIMIT_STATE_*</code> constants

### b2d.joint.get_linear_damping_ratio
*Type:* FUNCTION
Get weld joint linear damping ratio.

**Parameters**

- `joint` (b2Joint) - weld joint

**Returns**

- `ratio` (number) - damping ratio

### b2d.joint.get_linear_hertz
*Type:* FUNCTION
Get weld joint linear frequency.

**Parameters**

- `joint` (b2Joint) - weld joint

**Returns**

- `hertz` (number) - frequency in hertz

### b2d.joint.get_linear_offset
*Type:* FUNCTION
Get motor joint linear offset.

**Parameters**

- `joint` (b2Joint) - motor joint

**Returns**

- `offset` (vector3) - linear offset in project units

### b2d.joint.get_local_anchor_a
*Type:* FUNCTION
Get the local anchor on body A.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `anchor` (vector3) - local anchor

### b2d.joint.get_local_anchor_a
*Type:* FUNCTION
Get the local anchor on body A.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `anchor` (vector3) - local anchor

### b2d.joint.get_local_anchor_b
*Type:* FUNCTION
Get the local anchor on body B.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `anchor` (vector3) - local anchor

### b2d.joint.get_local_anchor_b
*Type:* FUNCTION
Get the local anchor on body B.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `anchor` (vector3) - local anchor

### b2d.joint.get_local_axis_a
*Type:* FUNCTION
Get the local axis on body A.

**Parameters**

- `joint` (b2Joint) - prismatic or wheel joint

**Returns**

- `axis` (vector3) - local axis

### b2d.joint.get_lower_limit
*Type:* FUNCTION
Get the lower joint limit.

**Parameters**

- `joint` (b2Joint) - prismatic or revolute joint

**Returns**

- `lower` (number) - lower limit

### b2d.joint.get_lower_limit
*Type:* FUNCTION
Get the lower joint limit.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or wheel joint

**Returns**

- `lower` (number) - lower limit

### b2d.joint.get_max_force
*Type:* FUNCTION
Get maximum force.

**Parameters**

- `joint` (b2Joint) - mouse or friction joint

**Returns**

- `force` (number) - maximum force

### b2d.joint.get_max_force
*Type:* FUNCTION
Get maximum force.

**Parameters**

- `joint` (b2Joint) - mouse or motor joint

**Returns**

- `force` (number) - maximum force

### b2d.joint.get_max_length
*Type:* FUNCTION
Get rope maximum length.

**Parameters**

- `joint` (b2Joint) - rope joint

**Returns**

- `length` (number) - maximum length in project units

### b2d.joint.get_max_length
*Type:* FUNCTION
Get the distance joint maximum length.

**Parameters**

- `joint` (b2Joint) - distance joint

**Returns**

- `length` (number) - maximum length in project units

### b2d.joint.get_max_motor_force
*Type:* FUNCTION
Get maximum motor force.

**Parameters**

- `joint` (b2Joint) - prismatic joint

**Returns**

- `force` (number) - maximum motor force

### b2d.joint.get_max_motor_force
*Type:* FUNCTION
Get maximum motor force.

**Parameters**

- `joint` (b2Joint) - distance or prismatic joint

**Returns**

- `force` (number) - maximum motor force

### b2d.joint.get_max_motor_torque
*Type:* FUNCTION
Get maximum motor torque.

**Parameters**

- `joint` (b2Joint) - revolute or wheel joint

**Returns**

- `torque` (number) - maximum motor torque

### b2d.joint.get_max_motor_torque
*Type:* FUNCTION
Get maximum motor torque.

**Parameters**

- `joint` (b2Joint) - revolute or wheel joint

**Returns**

- `torque` (number) - maximum motor torque

### b2d.joint.get_max_torque
*Type:* FUNCTION
Get maximum torque.

**Parameters**

- `joint` (b2Joint) - friction joint

**Returns**

- `torque` (number) - maximum torque

### b2d.joint.get_max_torque
*Type:* FUNCTION
Get maximum torque.

**Parameters**

- `joint` (b2Joint) - motor joint

**Returns**

- `torque` (number) - maximum torque

### b2d.joint.get_min_length
*Type:* FUNCTION
Get the distance joint minimum length.

**Parameters**

- `joint` (b2Joint) - distance joint

**Returns**

- `length` (number) - minimum length in project units

### b2d.joint.get_motor_force
*Type:* FUNCTION
Get current motor force.

**Parameters**

- `joint` (b2Joint) - prismatic joint
- `inv_dt` (number) - inverse time step

**Returns**

- `force` (number) - motor force

### b2d.joint.get_motor_force
*Type:* FUNCTION
Get current motor force.

**Parameters**

- `joint` (b2Joint) - distance or prismatic joint

**Returns**

- `force` (number) - motor force

### b2d.joint.get_motor_speed
*Type:* FUNCTION
Get motor speed.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or wheel joint

**Returns**

- `speed` (number) - motor speed

### b2d.joint.get_motor_speed
*Type:* FUNCTION
Get motor speed.

**Parameters**

- `joint` (b2Joint) - distance, prismatic, revolute, or wheel joint

**Returns**

- `speed` (number) - motor speed

### b2d.joint.get_motor_torque
*Type:* FUNCTION
Get current motor torque.

**Parameters**

- `joint` (b2Joint) - revolute or wheel joint
- `inv_dt` (number) - inverse time step

**Returns**

- `torque` (number) - motor torque

### b2d.joint.get_motor_torque
*Type:* FUNCTION
Get current motor torque.

**Parameters**

- `joint` (b2Joint) - revolute or wheel joint

**Returns**

- `torque` (number) - motor torque

### b2d.joint.get_mouse_target
*Type:* FUNCTION
Get the target for a mouse joint.

**Parameters**

- `joint` (b2Joint) - mouse joint

**Returns**

- `target` (vector3) - world target

### b2d.joint.get_mouse_target
*Type:* FUNCTION
Get the target for a mouse joint.

**Parameters**

- `joint` (b2Joint) - mouse joint

**Returns**

- `target` (vector3) - world target

### b2d.joint.get_ratio
*Type:* FUNCTION
Get joint ratio.

**Parameters**

- `joint` (b2Joint) - pulley or gear joint

**Returns**

- `ratio` (number) - joint ratio

### b2d.joint.get_reaction_force
*Type:* FUNCTION
Get reaction force.

**Parameters**

- `joint` (b2Joint) - joint
- `inv_dt` (number) - inverse time step

**Returns**

- `force` (vector3) - reaction force

### b2d.joint.get_reaction_force
*Type:* FUNCTION
Get reaction force.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `force` (vector3) - reaction force

### b2d.joint.get_reaction_torque
*Type:* FUNCTION
Get reaction torque.

**Parameters**

- `joint` (b2Joint) - joint
- `inv_dt` (number) - inverse time step

**Returns**

- `torque` (number) - reaction torque

### b2d.joint.get_reaction_torque
*Type:* FUNCTION
Get reaction torque.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `torque` (number) - reaction torque

### b2d.joint.get_reference_angle
*Type:* FUNCTION
Get the reference angle.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or weld joint

**Returns**

- `angle` (number) - reference angle in radians

### b2d.joint.get_reference_angle
*Type:* FUNCTION
Get weld joint reference angle.

**Parameters**

- `joint` (b2Joint) - weld joint

**Returns**

- `angle` (number) - reference angle in radians

### b2d.joint.get_spring_damping_ratio
*Type:* FUNCTION
Alias for b2d.joint.get_damping_ratio.

**Parameters**

- `joint` (b2Joint) - distance, mouse, weld, or wheel joint

**Returns**

- `ratio` (number) - damping ratio

### b2d.joint.get_spring_damping_ratio
*Type:* FUNCTION
Get spring damping ratio.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint

**Returns**

- `ratio` (number) - damping ratio

### b2d.joint.get_spring_hertz
*Type:* FUNCTION
Get spring frequency.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint

**Returns**

- `hertz` (number) - frequency in hertz

### b2d.joint.get_type
*Type:* FUNCTION
Get the joint type.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `type` (number) - one of the <code>JOINT_TYPE_*</code> constants

### b2d.joint.get_type
*Type:* FUNCTION
Get the joint type.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `type` (number) - one of the <code>JOINT_TYPE_*</code> constants

### b2d.joint.get_upper_limit
*Type:* FUNCTION
Get the upper joint limit.

**Parameters**

- `joint` (b2Joint) - prismatic or revolute joint

**Returns**

- `upper` (number) - upper limit

### b2d.joint.get_upper_limit
*Type:* FUNCTION
Get the upper joint limit.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or wheel joint

**Returns**

- `upper` (number) - upper limit

### b2d.joint.get_world
*Type:* FUNCTION
Get the world owning a joint.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `world` (b2World) - owning world

### b2d.joint.is_active
*Type:* FUNCTION
Get whether the joint is active.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `active` (boolean) - true if the joint is active

### b2d.joint.is_limit_enabled
*Type:* FUNCTION
Get whether joint limits are enabled.

**Parameters**

- `joint` (b2Joint) - prismatic or revolute joint

**Returns**

- `enabled` (boolean) - true if limits are enabled

### b2d.joint.is_limit_enabled
*Type:* FUNCTION
Get whether joint limits are enabled.

**Parameters**

- `joint` (b2Joint) - distance, prismatic, revolute, or wheel joint

**Returns**

- `enabled` (boolean) - true if limits are enabled

### b2d.joint.is_motor_enabled
*Type:* FUNCTION
Get whether the joint motor is enabled.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or wheel joint

**Returns**

- `enabled` (boolean) - true if the motor is enabled

### b2d.joint.is_motor_enabled
*Type:* FUNCTION
Get whether the joint motor is enabled.

**Parameters**

- `joint` (b2Joint) - distance, prismatic, revolute, or wheel joint

**Returns**

- `enabled` (boolean) - true if the motor is enabled

### b2d.joint.is_spring_enabled
*Type:* FUNCTION
Get whether joint spring behavior is enabled.

**Parameters**

- `joint` (b2Joint) - distance, prismatic, revolute, or wheel joint

**Returns**

- `enabled` (boolean) - true if the spring is enabled

### b2d.joint.is_valid
*Type:* FUNCTION
Validate a joint handle.

**Parameters**

- `joint` (b2Joint) - joint

**Returns**

- `valid` (boolean) - true if the joint handle still refers to a live Box2D joint

### b2d.joint.JOINT_TYPE_DISTANCE
*Type:* CONSTANT
Distance joint type.

### b2d.joint.JOINT_TYPE_DISTANCE
*Type:* CONSTANT
Distance joint type.

### b2d.joint.JOINT_TYPE_FILTER
*Type:* CONSTANT
Filter joint type.

### b2d.joint.JOINT_TYPE_FRICTION
*Type:* CONSTANT
Friction joint type.

### b2d.joint.JOINT_TYPE_GEAR
*Type:* CONSTANT
Gear joint type.

### b2d.joint.JOINT_TYPE_MOTOR
*Type:* CONSTANT
Motor joint type.

### b2d.joint.JOINT_TYPE_MOUSE
*Type:* CONSTANT
Mouse joint type.

### b2d.joint.JOINT_TYPE_MOUSE
*Type:* CONSTANT
Mouse joint type.

### b2d.joint.JOINT_TYPE_PRISMATIC
*Type:* CONSTANT
Prismatic joint type.

### b2d.joint.JOINT_TYPE_PRISMATIC
*Type:* CONSTANT
Prismatic joint type.

### b2d.joint.JOINT_TYPE_PULLEY
*Type:* CONSTANT
Pulley joint type.

### b2d.joint.JOINT_TYPE_REVOLUTE
*Type:* CONSTANT
Revolute joint type.

### b2d.joint.JOINT_TYPE_REVOLUTE
*Type:* CONSTANT
Revolute joint type.

### b2d.joint.JOINT_TYPE_ROPE
*Type:* CONSTANT
Rope joint type.

### b2d.joint.JOINT_TYPE_UNKNOWN
*Type:* CONSTANT
Unknown joint type.

### b2d.joint.JOINT_TYPE_WELD
*Type:* CONSTANT
Weld joint type.

### b2d.joint.JOINT_TYPE_WELD
*Type:* CONSTANT
Weld joint type.

### b2d.joint.JOINT_TYPE_WHEEL
*Type:* CONSTANT
Wheel joint type.

### b2d.joint.JOINT_TYPE_WHEEL
*Type:* CONSTANT
Wheel joint type.

### b2d.joint.LIMIT_STATE_AT_LOWER
*Type:* CONSTANT
At lower limit state.

### b2d.joint.LIMIT_STATE_AT_UPPER
*Type:* CONSTANT
At upper limit state.

### b2d.joint.LIMIT_STATE_EQUAL
*Type:* CONSTANT
Equal limits state.

### b2d.joint.LIMIT_STATE_INACTIVE
*Type:* CONSTANT
Inactive limit state.

### b2d.joint.set_angular_damping_ratio
*Type:* FUNCTION
Set weld joint angular damping ratio.

**Parameters**

- `joint` (b2Joint) - weld joint
- `ratio` (number) - damping ratio

### b2d.joint.set_angular_hertz
*Type:* FUNCTION
Set weld joint angular frequency.

**Parameters**

- `joint` (b2Joint) - weld joint
- `hertz` (number) - frequency in hertz

### b2d.joint.set_angular_offset
*Type:* FUNCTION
Set motor joint angular offset.

**Parameters**

- `joint` (b2Joint) - motor joint
- `offset` (number) - angular offset in radians

### b2d.joint.set_collide_connected
*Type:* FUNCTION
Set whether connected bodies can collide.

**Parameters**

- `joint` (b2Joint) - joint
- `collide` (boolean) - true if connected bodies can collide

### b2d.joint.set_correction_factor
*Type:* FUNCTION
Set motor joint correction factor.

**Parameters**

- `joint` (b2Joint) - motor joint
- `factor` (number) - correction factor

### b2d.joint.set_damping_ratio
*Type:* FUNCTION
Set spring damping ratio.

**Parameters**

- `joint` (b2Joint) - distance, mouse, weld, or wheel joint
- `ratio` (number) - damping ratio

### b2d.joint.set_damping_ratio
*Type:* FUNCTION
Alias for b2d.joint.set_spring_damping_ratio.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint
- `ratio` (number) - damping ratio

### b2d.joint.set_frequency
*Type:* FUNCTION
Set spring frequency.

**Parameters**

- `joint` (b2Joint) - distance, mouse, weld, or wheel joint
- `frequency` (number) - frequency in hertz

### b2d.joint.set_frequency
*Type:* FUNCTION
Alias for b2d.joint.set_spring_hertz.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint
- `frequency` (number) - frequency in hertz

### b2d.joint.set_hertz
*Type:* FUNCTION
Alias for b2d.joint.set_frequency.

**Parameters**

- `joint` (b2Joint) - distance, mouse, weld, or wheel joint
- `hertz` (number) - frequency in hertz

### b2d.joint.set_hertz
*Type:* FUNCTION
Alias for b2d.joint.set_spring_hertz.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint
- `hertz` (number) - frequency in hertz

### b2d.joint.set_length
*Type:* FUNCTION
Set the distance joint length.

**Parameters**

- `joint` (b2Joint) - distance joint
- `length` (number) - length in project units

### b2d.joint.set_length
*Type:* FUNCTION
Set the distance joint length.

**Parameters**

- `joint` (b2Joint) - distance joint
- `length` (number) - length in project units

### b2d.joint.set_length_range
*Type:* FUNCTION
Set the distance joint length range.

**Parameters**

- `joint` (b2Joint) - distance joint
- `min_length` (number) - minimum length in project units
- `max_length` (number) - maximum length in project units

### b2d.joint.set_limits
*Type:* FUNCTION
Set joint limits.

**Parameters**

- `joint` (b2Joint) - prismatic or revolute joint
- `lower` (number) - lower limit
- `upper` (number) - upper limit

### b2d.joint.set_limits
*Type:* FUNCTION
Set joint limits.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or wheel joint
- `lower` (number) - lower limit
- `upper` (number) - upper limit

### b2d.joint.set_linear_damping_ratio
*Type:* FUNCTION
Set weld joint linear damping ratio.

**Parameters**

- `joint` (b2Joint) - weld joint
- `ratio` (number) - damping ratio

### b2d.joint.set_linear_hertz
*Type:* FUNCTION
Set weld joint linear frequency.

**Parameters**

- `joint` (b2Joint) - weld joint
- `hertz` (number) - frequency in hertz

### b2d.joint.set_linear_offset
*Type:* FUNCTION
Set motor joint linear offset.

**Parameters**

- `joint` (b2Joint) - motor joint
- `offset` (vector3) - linear offset in project units

### b2d.joint.set_max_force
*Type:* FUNCTION
Set maximum force.

**Parameters**

- `joint` (b2Joint) - mouse or friction joint
- `force` (number) - maximum force

### b2d.joint.set_max_force
*Type:* FUNCTION
Set maximum force.

**Parameters**

- `joint` (b2Joint) - mouse or motor joint
- `force` (number) - maximum force

### b2d.joint.set_max_length
*Type:* FUNCTION
Set rope maximum length.

**Parameters**

- `joint` (b2Joint) - rope joint
- `length` (number) - maximum length in project units

### b2d.joint.set_max_length
*Type:* FUNCTION
Set the distance joint maximum length.

**Parameters**

- `joint` (b2Joint) - distance joint
- `length` (number) - maximum length in project units

### b2d.joint.set_max_motor_force
*Type:* FUNCTION
Set maximum motor force.

**Parameters**

- `joint` (b2Joint) - prismatic joint
- `force` (number) - maximum motor force

### b2d.joint.set_max_motor_force
*Type:* FUNCTION
Set maximum motor force.

**Parameters**

- `joint` (b2Joint) - distance or prismatic joint
- `force` (number) - maximum motor force

### b2d.joint.set_max_motor_torque
*Type:* FUNCTION
Set maximum motor torque.

**Parameters**

- `joint` (b2Joint) - revolute or wheel joint
- `torque` (number) - maximum motor torque

### b2d.joint.set_max_motor_torque
*Type:* FUNCTION
Set maximum motor torque.

**Parameters**

- `joint` (b2Joint) - revolute or wheel joint
- `torque` (number) - maximum motor torque

### b2d.joint.set_max_torque
*Type:* FUNCTION
Set maximum torque.

**Parameters**

- `joint` (b2Joint) - friction joint
- `torque` (number) - maximum torque

### b2d.joint.set_max_torque
*Type:* FUNCTION
Set maximum torque.

**Parameters**

- `joint` (b2Joint) - motor joint
- `torque` (number) - maximum torque

### b2d.joint.set_min_length
*Type:* FUNCTION
Set the distance joint minimum length.

**Parameters**

- `joint` (b2Joint) - distance joint
- `length` (number) - minimum length in project units

### b2d.joint.set_motor_speed
*Type:* FUNCTION
Set motor speed.

**Parameters**

- `joint` (b2Joint) - prismatic, revolute, or wheel joint
- `speed` (number) - motor speed

### b2d.joint.set_motor_speed
*Type:* FUNCTION
Set motor speed.

**Parameters**

- `joint` (b2Joint) - distance, prismatic, revolute, or wheel joint
- `speed` (number) - motor speed

### b2d.joint.set_mouse_target
*Type:* FUNCTION
Set the target for a mouse joint.

**Parameters**

- `joint` (b2Joint) - mouse joint
- `target` (vector3) - world target

### b2d.joint.set_mouse_target
*Type:* FUNCTION
Set the target for a mouse joint.

**Parameters**

- `joint` (b2Joint) - mouse joint
- `target` (vector3) - world target

### b2d.joint.set_ratio
*Type:* FUNCTION
Set gear joint ratio.

**Parameters**

- `joint` (b2Joint) - gear joint
- `ratio` (number) - gear ratio

### b2d.joint.set_reference_angle
*Type:* FUNCTION
Set weld joint reference angle.

**Parameters**

- `joint` (b2Joint) - weld joint
- `angle` (number) - reference angle in radians

### b2d.joint.set_spring_damping_ratio
*Type:* FUNCTION
Alias for b2d.joint.set_damping_ratio.

**Parameters**

- `joint` (b2Joint) - distance, mouse, weld, or wheel joint
- `ratio` (number) - damping ratio

### b2d.joint.set_spring_damping_ratio
*Type:* FUNCTION
Set spring damping ratio.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint
- `ratio` (number) - damping ratio

### b2d.joint.set_spring_hertz
*Type:* FUNCTION
Set spring frequency.

**Parameters**

- `joint` (b2Joint) - distance, mouse, prismatic, revolute, or wheel joint
- `hertz` (number) - frequency in hertz

### b2d.joint.wake_bodies
*Type:* FUNCTION
Wake the bodies connected to a joint.

**Parameters**

- `joint` (b2Joint) - joint

### b2Joint
*Type:* TYPEDEF
Box2D joint

**Parameters**

- `value` (userdata)

### b2Joint
*Type:* TYPEDEF
Box2D joint

**Parameters**

- `value` (userdata)
