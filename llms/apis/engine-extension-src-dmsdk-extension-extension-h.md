# Extension

**Namespace:** `Extension`
**Language:** C++
**Type:** Defold C++
**File:** `extension.h`
**Source:** `engine/extension/src/dmsdk/extension/extension.h`
**Include:** `dmsdk/extension/extension.h`

Functions for creating and controlling engine native extension libraries.

## API

### DM_DECLARE_EXTENSION
*Type:* MACRO
Declare and register new extension to the engine.
This macro is used to declare the extension callback functions used by the engine to communicate with the extension.

**Parameters**

- `symbol` (symbol) - external extension symbol description (no quotes).
- `name` (const char*) - extension name. Human readable.
- `app_init` (function(ExtensionAppParams* app_params)) - app-init function. May be null.
<dl>
<dt><code>app_params</code></dt>
<dd><span class="type">ExtensionAppParams*</span> Pointer to an <code>AppParams</code> structure.</dd>
</dl>
- `app_final` (function(ExtensionAppParams* app_params)) - app-final function. May be null.
<dl>
<dt><code>app_params</code></dt>
<dd><span class="type">ExtensionAppParams*</span> Pointer to an <code>AppParams</code> structure.</dd>
</dl>
- `init` (function(ExtensionParams* params)) - init function. May not be null.
<dl>
<dt><code>params</code></dt>
<dd><span class="type">ExtensionParams*</span> Pointer to a <code>Params</code> structure</dd>
</dl>
- `update` (function(ExtensionParams* params)) - update function. May be null.
<dl>
<dt><code>params</code></dt>
<dd><span class="type">ExtensionParams*</span> Pointer to a <code>Params</code> structure</dd>
</dl>
- `on_event` (function(ExtensionParams* params, const ExtensionEvent* event)) - event callback function. May be null.
<dl>
<dt><code>params</code></dt>
<dd><span class="type">ExtensionParams*</span> Pointer to a <code>Params</code> structure</dd>
<dt><code>event</code></dt>
<dd><span class="type">ExtensionEvent*</span> const Pointer to an <code>Event</code> structure</dd>
</dl>
- `final` (function(ExtensionParams* params)) - function. May not be null.
<dl>
<dt><code>params</code></dt>
<dd><span class="type">ExtensionParams*</span> Pointer to an <code>Params</code> structure.</dd>
</dl>

**Examples**

Register a new extension:
```
DM_DECLARE_EXTENSION(MyExt, "MyExt", AppInitializeMyExt, AppFinalizeMyExt, InitializeMyExt, UpdateMyExt, OnEventMyExt, FinalizeMyExt);

```

### DM_PLATFORM_ANDROID
*Type:* MACRO
Set if the platform is Android

### DM_PLATFORM_HTML5
*Type:* MACRO
Set if the platform is Html5

### DM_PLATFORM_IOS
*Type:* MACRO
Set if the platform is iPhoneOS

### DM_PLATFORM_LINUX
*Type:* MACRO
Set if the platform is Linux

### DM_PLATFORM_OSX
*Type:* MACRO
Set if the platform is OSX

### DM_PLATFORM_WINDOWS
*Type:* MACRO
Set if the platform is Windows  (on both x86 and x86_64)

### ExtensionAppExitCode
*Type:* ENUM
Engine exit code.

**Members**

- `EXTENSION_APP_EXIT_CODE_NONE`
- `EXTENSION_APP_EXIT_CODE_REBOOT`
- `EXTENSION_APP_EXIT_CODE_EXIT`

### ExtensionAppParams
*Type:* STRUCT
The extension app parameters

**Members**

- `m_ConfigFile` (HConfigFile) - Deprecated
- `m_ExitStatus` (ExtensionAppExitCode) - App exit code

### ExtensionAppParamsFinalize
*Type:* FUNCTION
Finalizes an extension app params struct (deallocates internal memory)

**Parameters**

- `app_params` (ExtensionAppParams*) - the params

### ExtensionAppParamsGetAppExitCode
*Type:* FUNCTION
get the app exit code

**Parameters**

- `app_params` (dmExtension::AppParams*) - The app params sent to the extension dmExtension::AppInitialize / dmExtension::AppInitialize

**Returns**

- `code` (ExtensionAppExitCode) - engine exit code

### ExtensionAppParamsGetContext
*Type:* FUNCTION
Gets a context using a specified name hash

**Parameters**

- `params` (ExtensionAppParams) - the params
- `name_hash` (dmhash_t) - the context name hash

**Returns**

- `context` (void*) - The context, if it exists

### ExtensionAppParamsGetContextByName
*Type:* FUNCTION
Gets a context using a specified name

**Parameters**

- `params` (ExtensionAppParams) - the params
- `name` (const char*) - the context name

**Returns**

- `context` (void*) - The context, if it exists

### ExtensionAppParamsInitialize
*Type:* FUNCTION
Initializes an extension app params struct
NOTE: this is an opaque struct, do not use it's members directly!

**Parameters**

- `app_params` (ExtensionAppParams*) - the params

### ExtensionAppParamsSetContext
*Type:* FUNCTION
Sets a context using a specified name

**Parameters**

- `params` (ExtensionAppParams) - the params
- `name` (const char*) - the context name
- `context` (void*) - the context

**Returns**

- `result` (int) - 0 if successful

### ExtensionCallbackType
*Type:* ENUM
Extra callback type for RegisterCallback function.

**Members**

- `EXTENSION_CALLBACK_PRE_RENDER`
- `EXTENSION_CALLBACK_POST_RENDER`

### ExtensionDescBufferSize
*Type:* CONSTANT
Used when registering new extensions

### ExtensionEvent
*Type:* STRUCT
Extension event

**Members**

- `m_Event` (ExtensionEventID)

### ExtensionEventID
*Type:* ENUM
Event id enumeration.
EVENT_ID_ICONIFYAPP and EVENT_ID_DEICONIFYAPP only available on

**Members**

- `EXTENSION_EVENT_ID_ACTIVATEAPP`
- `EXTENSION_EVENT_ID_DEACTIVATEAPP`
- `EXTENSION_EVENT_ID_ICONIFYAPP`
- `EXTENSION_EVENT_ID_DEICONIFYAPP`
- `EXTENSION_EVENT_ID_ENGINE_INITIALIZED`
- `EXTENSION_EVENT_ID_ENGINE_DELETE`

### ExtensionParams
*Type:* STRUCT
The global parameters avalable when registering and unregistering an extension

**Members**

- `m_ConfigFile` (HConfigFile) - The game project settings (including overrides and plugins)
- `m_ResourceFactory` (HResourceFactory) - The game resource factory / repository
- `m_L` (lua_State*) - The Lua state.

### ExtensionParamsFinalize
*Type:* FUNCTION
Finalizes an extension  params struct (deallocates internal memory)

**Parameters**

- `app_params` (ExtensionParams*) - the params

### ExtensionParamsGetContext
*Type:* FUNCTION
Gets a context using a specified name hash

**Parameters**

- `params` (ExtensionParams) - the params
- `name_hash` (dmhash_t) - the context name hash

**Returns**

- `context` (void*) - The context, if it exists

### ExtensionParamsGetContextByName
*Type:* FUNCTION
Gets a context using a specified name

**Parameters**

- `params` (ExtensionParams) - the params
- `name` (const char*) - the context name

**Returns**

- `context` (void*) - The context, if it exists

### ExtensionParamsInitialize
*Type:* FUNCTION
Initializes an extension params struct
NOTE: this is an opaque struct, do not use it's members directly!

**Parameters**

- `app_params` (ExtensionParams*) - the params

### ExtensionParamsSetContext
*Type:* FUNCTION
Sets a context using a specified name

**Parameters**

- `params` (ExtensionAppParams) - the params
- `name` (const char*) - the context name
- `context` (void*) - the context

**Returns**

- `result` (int) - 0 if successful

### ExtensionRegister
*Type:* FUNCTION
Extension declaration helper. Internal function. Use DM_DECLARE_EXTENSION

**Parameters**

- `desc` (void*) - A persistent buffer of at least 128 bytes.
- `desc_size` (const char*) - size of buffer holding desc. in bytes
- `name` (const char*) - extension name. human readble. max 16 characters long.
- `app_initialize` (FExtensionAppInitialize) - app-init function. May be null
- `app_finalize` (FExtensionAppFinalize) - app-final function. May be null
- `initialize` (FExtensionInitialize) - init function. May not be 0
- `finalize` (FExtensionFinalize) - finalize function. May not be 0
- `update` (FExtensionUpdate) - update function. May be null
- `on_event` (FExtensionOnEvent) - event callback function. May be null

### ExtensionRegisteriOSUIApplicationDelegate
*Type:* FUNCTION
Register an iOS application delegate to the engine. Multiple delegates are supported (Max 32)

**Notes**

- Note that the delegate needs to be registered before the UIApplicationMain in order to
handle any earlier callbacks.

This function is only available on iOS. [icon:ios]

**Parameters**

- `delegate` (void*) - An id<UIApplicationDelegate>, see: https://developer.apple.com/documentation/uikit/uiapplicationdelegate?language=objc

**Examples**

```
// myextension_ios.mm

id g_MyApplicationDelegate;

\@interface MyApplicationDelegate : NSObject

- (void) applicationDidBecomeActive:(UIApplication *) application;

\@end

\@implementation MyApplicationDelegate

- (void) applicationDidBecomeActive:(UIApplication *) application {
    dmLogWarning("applicationDidBecomeActive - MyAppDelegate");
}

\@end

struct MyAppDelegateRegister
{
    MyApplicationDelegate* m_Delegate;
    MyAppDelegateRegister() {
        m_Delegate = [[FacebookAppDelegate alloc] init];
        Extension::RegisteriOSUIApplicationDelegate(m_Delegate);
    }
    ~MyAppDelegateRegister() {
        Extension::UnregisteriOSUIApplicationDelegate(m_Delegate);
        [m_Delegate release];
    }
};

MyAppDelegateRegister g_FacebookDelegateRegister;

```

### ExtensionResult
*Type:* ENUM
Result enumeration.

**Members**

- `EXTENSION_RESULT_OK`
- `EXTENSION_RESULT_INIT_ERROR`

### ExtensionUnregisteriOSUIApplicationDelegate
*Type:* FUNCTION
Deregister a previously registered iOS application delegate
This function is only available on iOS.

**Parameters**

- `delegate` (void*) - an id<UIApplicationDelegate>

### FExtensionAppFinalize
*Type:* TYPEDEF
Callback when the app is being finalized

**Parameters**

- `params` (ExtensionAppParams)

**Returns**

- `result` (ExtensionResult) - EXTENSION_RESULT_OK if all went ok

### FExtensionAppInitialize
*Type:* TYPEDEF
Callback when the app is being initialized. Called before FExtensionInitialize

**Notes**

- There is no guarantuee of initialization order. If an extension requires another extension to be initialized,
      that should be handled in [ref:FExtensionInitialize].

**Parameters**

- `params` (ExtensionAppParams)

**Returns**

- `result` (ExtensionResult) - EXTENSION_RESULT_OK if all went ok

### FExtensionCallback
*Type:* TYPEDEF
Callback typedef for functions passed to RegisterCallback().

**Parameters**

- `params` (ExtensionParams)

**Returns**

- `return` (ExtensionResult)

### FExtensionFinalize
*Type:* TYPEDEF
Calls for the finalization of an extension

**Notes**

- All extensions will be called with `FExtensionFinalize` before moving on to the next step, the [ref:FExtensionAppFinalize]

**Parameters**

- `params` (ExtensionParams)

**Returns**

- `result` (ExtensionResult) - EXTENSION_RESULT_OK if all went ok

### FExtensionInitialize
*Type:* TYPEDEF
Callback after all extensions have been called with FExtensionAppInitialize

**Parameters**

- `params` (ExtensionParams)

**Returns**

- `result` (ExtensionResult) - EXTENSION_RESULT_OK if all went ok

### FExtensionOnEvent
*Type:* TYPEDEF
Receives an event from the engine

**Parameters**

- `params` (ExtensionParams)
- `event` (ExtensionEvent) - The current event

### FExtensionUpdate
*Type:* TYPEDEF
Updates an extension. Called for each game frame.

**Parameters**

- `params` (ExtensionParams)

**Returns**

- `result` (ExtensionResult) - EXTENSION_RESULT_OK if all went ok
