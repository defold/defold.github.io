# Cubemap Reflection

This example shows how to use a cubemap to draw environment reflections on a model.

[Project files](https://github.com/defold/examples/tree/master/model/cubemap)

This example contains a game object with a model component in the shape of the Defold logo. The model has a special `cubemap_model.material` which uses a cubemap sampler to calculate reflections on the model from the cubemap.

## Scripts

### cubemap.script

```lua
local ZOOM_SPEED = 0.1
local ROTATION_SPEED = 1

function init(self)
	msg.post("@render:", "use_camera_projection")
	msg.post(".", "acquire_input_focus")
	self.yaw            = 0   -- for camera rotation
	self.pitch          = 0   -- for camera rotation
	self.zoom           = 5   -- default zoom
	self.zoom_offset    = 0   -- modification from default zoom
end

function update(self, dt)
	local camera_yaw           = vmath.quat_rotation_y(math.rad(self.yaw))
	local camera_pitch         = vmath.quat_rotation_x(math.rad(self.pitch))
	local camera_rot           = camera_yaw * camera_pitch
	local camera_position      = vmath.rotate(camera_rot, vmath.vector3(0, 0, self.zoom + self.zoom_offset))
	go.set_position(camera_position)
	go.set_rotation(camera_rot)

	local cameraposv4 = vmath.vector4(camera_position.x, camera_position.y, camera_position.z, 1)
	go.set("logo#model", "cameraPosition", cameraposv4)
end

function on_input(self, action_id, action)
	if action_id == hash("touch") then
		self.yaw   = self.yaw   - action.dx * ROTATION_SPEED
		self.pitch = self.pitch + action.dy * ROTATION_SPEED
	elseif action_id == hash("mouse_wheel_up") then
		self.zoom_offset = self.zoom_offset - ZOOM_SPEED
	elseif action_id == hash("mouse_wheel_down") then
		self.zoom_offset = self.zoom_offset + ZOOM_SPEED
	end
end
```

### cubemap_model.fp

```glsl
#version 140

in mediump vec3 vReflect;
out vec4 out_FragColor;

uniform samplerCube envMap;

void main()
{
	out_FragColor = texture(envMap, vReflect);
}
```

### cubemap_model.vp

```glsl
#version 140

uniform vs_uniforms {
	mediump mat4 view_proj;
	mediump mat4 world;
	mediump mat4 normal_transform;
	mediump mat4 world_view;
	mediump vec4 cameraPosition;
};

in mediump vec3 position;
in mediump vec3 normal;
in mediump vec2 texcoord0;

out mediump vec3 vReflect;

void main()
{
	vec4 worldP = world * vec4(position, 1.0);
	gl_Position = view_proj * worldP;
	
	vec3 worldNormal = normalize(normal);
	vec3 cameraToVertex = normalize( worldP.xyz - cameraPosition.xyz );
	vReflect = reflect( cameraToVertex, worldNormal );
}
```
