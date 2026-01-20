# Pointer over

A GUI box node with an image texture and a script that react when pointer over this node.

[Project files](https://github.com/defold/examples/tree/master/gui/pointer_over)

The "gui" game object contains a GUI component stored in the file *pointer_over.gui*. The GUI contains
the setup with the "button" box node for the button image and the "text" text node for the button label text.

*pointer_over.gui* has a script attached to it, called *pointer_over.gui_script*, which contains the button logic.

## Scripts

### pointer_over.gui_script

```lua
function init(self)
  msg.post(".", "acquire_input_focus") -- <1>
  self.button = gui.get_node("button") -- <2>
  self.text = gui.get_node("text") -- <3>
  self.is_over = false -- <4>
end

function on_input(self, action_id, action)
  if action_id == nil then --<5>
    if gui.pick_node(self.button, action.x, action.y) then -- <6>
      if not self.is_over then
        gui.set_text(self.text, "HELLO!") -- <7>
        self.is_over = true
      end
    else
      if self.is_over then
        gui.set_text(self.text, "BUTTON") -- <8>
        self.is_over = false
      end
    end
  end
end

--[[
1. Tell the engine that this game object wants to receive input.
2. Get the instance for the node named "button" (the button box).
3. Get the instance for the node named "text" (the button label).
4. Trigger for locking multiple execution.
5. If action_id equal nil (pointer is moving)
6. Check if the pointer position (`action.x` and `action.y`) is within the boundaries of
   the button node.
7. Change the label text in pointer over case.
8. Change the label text to default value.
--]]
```
