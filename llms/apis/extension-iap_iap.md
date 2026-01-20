# extension-iap

**Namespace:** `iap`
**Language:** Lua
**Type:** Extension

Functions and constants for doing in-app purchases. Supported on iOS, Android (Google Play and Amazon) and Facebook Canvas platforms. [icon:ios] [icon:googleplay] [icon:amazon] [icon:facebook]

## API

### iap.buy
*Type:* FUNCTION
Purchase a product.

**Parameters**

- `id` (string) - product to buy
- `options` (table) - optional parameters as properties. The following parameters can be set
  - `request_id` (string) - Facebook only [icon:facebook]. Optional custom unique request id to set for this transaction. The id becomes attached to the payment within the Graph API.
  - `token` (string) - Google Play only [icon:googleplay]. Which subscription offer to use when buying a subscription. The token can be retrieved from the subscriptions table returned when calling iap.list()

**Examples**

```
  local function iap_listener(self, transaction, error)
    if error == nil then
      -- purchase is successful.
      print(transaction.date)
      -- required if auto finish transactions is disabled in project settings
      if (transaction.state == iap.TRANS_STATE_PURCHASED) then
        -- do server-side verification of purchase here..
        iap.finish(transaction)
      end
    else
      print(error.error, error.reason)
    end
  end

  function init(self)
      iap.set_listener(iap_listener)
      iap.buy("my_iap")
  end

```

### iap.finish
*Type:* FUNCTION
Explicitly finish a product transaction. [icon:attention] Calling iap.finish is required on a successful transaction if `auto_finish_transactions` is disabled in project settings. Calling this function with `auto_finish_transactions` set will be ignored and a warning is printed. The `transaction.state` field must equal `iap.TRANS_STATE_PURCHASED`.

**Parameters**

- `transaction` (table) - transaction table parameter as supplied in listener callback

### iap.acknowledge
*Type:* FUNCTION
Acknowledge a transaction. [icon:attention] Calling iap.acknowledge is required on a successful transaction on Google Play unless iap.finish is called. The transaction.state field must equal iap.TRANS_STATE_PURCHASED.

**Parameters**

- `transaction` (table) - transaction table parameter as supplied in listener callback

### iap.get_provider_id
*Type:* FUNCTION
Get current iap provider

**Returns**

- `constant` - one of the following values
- `iap.PROVIDER_ID_GOOGLE`
- `iap.PROVIDER_ID_AMAZON`
- `iap.PROVIDER_ID_APPLE`
- `iap.PROVIDER_ID_FACEBOOK`

### iap.list
*Type:* FUNCTION
Get a list of all avaliable iap products.

**Parameters**

- `ids` (table) - table (array) of identifiers to get products from
- `callback` (function) - result callback taking the following parameters
  - `self` (object) - The current object.
  - `products` (table) - a table describing the available iap products.
    - `ident` (string) - The product identifier.
    - `title` (string) - The product title.
    - `description` (string) - The product description.
    - `price` (number) - The price of the product. For Google Play [icon:googleplay] this is used only for in-app products
    - `price_string` (string) - The price of the product, as a formatted string (amount and currency symbol). For Google Play [icon:googleplay] this is used only for in-app products
    - `currency_code` (string) - The currency code. For Google Play [icon:googleplay] this is the merchant's locale, instead of the user's. For Google Play [icon:googleplay] this is used only for in-app products
    - `subscriptions` (table) - Only available for Google Play [icon:googleplay]. List of subscription offers. Each offer contains a token and a list of price and billing options. See https://developer.android.com/reference/com/android/billingclient/api/ProductDetails.PricingPhase
      - `token` (string) - The token associated with the pricing phases for the subscription.
      - `pricing` (table) - The pricing phases for the subscription.
        - `price_string` (string) - Formatted price for the payment cycle, including currency sign.
        - `price` (number) - Price of the payment cycle in micro-units.
        - `currency_code` (string) - ISO 4217 currency code
        - `billing_period` (string) - Billing period of the payment cycle, specified in ISO 8601 format
        - `billing_cycle_count` (number) - Number of cycles for which the billing period is applied.
        - `recurrence_mode` (string) - FINITE, INFINITE or NONE
  - `error` (table) - a table containing error information. `nil` if there is no error. - `error` (the error message)

**Examples**

```
  local function iap_callback(self, products, error)
    if error == nil then
      for k,p in pairs(products) do
        -- present the product
        print(p.title)
        print(p.description)
      end
    else
      print(error.error)
    end
  end

  function init(self)
      iap.list({"my_iap"}, iap_callback)
  end

```

### iap.restore
*Type:* FUNCTION
Restore previously purchased products.

**Returns**

- `boolean` - value is `true` if current store supports handling restored transactions, otherwise `false`.

### iap.set_listener
*Type:* FUNCTION
Set the callback function to receive purchase transaction events.

**Parameters**

- `listener` (function) - listener callback function. Pass an empty function if you no longer wish to receive callbacks.
  - `self` (object) - The current object.
  - `transaction` (table) - a table describing the transaction.
    - `ident` (string) - The product identifier.
    - `state` (string) - The transaction state. One of the following
- `iap.TRANS_STATE_FAILED`
- `iap.TRANS_STATE_PURCHASED`
- `iap.TRANS_STATE_PURCHASING`
- `iap.TRANS_STATE_RESTORED`
- `iap.TRANS_STATE_UNVERIFIED`
    - `date` (string) - The date and time for the transaction.
    - `trans_ident` (string) - The transaction identifier. This field is only set when `state` is `TRANS_STATE_RESTORED`, `TRANS_STATE_UNVERIFIED` or `TRANS_STATE_PURCHASED`.
    - `receipt` (string) - The transaction receipt. This field is only set when `state` is `TRANS_STATE_PURCHASED` or `TRANS_STATE_UNVERIFIED`.
    - `original_trans` (string) - Apple only [icon:apple]. The original transaction. This field is only set when `state` is `TRANS_STATE_RESTORED`.
    - `original_json` (string) - Android only [icon:android]. The purchase order details in JSON format.
    - `signature` (string) - Google Play only [icon:googleplay]. A string containing the signature of the purchase data that was signed with the private key of the developer.
    - `request_id` (string) - Facebook only [icon:facebook]. This field is set to the optional custom unique request id `request_id` if set in the `iap.buy()` call parameters.
    - `user_id` (string) - Amazon Pay only [icon:amazon]. The user ID.
    - `is_sandbox_mode` (boolean) - Amazon Pay only [icon:amazon]. If `true`, the SDK is running in Sandbox mode. This only allows interactions with the Amazon AppTester. Use this mode only for testing locally.
    - `cancel_date` (string) - Amazon Pay only [icon:amazon]. The cancel date for the purchase. This field is only set if the purchase is canceled.
    - `canceled` (string) - Amazon Pay only [icon:amazon]. Is set to `true` if the receipt was canceled or has expired; otherwise `false`.
  - `error` (table) - a table containing error information. `nil` if there is no error. `error` - the error message. `reason` - the reason for the error, value can be one of the following constants
- `iap.REASON_UNSPECIFIED`
- `iap.REASON_USER_CANCELED`

### PROVIDER_ID_AMAZON
*Type:* VARIABLE
provider id for Amazon

### PROVIDER_ID_APPLE
*Type:* VARIABLE
provider id for Apple

### PROVIDER_ID_FACEBOOK
*Type:* VARIABLE
provider id for Facebook

### PROVIDER_ID_GOOGLE
*Type:* VARIABLE
iap provider id for Google

### REASON_UNSPECIFIED
*Type:* VARIABLE
unspecified error reason

### REASON_USER_CANCELED
*Type:* VARIABLE
user canceled reason

### TRANS_STATE_FAILED
*Type:* VARIABLE
transaction failed state

### TRANS_STATE_PURCHASED
*Type:* VARIABLE
transaction purchased state

### TRANS_STATE_PURCHASING
*Type:* VARIABLE
transaction purchasing state This is an intermediate mode followed by TRANS_STATE_PURCHASED. Store provider support dependent.

### TRANS_STATE_RESTORED
*Type:* VARIABLE
transaction restored state This is only available on store providers supporting restoring purchases.

### TRANS_STATE_UNVERIFIED
*Type:* VARIABLE
transaction unverified state, requires verification of purchase
