# extension-siwa

**Namespace:** `siwa`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting Sign in with Apple. [icon:ios]

## API

### siwa.is_supported
*Type:* FUNCTION
Check if Sign in with Apple is available (iOS 13+).

### siwa.get_credential_state
*Type:* FUNCTION
Get the credential state of a user.

**Parameters**

- `user_id` (string) - User id to get credential state for.
- `callback` (function) - Credential state callback function.
  - `self` (object) - The current object.
  - `state` (table) - The credential state (user_id, credential_state)

**Examples**

```
siwa.get_credential_state(id, function(self, data)
    if data.credential_state == siwa.STATE_AUTHORIZED then
        print("User has still authorized the application", data.user_id)
    elseif data.credential_state == siwa.STATE_REVOKED then
        print("User has revoked authorization for the application", data.user_id)
    end
end)

```

### siwa.authenticate
*Type:* FUNCTION
Show the Sign in with Apple UI

**Parameters**

- `callback` (function) - Authentication callback function.
  - `self` (object) - The current object.
  - `state` (table) - The authentication result data (user_id, identity_token, email, first_name, family_name, status, result)

**Examples**

```
siwa.authenticate(function(self, data)
    print(data.identity_token)
    print(data.user_id)
    print(data.first_name, data.family_name)
    print(data.email)
    if data.user_status == siwa.STATUS_LIKELY_REAL then
        print("Likely a real person")
    end
end)

```

### STATE_NOT_FOUND
*Type:* VARIABLE
The user can’t be found.

### STATE_UNKNOWN
*Type:* VARIABLE
Unknown credential state.

### STATE_AUTHORIZED
*Type:* VARIABLE
The user is authorized.

### STATE_REVOKED
*Type:* VARIABLE
Authorization for the given user has been revoked.

### STATUS_UNKNOWN
*Type:* VARIABLE
The system hasn’t determined whether the user might be a real person.

### STATUS_UNSUPPORTED
*Type:* VARIABLE
The system can’t determine this user’s status as a real person.

### STATUS_LIKELY_REAL
*Type:* VARIABLE
The user appears to be a real person.
