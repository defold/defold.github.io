# Cubemap Reflection

Shows how to sample a cubemap in a model shader to create environment reflections.

[Project files](https://github.com/defold/examples/tree/master/model/cubemap)

The example renders the Defold logo with a custom material that reflects an environment cubemap. Drag or touch to orbit around the model and use the mouse wheel to zoom.

## What You'll Learn

- How to bind a cubemap texture to a model material sampler
- How to compute world-space reflection vectors for environment mapping

## Setup

The collection contains a `logo` game object with an embedded Model component using `/example/assets/defold_logo.gltf`. Its material is `/example/cubemap_model.material`, and the material's `env_map` sampler is bound to `/example/assets/env.cubemap`.

The `camera` game object contains a perspective Camera component and `orbit_camera.script`. The script is used only to move the camera around the logo from pointer and mouse wheel input.

There is also an `info` game object with a GUI with a text to display controls on screen.

## How It Works

`cubemap_model.vp` receives the model position, normal, and per-instance `mtx_world` attribute. It transforms the normal into world space, derives the camera world position from the view matrix, and calculates a reflection vector for each vertex.

`cubemap_model.fp` samples the cubemap with that reflection vector. A small Fresnel term makes the logo edges more reflective, which makes the environment reflection easier to see while keeping the shader focused on cubemap sampling.

## Scripts

### cubemap_model.vp

```glsl
#version 140

// Model components provide local vertex data. The material uses
// `VERTEX_SPACE_LOCAL`, so the shader must transform positions itself.
in vec4 position;
in vec3 normal;

// Defold automatically provides `mtx_world` as a per-instance attribute for
// model materials in local vertex space. It is not listed as a material uniform.
in mat4 mtx_world;

// `mtx_view` and `mtx_proj` are vertex constants declared in `cubemap_model.material`.
uniform general_vp
{
	mat4 mtx_view;
	mat4 mtx_proj;
};

// The fragment shader samples the cubemap with this reflected world direction.
out vec3 var_reflection;

// The Fresnel value is used only to make grazing angles slightly brighter.
out float var_fresnel;

// Build a world-space normal matrix from `mtx_world`.
// This is equivalent to transpose(inverse(mat3(mtx_world))) after normalize(),
// but avoids a full matrix inverse in the shader.
mat3 adjoint(mat4 m)
{
	return mat3(
		cross(m[1].xyz, m[2].xyz),
		cross(m[2].xyz, m[0].xyz),
		cross(m[0].xyz, m[1].xyz)
	);
}

// The cubemap reflection vector needs the camera position in world space.
// Defold gives us the view matrix, so this converts it back to camera origin.
vec3 camera_position_from_view(mat4 view)
{
	return -(transpose(mat3(view)) * view[3].xyz);
}

void main()
{
	// Move the vertex from model space to world space before projecting it.
	vec4 world_position = mtx_world * vec4(position.xyz, 1.0);

	// Transform the model normal into world space so it matches the cubemap.
	vec3 world_normal = normalize(adjoint(mtx_world) * normal);

	// Create the incident view direction used by GLSL `reflect()`.
	vec3 camera_position = camera_position_from_view(mtx_view);
	vec3 camera_to_vertex = normalize(world_position.xyz - camera_position);

	// Reflect the view direction around the surface normal.
	// The result points into the cubemap and is interpolated across the model surface.
	var_reflection = reflect(camera_to_vertex, world_normal);
	var_fresnel = pow(1.0 - max(dot(-camera_to_vertex, world_normal), 0.0), 4.0);

	// Finish the model transform: world -> view -> projection.
	gl_Position = mtx_proj * mtx_view * world_position;
}
```

### cubemap_model.fp

```glsl
#version 140

// These values are calculated per vertex in `cubemap_model.vp` and
// interpolated for each fragment.
in vec3 var_reflection;
in float var_fresnel;

// Output fragment color
out vec4 out_frag_color;

// Environment map
// This sampler name must match the sampler in `cubemap_model.material` and
// the texture binding in the Model component.
uniform samplerCube env_map;

void main()
{
	// Normalize after interpolation, then sample the cubemap in that direction.
	vec3 reflected_color = texture(env_map, normalize(var_reflection)).rgb;

	// You can add a small base color so the logo still has shape in darker cubemap areas.
	vec3 base_color = vec3(0.06, 0.08, 0.1);

	// Fresnel makes shallow viewing angles more reflective, which helps show
	// that the cubemap is responding to the model's surface direction.
	float reflection_strength = mix(0.72, 1.0, var_fresnel);
	vec3 color = mix(base_color, reflected_color, reflection_strength);

	out_frag_color = vec4(color, 1.0);
}
```

### orbit_camera.script

```lua
local TOUCH = hash("touch")
local MOUSE_WHEEL_UP = hash("mouse_wheel_up")
local MOUSE_WHEEL_DOWN = hash("mouse_wheel_down")

local ROTATION_SPEED = 0.8
local ZOOM_STEP = 0.35
local MIN_PITCH = -75
local MAX_PITCH = 75
local MIN_ZOOM = 3.0
local MAX_ZOOM = 8.0
local SMOOTHING = 0.15

local function clamp(value, min_value, max_value)
	return math.max(min_value, math.min(max_value, value))
end

local function apply_camera(self)
	local yaw = vmath.quat_rotation_y(math.rad(self.current_yaw)) -- <1>
	local pitch = vmath.quat_rotation_x(math.rad(self.current_pitch)) -- <2>
	local rotation = yaw * pitch -- <3>
	local position = vmath.rotate(rotation, vmath.vector3(0, 0, self.current_zoom)) -- <4>

	go.set_position(position) -- <5>
	go.set_rotation(rotation) -- <6>
end

function init(self)
	msg.post(".", "acquire_input_focus") -- <7>

	self.target_yaw = 0
	self.target_pitch = 0
	self.target_zoom = 5.0
	self.current_yaw = self.target_yaw
	self.current_pitch = self.target_pitch
	self.current_zoom = self.target_zoom

	apply_camera(self)
end

function update(self, dt)
	self.current_yaw = vmath.lerp(SMOOTHING, self.current_yaw, self.target_yaw) -- <8>
	self.current_pitch = vmath.lerp(SMOOTHING, self.current_pitch, self.target_pitch)
	self.current_zoom = vmath.lerp(SMOOTHING, self.current_zoom, self.target_zoom)

	apply_camera(self)
end

function on_input(self, action_id, action)
	if action_id == TOUCH and not action.pressed and not action.released then -- <9>
		self.target_yaw = self.target_yaw - action.dx * ROTATION_SPEED -- <10>
		self.target_pitch = clamp(self.target_pitch + action.dy * ROTATION_SPEED, MIN_PITCH, MAX_PITCH) -- <11>
	elseif action_id == MOUSE_WHEEL_UP then
		self.target_zoom = clamp(self.target_zoom - ZOOM_STEP, MIN_ZOOM, MAX_ZOOM) -- <12>
	elseif action_id == MOUSE_WHEEL_DOWN then
		self.target_zoom = clamp(self.target_zoom + ZOOM_STEP, MIN_ZOOM, MAX_ZOOM) -- <13>
	end
end

--[[
1. Create the horizontal orbit rotation from the smoothed yaw angle.
2. Create the vertical orbit rotation from the smoothed pitch angle.
3. Combine yaw and pitch into the camera rotation.
4. Rotate a forward offset to place the camera on an orbit around the logo.
5. Move the camera game object to the calculated orbit position.
6. Rotate the camera so it keeps looking at the logo.
7. Acquire input focus so drag and mouse wheel input reaches this script.
8. Smoothly blend the visible camera values toward the latest input targets.
9. Handle pointer movement after the initial press and before release.
10. Drag left and right to orbit around the vertical axis.
11. Drag up and down to pitch the camera, clamped so it cannot flip over.
12. Scroll up to zoom in, clamped to the closest useful distance.
13. Scroll down to zoom out, clamped so the logo remains visible.
]]
```
