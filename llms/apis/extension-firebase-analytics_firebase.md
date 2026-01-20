# extension-firebase-analytics

**Namespace:** `firebase`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Firebase

## API

### firebase.analytics.initialize
*Type:* FUNCTION
Initialise analytics

### firebase.analytics.set_callback
*Type:* FUNCTION
Sets a callback function for receiving events from the SDK. Call `firebase.analytics.set_callback(nil)` to remove callback

**Parameters**

- `callback` (function) - Callback function that is executed on any event in the SDK.
  - `self` (object) - The calling script instance
  - `message_id` (number) - One of message types: `firebase.analytics.MSG_ERROR` `firebase.analytics.MSG_INSTANCE_ID`
  - `message` (table) - A table holding the data
    - `error` (string) - The error message (if an error occurred or `nil` otherwise)
    - `instance_id` (string) - For message_id MSG_INSTANCE_ID or `nil` otherwise.

### firebase.analytics.log
*Type:* FUNCTION
Log an event without parameters.

**Parameters**

- `name` (string) - Event name

### firebase.analytics.log_string
*Type:* FUNCTION
Log an event with one string parameter.

**Parameters**

- `name` (string) - Event name
- `PARAMeter_name` (string) - Parameter name
- `PARAMeter_value` (string) - Parameter value

### firebase.analytics.log_int
*Type:* FUNCTION
Log an event with one integer parameter.

**Parameters**

- `name` (string) - Event name
- `PARAMeter_name` (string) - Parameter name
- `PARAMeter_value` (number) - Parameter value

### firebase.analytics.log_number
*Type:* FUNCTION
Log an event with one float parameter.

**Parameters**

- `name` (string) - Event name
- `PARAMeter_name` (string) - Parameter name
- `PARAMeter_value` (number) - Parameter value

### firebase.analytics.log_table
*Type:* FUNCTION
Log an event with table parameters.

**Parameters**

- `name` (string) - Event name
- `parameters_table` (table) - Table with parameters (key-value pairs)

### firebase.analytics.set_default_event_params
*Type:* FUNCTION
Log an event with table parameters.

**Parameters**

- `default_params` (table) - Table with default parameters (key-value pairs)

### firebase.analytics.set_user_id
*Type:* FUNCTION
Sets the user ID property.

**Parameters**

- `user_id` (string) - User ID property

### firebase.analytics.set_user_property
*Type:* FUNCTION
Set a user property to the given value.

**Parameters**

- `name` (string) - User property name
- `property` (string) - User property value

### firebase.analytics.reset
*Type:* FUNCTION
Clears all data for this app from the device and resets the app instance id.

### firebase.analytics.get_id
*Type:* FUNCTION
Get the instance ID from the service. Returned in callback with MSG_INSTANCE_ID message_id.

### firebase.analytics.set_enabled
*Type:* FUNCTION
Sets whether analytics collection is enabled for this app on this device.

**Parameters**

- `key` (boolean) - The value

### MSG_ERROR
*Type:* VARIABLE
Event generated when an error occurred.

### MSG_INSTANCE_ID
*Type:* VARIABLE
Event generated when instance_id ready after `firebase.analytics.get_id()` call

### EVENT_ADIMPRESSION
*Type:* STRING
Predefined event

### EVENT_ADDPAYMENTINFO
*Type:* STRING
Predefined event

### EVENT_ADDSHIPPINGINFO
*Type:* STRING
Predefined event

### EVENT_ADDTOCART
*Type:* STRING
Predefined event

### EVENT_ADDTOWISHLIST
*Type:* STRING
Predefined event

### EVENT_APPOPEN
*Type:* STRING
Predefined event

### EVENT_BEGINCHECKOUT
*Type:* STRING
Predefined event

### EVENT_CAMPAIGNDETAILS
*Type:* STRING
Predefined event

### EVENT_EARNVIRTUALCURRENCY
*Type:* STRING
Predefined event

### EVENT_GENERATELEAD
*Type:* STRING
Predefined event

### EVENT_JOINGROUP
*Type:* STRING
Predefined event

### EVENT_LEVELEND
*Type:* STRING
Predefined event

### EVENT_LEVELSTART
*Type:* STRING
Predefined event

### EVENT_LEVELUP
*Type:* STRING
Predefined event

### EVENT_LOGIN
*Type:* STRING
Predefined event

### EVENT_POSTSCORE
*Type:* STRING
Predefined event

### EVENT_PURCHASE
*Type:* STRING
Predefined event

### EVENT_REFUND
*Type:* STRING
Predefined event

### EVENT_REMOVEFROMCART
*Type:* STRING
Predefined event

### EVENT_SCREENVIEW
*Type:* STRING
Predefined event

### EVENT_SEARCH
*Type:* STRING
Predefined event

### EVENT_SELECTCONTENT
*Type:* STRING
Predefined event

### EVENT_SELECTITEM
*Type:* STRING
Predefined event

### EVENT_SELECTPROMOTION
*Type:* STRING
Predefined event

### EVENT_SHARE
*Type:* STRING
Predefined event

### EVENT_SIGNUP
*Type:* STRING
Predefined event

### EVENT_SPENDVIRTUALCURRENCY
*Type:* STRING
Predefined event

### EVENT_TUTORIALBEGIN
*Type:* STRING
Predefined event

### EVENT_TUTORIALCOMPLETE
*Type:* STRING
Predefined event

### EVENT_UNLOCKACHIEVEMENT
*Type:* STRING
Predefined event

### EVENT_VIEWCART
*Type:* STRING
Predefined event

### EVENT_VIEWITEM
*Type:* STRING
Predefined event

### EVENT_VIEWITEMLIST
*Type:* STRING
Predefined event

### EVENT_VIEWPROMOTION
*Type:* STRING
Predefined event

### EVENT_VIEWSEARCHRESULTS
*Type:* STRING
Predefined event

### PARAM_ADFORMAT
*Type:* STRING
Predefined parameter

### PARAM_ADNETWORKCLICKID
*Type:* STRING
Predefined parameter

### PARAM_ADPLATFORM
*Type:* STRING
Predefined parameter

### PARAM_ADSOURCE
*Type:* STRING
Predefined parameter

### PARAM_ADUNITNAME
*Type:* STRING
Predefined parameter

### PARAM_AFFILIATION
*Type:* STRING
Predefined parameter

### PARAM_CP1
*Type:* STRING
Predefined parameter

### PARAM_CAMPAIGN
*Type:* STRING
Predefined parameter

### PARAM_CAMPAIGNID
*Type:* STRING
Predefined parameter

### PARAM_CHARACTER
*Type:* STRING
Predefined parameter

### PARAM_CONTENT
*Type:* STRING
Predefined parameter

### PARAM_CONTENTTYPE
*Type:* STRING
Predefined parameter

### PARAM_COUPON
*Type:* STRING
Predefined parameter

### PARAM_CREATIVEFORMAT
*Type:* STRING
Predefined parameter

### PARAM_CREATIVENAME
*Type:* STRING
Predefined parameter

### PARAM_CREATIVESLOT
*Type:* STRING
Predefined parameter

### PARAM_CURRENCY
*Type:* STRING
Predefined parameter

### PARAM_DESTINATION
*Type:* STRING
Predefined parameter

### PARAM_DISCOUNT
*Type:* STRING
Predefined parameter

### PARAM_ENDDATE
*Type:* STRING
Predefined parameter

### PARAM_EXTENDSESSION
*Type:* STRING
Predefined parameter

### PARAM_FLIGHTNUMBER
*Type:* STRING
Predefined parameter

### PARAM_GROUPID
*Type:* STRING
Predefined parameter

### PARAM_INDEX
*Type:* STRING
Predefined parameter

### PARAM_ITEMBRAND
*Type:* STRING
Predefined parameter

### PARAM_ITEMCATEGORY
*Type:* STRING
Predefined parameter

### PARAM_ITEMCATEGORY2
*Type:* STRING
Predefined parameter

### PARAM_ITEMCATEGORY3
*Type:* STRING
Predefined parameter

### PARAM_ITEMCATEGORY4
*Type:* STRING
Predefined parameter

### PARAM_ITEMCATEGORY5
*Type:* STRING
Predefined parameter

### PARAM_ITEMID
*Type:* STRING
Predefined parameter

### PARAM_ITEMLISTID
*Type:* STRING
Predefined parameter

### PARAM_ITEMLISTNAME
*Type:* STRING
Predefined parameter

### PARAM_ITEMNAME
*Type:* STRING
Predefined parameter

### PARAM_ITEMVARIANT
*Type:* STRING
Predefined parameter

### PARAM_ITEMS
*Type:* STRING
Predefined parameter

### PARAM_LEVEL
*Type:* STRING
Predefined parameter

### PARAM_LEVELNAME
*Type:* STRING
Predefined parameter

### PARAM_LOCATION
*Type:* STRING
Predefined parameter

### PARAM_LOCATIONID
*Type:* STRING
Predefined parameter

### PARAM_MARKETINGTACTIC
*Type:* STRING
Predefined parameter

### PARAM_MEDIUM
*Type:* STRING
Predefined parameter

### PARAM_METHOD
*Type:* STRING
Predefined parameter

### PARAM_NUMBEROFNIGHTS
*Type:* STRING
Predefined parameter

### PARAM_NUMBEROFPASSENGERS
*Type:* STRING
Predefined parameter

### PARAM_NUMBEROFROOMS
*Type:* STRING
Predefined parameter

### PARAM_ORIGIN
*Type:* STRING
Predefined parameter

### PARAM_PAYMENTTYPE
*Type:* STRING
Predefined parameter

### PARAM_PRICE
*Type:* STRING
Predefined parameter

### PARAM_PROMOTIONID
*Type:* STRING
Predefined parameter

### PARAM_PROMOTIONNAME
*Type:* STRING
Predefined parameter

### PARAM_QUANTITY
*Type:* STRING
Predefined parameter

### PARAM_SCORE
*Type:* STRING
Predefined parameter

### PARAM_SCREENCLASS
*Type:* STRING
Predefined parameter

### PARAM_SCREENNAME
*Type:* STRING
Predefined parameter

### PARAM_SEARCHTERM
*Type:* STRING
Predefined parameter

### PARAM_SHIPPING
*Type:* STRING
Predefined parameter

### PARAM_SHIPPINGTIER
*Type:* STRING
Predefined parameter

### PARAM_SOURCE
*Type:* STRING
Predefined parameter

### PARAM_SOURCEPLATFORM
*Type:* STRING
Predefined parameter

### PARAM_STARTDATE
*Type:* STRING
Predefined parameter

### PARAM_SUCCESS
*Type:* STRING
Predefined parameter

### PARAM_TAX
*Type:* STRING
Predefined parameter

### PARAM_TERM
*Type:* STRING
Predefined parameter

### PARAM_TRANSACTIONID
*Type:* STRING
Predefined parameter

### PARAM_TRAVELCLASS
*Type:* STRING
Predefined parameter

### PARAM_VALUE
*Type:* STRING
Predefined parameter

### PARAM_VIRTUALCURRENCYNAME
*Type:* STRING
Predefined parameter

### PROP_ALLOWADPERSONALIZATIONSIGNALS
*Type:* STRING
Predefined property

### PROP_SIGNUPMETHOD
*Type:* STRING
Predefined property

###
*Type:* TABLE
Functions and constants for interacting with Firebase Analytics
