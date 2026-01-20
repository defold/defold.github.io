# extension-zendesk

**Namespace:** `zendesk`
**Language:** Lua
**Type:** Extension

Defold native extension to interact with the Zendesk SDK.

## API

### zendesk.initialize
*Type:* FUNCTION
Initialize the Zendesk SDK

### zendesk.set_callback
*Type:* FUNCTION
Set a callback for events from the Zendesk SDK

### zendesk.show_messaging
*Type:* FUNCTION
Show the conversation screen.

### zendesk.set_conversation_fields
*Type:* FUNCTION
Set conversation fields in the SDK to add contextual data about the conversation.

### zendesk.clear_conversation_fields
*Type:* FUNCTION
Clear conversation fields from the SDK storage when the client side context changes.

### zendesk.set_conversation_tags
*Type:* FUNCTION
Set custom conversation tags in the SDK to add contextual data about the conversation.

### zendesk.clear_conversation_tags
*Type:* FUNCTION
Clear conversation tags from SDK storage when the client side context changes.

### zendesk.login
*Type:* FUNCTION
Authenticate a user.

### zendesk.logout
*Type:* FUNCTION
Unauthenticate a user.

### MSG_INIT_ERROR
*Type:* VARIABLE
An error was detected while initializing the Zendesk SDK

### MSG_INIT_SUCCESS
*Type:* VARIABLE
The Zendesk SDK has been initialized successfully

### MSG_INTERNAL_ERROR
*Type:* VARIABLE
An internal error occured

### MSG_ERROR
*Type:* VARIABLE
An generic error occured

### MSG_UNREAD_MESSAGE_COUNT_CHANGED
*Type:* VARIABLE
The number of unread messages has changed

### MSG_AUTHENTICATION_FAILED
*Type:* VARIABLE
A REST call failed for authentication reasons

### MSG_FIELD_VALIDATION_FAILED
*Type:* VARIABLE
Validation checks failed for conversation fields

### MSG_LOGIN_SUCCESS
*Type:* VARIABLE
Login was successful

### MSG_LOGIN_FAILED
*Type:* VARIABLE
Login failed

### MSG_LOGOUT_SUCCESS
*Type:* VARIABLE
Logout was successful

### MSG_LOGOUT_FAILED
*Type:* VARIABLE
Logout failed
