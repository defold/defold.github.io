# Dynamic factories

This example shows how to change the prototype game object used by a factory component.

[Project files](https://github.com/defold/examples/tree/master/factory/dynamic)

This example shows how to change the prototype game object used by a factory component. All prototype bullets are stored in a collection and referenced as a collection proxy. The collection proxy is never loaded, but it will ensure that the bullet prototypes are included in the build even though they are not immediately used by a factory. Another alternative is to load bullet prototypes using Live Update.

ship
: The red ship at the bottom. Contains:
  - A *Sprite* component with the spaceship image.
  - A *Factory* component to spawn bullet game objects. This component has the *Dynamic Protoype* option checked.
  - A *Collection Proxy* component referencing a collection containing all bullet types
  - A *Script* component to handle spawning of bullets.

All bullets are added in the bullets.collection:

The bullets.collection is referenced from the dynamic.collection as a collection proxy:

## Scripts

### dynamic.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus")

	-- a list of different bullet prototypes
	self.bullets = {
		"/example/flame.goc",
		"/example/lightning.goc",
		"/example/rock.goc",
	}
	-- the currently used bullet prototype
	self.bullet_index = 1

	-- shoot one bullet per second
	-- animate the bullet up 1000 pixels and then delete it
	timer.delay(0.2, true, function()
		local id = factory.create("#bulletfactory")
		local to = go.get_position(id)
		to.y = to.y + 1000
		go.animate(id, "position", go.PLAYBACK_ONCE_FORWARD, to, go.EASING_LINEAR, 1.5, 0, function()
			go.delete(id)
		end)
	end)
end

function on_input(self, action_id, action)
	-- mouse or spacebar
	if (action_id == hash("touch") or action_id == hash("key_space")) and action.pressed then
		-- next bullet prototype, wrap around to the first
		self.bullet_index = self.bullet_index + 1
		if self.bullet_index > #self.bullets then
			self.bullet_index = 1
		end

		-- unload current prototype
		factory.unload("#bulletfactory")

		-- set a new prototype
		local prototype = self.bullets[self.bullet_index]
		factory.set_prototype("#bulletfactory", prototype)
	end
end
```
