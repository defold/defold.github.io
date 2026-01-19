# Android

**Namespace:** `dmAndroid`
**Language:** C++
**Type:** Defold C++
**File:** `android.h`
**Source:** `engine/dlib/src/dmsdk/dlib/android.h`
**Include:** `dmsdk/dlib/android.h`

Android utility functions

## API

### Detach
*Type:* FUNCTION
Detaches the jni environment

**Returns**

- `ok` (bool) - true if there was no java exceptions. False if there was an exception.

### GetActivity
*Type:* FUNCTION
Gets the app native activity

**Returns**

- `activity` (ANativeActivity*) - the app native activity

### GetEnv
*Type:* FUNCTION
Gets the JNI environment

**Returns**

- `env` (JNIENV*) - the attached environment

### IsAttached
*Type:* FUNCTION
Is the environment attached and valid?

**Returns**

- `isattached` (bool) - true if the environment is valid

**Examples**

```
Result SomeFunc() {
  ThreadAttacher thread;
  JNIEnv* env = thread.GetEnv();
  if (!env)
    return RESULT_ATTACH_FAILED;
  ... calls using jni
  return thread.Detach() ? RESULT_OK : RESULT_JNI_CALLS_FAILED;
}

```

### LoadClass
*Type:* FUNCTION
Load a class

**Parameters**

- `env` (JNIEnv*)
- `class_name` (const char*)

**Returns**

- `class` (jclass) - the activity class loader

### LoadClass
*Type:* FUNCTION
Load a class

**Parameters**

- `env` (JNIEnv*)
- `activity` (jobject)
- `class_name` (const char*)

**Returns**

- `class` (jclass) - the activity class loader

### OnActivityCreate
*Type:* TYPEDEF
onCreate callback function type.
Used with RegisterOnActivityCreateListener() and UnregisterOnActivityCreateListener()

**Parameters**

- `env` (JNIEnv*)
- `activity` (jobject)

### OnActivityResult
*Type:* TYPEDEF
Activity result callback function type. Monitors events from the main activity.
Used with RegisterOnActivityResultListener() and UnregisterOnActivityResultListener()

**Parameters**

- `env` (JNIEnv*)
- `activity` (jobject)
- `request_code` (int32_t)
- `result_code` (int32_t)
- `result` (void*)

### RegisterOnActivityCreateListener
*Type:* FUNCTION
Registers an onCreate callback. Multiple listeners are allowed.

**Notes**

- [icon:android] Only available on Android

**Parameters**

- `listener` (dmAndroid::OnActivityCreate)

### RegisterOnActivityResultListener
*Type:* FUNCTION
Registers an activity result callback. Multiple listeners are allowed.

**Notes**

- [icon:android] Only available on Android

**Parameters**

- `listener` (dmAndroid::OnActivityResult)

### ThreadAttacher
*Type:* CLASS
Struct attaching the JNI environment. Detaches the

### ThreadAttacher
*Type:* FUNCTION
constructor

**Examples**

```
{
  ThreadAttacher thread;
  SomeFunction( thread.GetEnv() );
  // Automatically detaches
}

```

```
{
  ThreadAttacher thread;
  JNIEnv* env = thread.GetEnv();
  if (!env)
    return;
  ...
}

```

### UnregisterOnActivityCreateListener
*Type:* FUNCTION
Unregisters an onCreate callback

**Notes**

- [icon:android] Only available on Android

**Parameters**

- `listener` (dmAndroid::OnActivityCreate)

### UnregisterOnActivityResultListener
*Type:* FUNCTION
Unregisters an activity result callback

**Notes**

- [icon:android] Only available on Android

**Parameters**

- `listener` (dmAndroid::OnActivityResult)
