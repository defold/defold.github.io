# Hid

**Namespace:** `dmHid`
**Language:** C++
**Type:** Defold C++
**File:** `hid.h`
**Source:** `engine/hid/src/dmsdk/hid/hid.h`
**Include:** `dmsdk/hid/hid.h`

Used to add input to the engine

## API

### AddKeyboardChar
*Type:* FUNCTION
Add text input

**Parameters**

- `keyboard` (dmHID::HContext) - context handle
- `chr` (int) - The character (unicode)

### AddTouch
*Type:* FUNCTION
Adds a touch event touch.

**Parameters**

- `device` (dmHID::HTouchDevice) - device handle
- `x` (int32_t) - x-coordinate of the position
- `y` (int32_t) - y-coordinate of the position
- `id` (uint32_t) - identifier of touch
- `phase` (dmHID::Phase) - phase of touch

### dmHID::HContext
*Type:* TYPEDEF
HID context handle

### dmHID::HGamepad
*Type:* TYPEDEF
gamepad context handle

### dmHID::HKeyboard
*Type:* TYPEDEF
keyboard context handle

### dmHID::HMouse
*Type:* TYPEDEF
mouse context handle

### dmHID::HTouchDevice
*Type:* TYPEDEF
touch device context handle

### dmHID::INVALID_GAMEPAD_HANDLE [type: dmHID::HGamepad]
*Type:* CONSTANT
invalid gamepad handle

### dmHID::INVALID_KEYBOARD_HANDLE [type: dmHID::HKeyboard]
*Type:* CONSTANT
invalid keyboard handle

### dmHID::INVALID_MOUSE_HANDLE [type: dmHID::HMouse]
*Type:* CONSTANT
invalid mouse handle

### dmHID::INVALID_TOUCHDEVICE_HANDLE [type: dmHID::HTouchDevice]
*Type:* CONSTANT
invalid touch devicehandle

### dmHID::MAX_CHAR_COUNT
*Type:* CONSTANT
max number of characters

### dmHID::MAX_GAMEPAD_AXIS_COUNT [type: uint32_t]
*Type:* CONSTANT
Maximum number of gamepad axis supported

### dmHID::MAX_GAMEPAD_BUTTON_COUNT [type: uint32_t]
*Type:* CONSTANT
Maximum number of gamepad buttons supported

### dmHID::MAX_GAMEPAD_COUNT [type: uint32_t]
*Type:* CONSTANT
Maximum number of gamepads supported

### dmHID::MAX_GAMEPAD_HAT_COUNT [type: uint32_t]
*Type:* CONSTANT
Maximum number of gamepad hats supported

### dmHID::MAX_KEYBOARD_COUNT [type: uint32_t]
*Type:* CONSTANT
Maximum number of keyboards supported

### dmHID::MAX_MOUSE_COUNT [type: uint32_t]
*Type:* CONSTANT
Maximum number of mice supported

### dmHID::MAX_TOUCH_COUNT [type: uint32_t]
*Type:* CONSTANT
Maximum number of simultaneous touches supported

### dmHID::MAX_TOUCH_DEVICE_COUNT [type: uint32_t]
*Type:* CONSTANT
Maximum number of touch devices supported

### GamepadPacket
*Type:* STRUCT
Contains the current state of a gamepad

**Notes**

- implementation is internal, use the proper accessor functions

### GetGamePad
*Type:* FUNCTION
gets a gamepad device handle

**Parameters**

- `context` (dmHID::HContext) - context in which to find the gamepad
- `index` (uint8_t) - device index

**Returns**

- `gamepad` (dmHID::HGamepad) - Handle to gamepad. dmHID::INVALID_GAMEPAD_HANDLE if not available

### GetGamePad
*Type:* FUNCTION
gets a gamepad device handle

**Parameters**

- `gamepad` (dmHID::HGamepad) - Handle to gamepad
- `out` (void**) - Platform specific user id data

**Returns**

- `result` (boolean) - true if gamepad has a user id data assigned to it

### GetGamepadButton
*Type:* FUNCTION
Convenience function to retrieve the state of a gamepad button from a gamepad packet.

**Parameters**

- `packet` (dmHID::GamepadPacket) - Gamepad packet
- `button` (uint32_t) - The requested button

**Returns**

- `success` (bool) - True if the button is currently pressed down.

### GetGamepadHat
*Type:* FUNCTION
Convenience function to retrieve the state of a gamepad hat from a gamepad packet.

**Parameters**

- `packet` (dmHID::GamepadPacket) - Gamepad packet
- `hat` (uint32_t) - The requested hat index
- `out_hat_value` (uint8_t) - Hat value out argument

**Returns**

- `success` (bool) - True if the hat has data.

### GetGamepadPacket
*Type:* FUNCTION
Obtain a gamepad packet reflecting the current input state of the gamepad in a  HID context.

**Parameters**

- `gamepad` (dmHID::HGamepad) - gamepad handle
- `out_packet` (dmHID::GamepadPacket) - Gamepad packet out argument

**Returns**

- `success` (bool) - True if the packet was successfully updated.

### GetKeyboard
*Type:* FUNCTION
gets a keyboard handle

**Parameters**

- `context` (dmHID::HContext) - context in which to find the gamepad
- `index` (uint8_t) - device index

**Returns**

- `keyboard` (dmHID::HKeyboard) - Handle to keyboard. dmHID::INVALID_KEYBOARD_HANDLE if not available

### GetMouse
*Type:* FUNCTION
gets a mouse handle

**Parameters**

- `context` (dmHID::HContext) - context in which to find the gamepad
- `index` (uint8_t) - device index

**Returns**

- `mouse` (dmHID::HMouse) - Handle to mouse. dmHID::INVALID_MOUSE_HANDLE if not available

### GetMouseButton
*Type:* FUNCTION
Convenience function to retrieve the state of a mouse button from a mouse packet.

**Parameters**

- `packet` (dmHID::MousePacket*) - Mouse packet
- `button` (dmHID::MouseButton) - The requested button

**Returns**

- `result` (bool) - If the button was pressed or not

### GetMousePacket
*Type:* FUNCTION
Obtain a mouse packet reflecting the current input state of a HID context.

**Parameters**

- `mouse` (dmHID::HMouse) - context from which to retrieve the packet
- `out_packet` (dmHID::MousePacket*) - Mouse packet out argument

**Returns**

- `result` (bool) - If the packet was successfully updated or not.

### GetTouchDevice
*Type:* FUNCTION
gets a touch device handle

**Parameters**

- `context` (dmHID::HContext) - context in which to find the gamepad
- `index` (uint8_t) - device index

**Returns**

- `device` (dmHID::HTouchDevice) - Handle to touch device. dmHID::INVALID_TOUCH_DEVICE_HANDLE if not available

### Key
*Type:* ENUM
keyboard key enumeration

**Members**

- `dmHID::KEY_SPACE`
- `dmHID::KEY_EXCLAIM`
- `dmHID::KEY_QUOTEDBL`
- `dmHID::KEY_HASH`
- `dmHID::KEY_DOLLAR`
- `dmHID::KEY_AMPERSAND`
- `dmHID::KEY_QUOTE`
- `dmHID::KEY_LPAREN`
- `dmHID::KEY_RPAREN`
- `dmHID::KEY_ASTERISK`
- `dmHID::KEY_PLUS`
- `dmHID::KEY_COMMA`
- `dmHID::KEY_MINUS`
- `dmHID::KEY_PERIOD`
- `dmHID::KEY_SLASH`
- `dmHID::KEY_0`
- `dmHID::KEY_1`
- `dmHID::KEY_2`
- `dmHID::KEY_3`
- `dmHID::KEY_4`
- `dmHID::KEY_5`
- `dmHID::KEY_6`
- `dmHID::KEY_7`
- `dmHID::KEY_8`
- `dmHID::KEY_9`
- `dmHID::KEY_COLON`
- `dmHID::KEY_SEMICOLON`
- `dmHID::KEY_LESS`
- `dmHID::KEY_EQUALS`
- `dmHID::KEY_GREATER`
- `dmHID::KEY_QUESTION`
- `dmHID::KEY_AT`
- `dmHID::KEY_A`
- `dmHID::KEY_B`
- `dmHID::KEY_C`
- `dmHID::KEY_D`
- `dmHID::KEY_E`
- `dmHID::KEY_F`
- `dmHID::KEY_G`
- `dmHID::KEY_H`
- `dmHID::KEY_I`
- `dmHID::KEY_J`
- `dmHID::KEY_K`
- `dmHID::KEY_L`
- `dmHID::KEY_M`
- `dmHID::KEY_N`
- `dmHID::KEY_O`
- `dmHID::KEY_P`
- `dmHID::KEY_Q`
- `dmHID::KEY_R`
- `dmHID::KEY_S`
- `dmHID::KEY_T`
- `dmHID::KEY_U`
- `dmHID::KEY_V`
- `dmHID::KEY_W`
- `dmHID::KEY_X`
- `dmHID::KEY_Y`
- `dmHID::KEY_Z`
- `dmHID::KEY_LBRACKET`
- `dmHID::KEY_BACKSLASH`
- `dmHID::KEY_RBRACKET`
- `dmHID::KEY_CARET`
- `dmHID::KEY_UNDERSCORE`
- `dmHID::KEY_BACKQUOTE`
- `dmHID::KEY_LBRACE`
- `dmHID::KEY_PIPE`
- `dmHID::KEY_RBRACE`
- `dmHID::KEY_TILDE`
- `dmHID::KEY_ESC`
- `dmHID::KEY_F1`
- `dmHID::KEY_F2`
- `dmHID::KEY_F3`
- `dmHID::KEY_F4`
- `dmHID::KEY_F5`
- `dmHID::KEY_F6`
- `dmHID::KEY_F7`
- `dmHID::KEY_F8`
- `dmHID::KEY_F9`
- `dmHID::KEY_F10`
- `dmHID::KEY_F11`
- `dmHID::KEY_F12`
- `dmHID::KEY_UP`
- `dmHID::KEY_DOWN`
- `dmHID::KEY_LEFT`
- `dmHID::KEY_RIGHT`
- `dmHID::KEY_LSHIFT`
- `dmHID::KEY_RSHIFT`
- `dmHID::KEY_LCTRL`
- `dmHID::KEY_RCTRL`
- `dmHID::KEY_LALT`
- `dmHID::KEY_RALT`
- `dmHID::KEY_TAB`
- `dmHID::KEY_ENTER`
- `dmHID::KEY_BACKSPACE`
- `dmHID::KEY_INSERT`
- `dmHID::KEY_DEL`
- `dmHID::KEY_PAGEUP`
- `dmHID::KEY_PAGEDOWN`
- `dmHID::KEY_HOME`
- `dmHID::KEY_END`
- `dmHID::KEY_KP_0`
- `dmHID::KEY_KP_1`
- `dmHID::KEY_KP_2`
- `dmHID::KEY_KP_3`
- `dmHID::KEY_KP_4`
- `dmHID::KEY_KP_5`
- `dmHID::KEY_KP_6`
- `dmHID::KEY_KP_7`
- `dmHID::KEY_KP_8`
- `dmHID::KEY_KP_9`
- `dmHID::KEY_KP_DIVIDE`
- `dmHID::KEY_KP_MULTIPLY`
- `dmHID::KEY_KP_SUBTRACT`
- `dmHID::KEY_KP_ADD`
- `dmHID::KEY_KP_DECIMAL`
- `dmHID::KEY_KP_EQUAL`
- `dmHID::KEY_KP_ENTER`
- `dmHID::KEY_KP_NUM_LOCK`
- `dmHID::KEY_CAPS_LOCK`
- `dmHID::KEY_SCROLL_LOCK`
- `dmHID::KEY_PAUSE`
- `dmHID::KEY_LSUPER`
- `dmHID::KEY_RSUPER`
- `dmHID::KEY_MENU`
- `dmHID::KEY_BACK`
- `dmHID::MAX_KEY_COUNT`

### KeyboardPacket
*Type:* STRUCT
Contains the current state of a keyboard

**Notes**

- implementation is internal, use the proper accessor functions

### MouseButton
*Type:* ENUM
mouse button enumeration

**Members**

- `dmHID::MOUSE_BUTTON_LEFT`
- `dmHID::MOUSE_BUTTON_MIDDLE`
- `dmHID::MOUSE_BUTTON_RIGHT`
- `dmHID::MOUSE_BUTTON_1`
- `dmHID::MOUSE_BUTTON_2`
- `dmHID::MOUSE_BUTTON_3`
- `dmHID::MOUSE_BUTTON_4`
- `dmHID::MOUSE_BUTTON_5`
- `dmHID::MOUSE_BUTTON_6`
- `dmHID::MOUSE_BUTTON_7`
- `dmHID::MOUSE_BUTTON_8`
- `dmHID::MAX_MOUSE_BUTTON_COUNT`

### MousePacket
*Type:* STRUCT
Contains the current state of a mouse

**Notes**

- implementation is internal, use the proper accessor functions

### Phase
*Type:* ENUM
touch phase enumeration

**Notes**

- By convention the enumeration corresponds to the iOS values

**Members**

- `dmHID::PHASE_BEGAN`
- `dmHID::PHASE_MOVED`
- `dmHID::PHASE_STATIONARY`
- `dmHID::PHASE_ENDED`
- `dmHID::PHASE_CANCELLED`

### SetGamepadAxis
*Type:* FUNCTION
Sets the state of a gamepad axis.

**Parameters**

- `gamepad` (dmHID::HGamepad) - device handle
- `axis` (uint32_t) - The requested axis [0, dmHID::MAX_GAMEPAD_AXIS_COUNT)
- `value` (float) - axis value [-1, 1]

### SetGamepadButton
*Type:* FUNCTION
Sets the state of a gamepad button.

**Parameters**

- `gamepad` (dmHID::HGamepad) - device handle
- `button` (uint32_t) - The requested button [0, dmHID::MAX_GAMEPAD_BUTTON_COUNT)
- `value` (bool) - Button state

### SetKey
*Type:* FUNCTION
Sets the state of a key.

**Parameters**

- `keyboard` (dmHID::HKeyboard) - context handle
- `key` (dmHID::Key) - The requested key
- `value` (bool) - Key state

### SetMouseButton
*Type:* FUNCTION
Sets the state of a mouse button.

**Parameters**

- `mouse` (dmHID::HMouse) - device handle
- `button` (dmHID::MouseButton) - The requested button
- `value` (bool) - Button state

### SetMousePosition
*Type:* FUNCTION
Sets the position of a mouse.

**Parameters**

- `mouse` (dmHID::HMouse) - device handle
- `x` (int32_t) - x-coordinate of the position
- `y` (int32_t) - y-coordinate of the position

### SetMouseWheel
*Type:* FUNCTION
Sets the mouse wheel.

**Parameters**

- `mouse` (dmHID::HMouse) - device handle
- `value` (int32_t) - wheel value

### Touch
*Type:* STRUCT
Data for a single touch, e.g. finger

**Members**

- `m_TapCount` (int32_t) - Single-click, double, etc
- `m_Phase` (Phase) - Begin, end, etc
- `m_X` (int32_t) - Current x
- `m_Y` (int32_t) - Current y
- `m_ScreenX` (int32_t) - Current x, in screen space
- `m_ScreenY` (int32_t) - Current y, in screen space
- `m_DX` (int32_t) - Current dx
- `m_DY` (int32_t) - Current dy
- `m_ScreenDX` (int32_t) - Current dx, in screen space
- `m_ScreenDY` (int32_t) - Current dy, in screen space
- `m_Id` (int32_t) - Touch id
