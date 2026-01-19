# extension-xsolla

**Namespace:** `shop`
**Language:** Lua
**Type:** Extension

Functions to use the Xsolla Shop Builder API.

## API

### shop.cancel
*Type:* FUNCTION
Cancel a cancellation token

**Parameters**

- `token` (table) - The cancellation token

### shop.cancellation_token
*Type:* FUNCTION
Create a cancellation token

**Returns**

- `table` - A cancellation token

### shop.set_bearer_token
*Type:* FUNCTION
Set a bearer token

**Parameters**

- `token` (string) - The bearer token

### shop.set_username_password
*Type:* FUNCTION
Set a username and password for basic authentication

**Parameters**

- `username` (string) - The username
- `password` (string) - The password

### shop.set_merchant_auth
*Type:* FUNCTION
Set merchant id and api key for use with 'basicMerchantAuth' authentication

**Parameters**

- `merchant_id` (string) - The merchant id
- `api_key` (string) - The API key

### shop.set_auth_for_cart
*Type:* FUNCTION
Set authorization when using 'AuthForCart' authentication

**Parameters**

- `authorization_id` (string) - Unique authorization id
- `user` (string) - The user email

### shop.sync
*Type:* FUNCTION
Run code within a coroutine.

**Parameters**

- `fn` (function) - The function to run
- `cancellation_token` (table) - Optional cancellation token

### shop.get_payment_url
*Type:* FUNCTION
get the payment url for an order

**Parameters**

- `order` (table)
- `is_sandbox` (boolean)

**Returns**

- `string`

### shop.get_bundle_list
*Type:* FUNCTION
Get list of bundles

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_bundle
*Type:* FUNCTION
Get specified bundle

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `sku (REQUIRED)` (string) - Bundle SKU.
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_bundle_list_in_group
*Type:* FUNCTION
Get list of bundles by specified group

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `external_id (REQUIRED)` (string) - Group external ID.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_cart_by_id
*Type:* FUNCTION
Get cart by cart ID

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `cart_id (REQUIRED)` (string) - Cart ID.
- `currency` (string) - The item price currency displayed in the cart. Three-letter currency code per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Check the documentation for detailed information about [currencies supported by Xsolla](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_user_cart
*Type:* FUNCTION
Get current user's cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `currency` (string) - The item price currency displayed in the cart. Three-letter currency code per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Check the documentation for detailed information about [currencies supported by Xsolla](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.cart_clear_by_id
*Type:* FUNCTION
Delete all cart items by cart ID

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `cart_id (REQUIRED)` (string) - Cart ID.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.cart_clear
*Type:* FUNCTION
Delete all cart items from current cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.cart_fill
*Type:* FUNCTION
Fill cart with items

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  items =
  {
    {
      sku = "com.xsolla.booster_mega_1",
      quantity = 123,
    },
  },
}

```

### shop.cart_fill_by_id
*Type:* FUNCTION
Fill specific cart with items

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `cart_id (REQUIRED)` (string) - Cart ID.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  items =
  {
    {
      sku = "com.xsolla.booster_mega_1",
      quantity = 123,
    },
  },
}

```

### shop.put_item_by_cart_id
*Type:* FUNCTION
Update cart item by cart ID

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `cart_id (REQUIRED)` (string) - Cart ID.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  quantity = 123.456,
}

```

### shop.delete_item_by_cart_id
*Type:* FUNCTION
Delete cart item by cart ID

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `cart_id (REQUIRED)` (string) - Cart ID.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.put_item
*Type:* FUNCTION
Update cart item from current cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  quantity = 123.456,
}

```

### shop.delete_item
*Type:* FUNCTION
Delete cart item from current cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.create_order_by_cart_id
*Type:* FUNCTION
Create order with all items from particular cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `cart_id (REQUIRED)` (string) - Cart ID.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  currency = "Order price currency. Three-letter currency code per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Check the documentation for detailed information about [currencies supported by Xsolla](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/).",
  locale = "Response language.",
  sandbox = true,
  settings =
  {
    cart_payment_settings_ui =
    {
      theme = "Payment UI theme. Can be `63295a9a2e47fab76f7708e1` for the light theme (default) or `63295aab2e47fab76f7708e3` for the dark theme. You can also [create a custom theme](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_in_token) and pass its ID in this parameter.",
      desktop =
      {
        header =
        {
          is_visible = true,
          visible_logo = true,
          visible_name = true,
          visible_purchase = true,
          type = "How to show the header. Can be `compact` (hides project name and user ID) or `normal` (default).",
          close_button = true,
        },
      },
      mode = "Interface mode in payment UI. Can be `user_account` only. The header contains only the account navigation menu, and the user cannot select a product or make a payment. This mode is only available on the desktop.",
      user_account =
      {
        payment_accounts =
        {
          enable = true,
        },
        info =
        {
          enable = true,
          order = 123,
        },
        subscriptions =
        {
          enable = true,
          order = 123,
        },
      },
      header =
      {
        visible_virtual_currency_balance = true,
      },
      mobile =
      {
        header =
        {
          close_button = true,
        },
      },
      is_prevent_external_link_open = true,
      is_payment_methods_list_mode = true,
      is_independent_windows = true,
      currency_format = "Set to `code` to display a three-letter [ISO 4217](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/) currency code in the payment UI. The currency symbol is displayed instead of the three-letter currency code by default.",
      is_show_close_widget_warning = true,
      layout = "Location of the main elements of the payment UI. You can open the payment UI inside your game and/or swap the columns with information about an order and payment methods. Refer to the [customization instructions](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_layout) for detailed information.",
      is_three_ds_independent_windows = true,
      is_cart_open_by_default = true,
    },
    cart_payment_settings_payment_method = 123,
    cart_payment_settings_return_url = "Page to redirect the user to after payment. Parameters `user_id`, `foreigninvoice`, `invoice_id` and `status` will be automatically added to the link.",
    cart_payment_redirect_policy =
    {
      redirect_conditions = "none",
      delay = 0,
      status_for_manual_redirection = "none",
      redirect_button_caption = "Text button",
    },
  },
  custom_parameters =
  {
  },
}

```

### shop.create_order
*Type:* FUNCTION
Create order with all items from current cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  currency = "Order price currency. Three-letter currency code per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Check the documentation for detailed information about [currencies supported by Xsolla](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/).",
  locale = "Response language.",
  sandbox = true,
  settings =
  {
    cart_payment_settings_ui =
    {
      theme = "Payment UI theme. Can be `63295a9a2e47fab76f7708e1` for the light theme (default) or `63295aab2e47fab76f7708e3` for the dark theme. You can also [create a custom theme](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_in_token) and pass its ID in this parameter.",
      desktop =
      {
        header =
        {
          is_visible = true,
          visible_logo = true,
          visible_name = true,
          visible_purchase = true,
          type = "How to show the header. Can be `compact` (hides project name and user ID) or `normal` (default).",
          close_button = true,
        },
      },
      mode = "Interface mode in payment UI. Can be `user_account` only. The header contains only the account navigation menu, and the user cannot select a product or make a payment. This mode is only available on the desktop.",
      user_account =
      {
        payment_accounts =
        {
          enable = true,
        },
        info =
        {
          enable = true,
          order = 123,
        },
        subscriptions =
        {
          enable = true,
          order = 123,
        },
      },
      header =
      {
        visible_virtual_currency_balance = true,
      },
      mobile =
      {
        header =
        {
          close_button = true,
        },
      },
      is_prevent_external_link_open = true,
      is_payment_methods_list_mode = true,
      is_independent_windows = true,
      currency_format = "Set to `code` to display a three-letter [ISO 4217](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/) currency code in the payment UI. The currency symbol is displayed instead of the three-letter currency code by default.",
      is_show_close_widget_warning = true,
      layout = "Location of the main elements of the payment UI. You can open the payment UI inside your game and/or swap the columns with information about an order and payment methods. Refer to the [customization instructions](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_layout) for detailed information.",
      is_three_ds_independent_windows = true,
      is_cart_open_by_default = true,
    },
    cart_payment_settings_payment_method = 123,
    cart_payment_settings_return_url = "Page to redirect the user to after payment. Parameters `user_id`, `foreigninvoice`, `invoice_id` and `status` will be automatically added to the link.",
    cart_payment_redirect_policy =
    {
      redirect_conditions = "none",
      delay = 0,
      status_for_manual_redirection = "none",
      redirect_button_caption = "Text button",
    },
  },
  custom_parameters =
  {
  },
}

```

### shop.create_order_with_item
*Type:* FUNCTION
Create order with specified item

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  currency = "Order price currency. Three-letter currency code per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Check the documentation for detailed information about [currencies supported by Xsolla](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/).",
  locale = "Response language.",
  sandbox = true,
  quantity = 123,
  promo_code = "Redeems a code of a promo code promotion with payment.",
  settings =
  {
    cart_payment_settings_ui =
    {
      theme = "Payment UI theme. Can be `63295a9a2e47fab76f7708e1` for the light theme (default) or `63295aab2e47fab76f7708e3` for the dark theme. You can also [create a custom theme](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_in_token) and pass its ID in this parameter.",
      desktop =
      {
        header =
        {
          is_visible = true,
          visible_logo = true,
          visible_name = true,
          visible_purchase = true,
          type = "How to show the header. Can be `compact` (hides project name and user ID) or `normal` (default).",
          close_button = true,
        },
      },
      mode = "Interface mode in payment UI. Can be `user_account` only. The header contains only the account navigation menu, and the user cannot select a product or make a payment. This mode is only available on the desktop.",
      user_account =
      {
        payment_accounts =
        {
          enable = true,
        },
        info =
        {
          enable = true,
          order = 123,
        },
        subscriptions =
        {
          enable = true,
          order = 123,
        },
      },
      header =
      {
        visible_virtual_currency_balance = true,
      },
      mobile =
      {
        header =
        {
          close_button = true,
        },
      },
      is_prevent_external_link_open = true,
      is_payment_methods_list_mode = true,
      is_independent_windows = true,
      currency_format = "Set to `code` to display a three-letter [ISO 4217](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/) currency code in the payment UI. The currency symbol is displayed instead of the three-letter currency code by default.",
      is_show_close_widget_warning = true,
      layout = "Location of the main elements of the payment UI. You can open the payment UI inside your game and/or swap the columns with information about an order and payment methods. Refer to the [customization instructions](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_layout) for detailed information.",
      is_three_ds_independent_windows = true,
      is_cart_open_by_default = true,
    },
    cart_payment_settings_payment_method = 123,
    cart_payment_settings_return_url = "Page to redirect the user to after payment. Parameters `user_id`, `foreigninvoice`, `invoice_id` and `status` will be automatically added to the link.",
    cart_payment_redirect_policy =
    {
      redirect_conditions = "none",
      delay = 0,
      status_for_manual_redirection = "none",
      redirect_button_caption = "Text button",
    },
  },
  custom_parameters =
  {
  },
}

```

### shop.create_free_order
*Type:* FUNCTION
Create order with free cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  currency = "Order price currency. Three-letter currency code per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Check the documentation for detailed information about [currencies supported by Xsolla](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/).",
  locale = "Response language.",
  sandbox = true,
  settings =
  {
    cart_payment_settings_ui =
    {
      theme = "Payment UI theme. Can be `63295a9a2e47fab76f7708e1` for the light theme (default) or `63295aab2e47fab76f7708e3` for the dark theme. You can also [create a custom theme](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_in_token) and pass its ID in this parameter.",
      desktop =
      {
        header =
        {
          is_visible = true,
          visible_logo = true,
          visible_name = true,
          visible_purchase = true,
          type = "How to show the header. Can be `compact` (hides project name and user ID) or `normal` (default).",
          close_button = true,
        },
      },
      mode = "Interface mode in payment UI. Can be `user_account` only. The header contains only the account navigation menu, and the user cannot select a product or make a payment. This mode is only available on the desktop.",
      user_account =
      {
        payment_accounts =
        {
          enable = true,
        },
        info =
        {
          enable = true,
          order = 123,
        },
        subscriptions =
        {
          enable = true,
          order = 123,
        },
      },
      header =
      {
        visible_virtual_currency_balance = true,
      },
      mobile =
      {
        header =
        {
          close_button = true,
        },
      },
      is_prevent_external_link_open = true,
      is_payment_methods_list_mode = true,
      is_independent_windows = true,
      currency_format = "Set to `code` to display a three-letter [ISO 4217](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/) currency code in the payment UI. The currency symbol is displayed instead of the three-letter currency code by default.",
      is_show_close_widget_warning = true,
      layout = "Location of the main elements of the payment UI. You can open the payment UI inside your game and/or swap the columns with information about an order and payment methods. Refer to the [customization instructions](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_layout) for detailed information.",
      is_three_ds_independent_windows = true,
      is_cart_open_by_default = true,
    },
    cart_payment_settings_payment_method = 123,
    cart_payment_settings_return_url = "Page to redirect the user to after payment. Parameters `user_id`, `foreigninvoice`, `invoice_id` and `status` will be automatically added to the link.",
    cart_payment_redirect_policy =
    {
      redirect_conditions = "none",
      delay = 0,
      status_for_manual_redirection = "none",
      redirect_button_caption = "Text button",
    },
  },
  custom_parameters =
  {
  },
}

```

### shop.create_free_order_by_cart_id
*Type:* FUNCTION
Create order with particular free cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `cart_id (REQUIRED)` (string) - Cart ID.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  currency = "Order price currency. Three-letter currency code per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Check the documentation for detailed information about [currencies supported by Xsolla](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/).",
  locale = "Response language.",
  sandbox = true,
  settings =
  {
    cart_payment_settings_ui =
    {
      theme = "Payment UI theme. Can be `63295a9a2e47fab76f7708e1` for the light theme (default) or `63295aab2e47fab76f7708e3` for the dark theme. You can also [create a custom theme](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_in_token) and pass its ID in this parameter.",
      desktop =
      {
        header =
        {
          is_visible = true,
          visible_logo = true,
          visible_name = true,
          visible_purchase = true,
          type = "How to show the header. Can be `compact` (hides project name and user ID) or `normal` (default).",
          close_button = true,
        },
      },
      mode = "Interface mode in payment UI. Can be `user_account` only. The header contains only the account navigation menu, and the user cannot select a product or make a payment. This mode is only available on the desktop.",
      user_account =
      {
        payment_accounts =
        {
          enable = true,
        },
        info =
        {
          enable = true,
          order = 123,
        },
        subscriptions =
        {
          enable = true,
          order = 123,
        },
      },
      header =
      {
        visible_virtual_currency_balance = true,
      },
      mobile =
      {
        header =
        {
          close_button = true,
        },
      },
      is_prevent_external_link_open = true,
      is_payment_methods_list_mode = true,
      is_independent_windows = true,
      currency_format = "Set to `code` to display a three-letter [ISO 4217](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/) currency code in the payment UI. The currency symbol is displayed instead of the three-letter currency code by default.",
      is_show_close_widget_warning = true,
      layout = "Location of the main elements of the payment UI. You can open the payment UI inside your game and/or swap the columns with information about an order and payment methods. Refer to the [customization instructions](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_layout) for detailed information.",
      is_three_ds_independent_windows = true,
      is_cart_open_by_default = true,
    },
    cart_payment_settings_payment_method = 123,
    cart_payment_settings_return_url = "Page to redirect the user to after payment. Parameters `user_id`, `foreigninvoice`, `invoice_id` and `status` will be automatically added to the link.",
    cart_payment_redirect_policy =
    {
      redirect_conditions = "none",
      delay = 0,
      status_for_manual_redirection = "none",
      redirect_button_caption = "Text button",
    },
  },
  custom_parameters =
  {
  },
}

```

### shop.create_free_order_with_item
*Type:* FUNCTION
Create order with specified free item

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  currency = "Order price currency. Three-letter currency code per [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). Check the documentation for detailed information about [currencies supported by Xsolla](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/).",
  locale = "Response language.",
  sandbox = true,
  quantity = 123,
  promo_code = "Redeems a code of a promo code promotion with payment.",
  settings =
  {
    cart_payment_settings_ui =
    {
      theme = "Payment UI theme. Can be `63295a9a2e47fab76f7708e1` for the light theme (default) or `63295aab2e47fab76f7708e3` for the dark theme. You can also [create a custom theme](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_in_token) and pass its ID in this parameter.",
      desktop =
      {
        header =
        {
          is_visible = true,
          visible_logo = true,
          visible_name = true,
          visible_purchase = true,
          type = "How to show the header. Can be `compact` (hides project name and user ID) or `normal` (default).",
          close_button = true,
        },
      },
      mode = "Interface mode in payment UI. Can be `user_account` only. The header contains only the account navigation menu, and the user cannot select a product or make a payment. This mode is only available on the desktop.",
      user_account =
      {
        payment_accounts =
        {
          enable = true,
        },
        info =
        {
          enable = true,
          order = 123,
        },
        subscriptions =
        {
          enable = true,
          order = 123,
        },
      },
      header =
      {
        visible_virtual_currency_balance = true,
      },
      mobile =
      {
        header =
        {
          close_button = true,
        },
      },
      is_prevent_external_link_open = true,
      is_payment_methods_list_mode = true,
      is_independent_windows = true,
      currency_format = "Set to `code` to display a three-letter [ISO 4217](https://developers.xsolla.com/doc/pay-station/references/supported-currencies/) currency code in the payment UI. The currency symbol is displayed instead of the three-letter currency code by default.",
      is_show_close_widget_warning = true,
      layout = "Location of the main elements of the payment UI. You can open the payment UI inside your game and/or swap the columns with information about an order and payment methods. Refer to the [customization instructions](https://developers.xsolla.com/doc/pay-station/features/ui-theme-customization/#pay_station_ui_theme_customization_layout) for detailed information.",
      is_three_ds_independent_windows = true,
      is_cart_open_by_default = true,
    },
    cart_payment_settings_payment_method = 123,
    cart_payment_settings_return_url = "Page to redirect the user to after payment. Parameters `user_id`, `foreigninvoice`, `invoice_id` and `status` will be automatically added to the link.",
    cart_payment_redirect_policy =
    {
      redirect_conditions = "none",
      delay = 0,
      status_for_manual_redirection = "none",
      redirect_button_caption = "Text button",
    },
  },
  custom_parameters =
  {
  },
}

```

### shop.get_order
*Type:* FUNCTION
Get order

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `order_id (REQUIRED)` (string) - Order ID.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_upsell_for_project_client
*Type:* FUNCTION
Get list of upsell items in project

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_games_list
*Type:* FUNCTION
Get games list

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_games_group
*Type:* FUNCTION
Get games list by specified group

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `external_id (REQUIRED)` (string) - Group external ID.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_game_by_sku
*Type:* FUNCTION
Get game for catalog

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_game_key_by_sku
*Type:* FUNCTION
Get game key for catalog

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_game_keys_group
*Type:* FUNCTION
Get game keys list by specified group

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `external_id (REQUIRED)` (string) - Group external ID.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_drm_list
*Type:* FUNCTION
Get DRM list

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_user_games
*Type:* FUNCTION
Get list of games owned by user

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `sandbox` (integer) - What type of entitlements should be returned. If the parameter is set to 1, the entitlements received by the user in the sandbox mode only are returned. If the parameter isn&#x27;t passed or is set to 0, the entitlements received by the user in the live mode only are returned.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request. Available fields `attributes`.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.redeem_game_pin_code
*Type:* FUNCTION
Redeem game code by client

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  code = "AAAA-BBBB-CCCC-DDDD",
  sandbox = false,
}

```

### shop.redeem_coupon
*Type:* FUNCTION
Redeem coupon code

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  coupon_code = "WINTER2021",
  selected_unit_items =
  {
  },
}

```

### shop.get_coupon_rewards_by_code
*Type:* FUNCTION
Get coupon rewards

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `coupon_code (REQUIRED)` (string) - Unique case sensitive code. Contains letters and numbers.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.redeem_promo_code
*Type:* FUNCTION
Redeem promo code

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  coupon_code = "SUMMER2021",
  cart =
  {
    id = "Cart ID.",
  },
  selected_unit_items =
  {
  },
}

```

### shop.remove_cart_promo_code
*Type:* FUNCTION
Remove promo code from cart

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  cart =
  {
    id = "Cart ID.",
  },
}

```

### shop.get_promo_code_rewards_by_code
*Type:* FUNCTION
Get promo code rewards

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `promocode_code (REQUIRED)` (string) - Unique case sensitive code. Contains letters and numbers.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.verify_promotion_code
*Type:* FUNCTION
Verify promotion code

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `code (REQUIRED)` (string) - Unique case-sensitive code. Contains letters and numbers.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_virtual_items
*Type:* FUNCTION
Get virtual items list

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_virtual_items_sku
*Type:* FUNCTION
Get virtual item by SKU

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_all_virtual_items
*Type:* FUNCTION
Get all virtual items list

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_virtual_currency
*Type:* FUNCTION
Get virtual currency list

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_virtual_currency_sku
*Type:* FUNCTION
Get virtual currency by SKU

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `virtual_currency_sku (REQUIRED)` (string) - Virtual currency SKU.
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_virtual_currency_package
*Type:* FUNCTION
Get virtual currency package list

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_virtual_currency_package_sku
*Type:* FUNCTION
Get virtual currency package by SKU

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `virtual_currency_package_sku (REQUIRED)` (string) - Virtual currency package SKU.
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_virtual_items_group
*Type:* FUNCTION
Get items list by specified group

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `external_id (REQUIRED)` (string) - Group external ID.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_item_groups
*Type:* FUNCTION
Get item group list

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.create_order_with_item_for_virtual_currency
*Type:* FUNCTION
Create order with specified item purchased by virtual currency

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_sku (REQUIRED)` (string) - Item SKU.
- `virtual_currency_sku (REQUIRED)` (string) - Virtual currency SKU.
- `platform` (string) - Publishing platform the user plays on `xsolla` (default), `playstation_network`, `xbox_live`, `pc_standalone`, `nintendo_shop`, `google_play`, `app_store_ios`, `android_standalone`, `ios_standalone`, `android_other`, `ios_other`, `pc_other`.
- `body` (table)
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

**Examples**

```
{
  custom_parameters =
  {
  },
}

```

### shop.get_sellable_items
*Type:* FUNCTION
Get sellable items list

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_sellable_item_by_id
*Type:* FUNCTION
Get sellable item by ID

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `item_id (REQUIRED)` (string) - Item ID.
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_sellable_item_by_sku
*Type:* FUNCTION
Get sellable item by SKU

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `sku (REQUIRED)` (string) - Item SKU.
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_sellable_items_group
*Type:* FUNCTION
Get sellable items list by specified group

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `external_id (REQUIRED)` (string) - Group external ID.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `locale` (string) - Response language. Two-letter lowercase language code per ISO 639-1.
- `additional_fields` (array) - The list of additional fields. These fields will be in the response if you send them in your request.
- `country` (string) - Two-letter uppercase country code per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Check the documentation for detailed information about [countries supported by Xsolla](https://developers.xsolla.com/doc/shop-builder/references/supported-countries/) and [the process of determining the country](https://developers.xsolla.com/doc/shop-builder/features/pricing-policy/#pricing_policy_country_determination).
- `promo_code` (string) - Unique case sensitive code. Contains letters and numbers.
- `show_inactive_time_limited_items` (integer) - Shows time-limited items that are not available to the user. The validity period of such items has not started or has already expired.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_reward_chains_list
*Type:* FUNCTION
Get current user's reward chains

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `limit` (integer) - Limit for the number of elements on the page.
- `offset` (integer) - Number of the element from which the list is generated (the count starts from 0).
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_user_reward_chain_balance
*Type:* FUNCTION
Get current user's value point balance

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `reward_chain_id (REQUIRED)` (integer) - Reward chain ID.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.claim_user_reward_chain_step_reward
*Type:* FUNCTION
Claim step reward

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID. You can find this parameter in your [Publisher Account](https://publisher.xsolla.com/) next to the name of the project.
- `reward_chain_id (REQUIRED)` (integer) - Reward chain ID.
- `step_id (REQUIRED)` (integer) - Reward chain step ID.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.get_user_clan_top_contributors
*Type:* FUNCTION
Get top 10 contributors to reward chain under clan

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID.
- `reward_chain_id (REQUIRED)` (integer) - Reward chain ID.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token

### shop.user_clan_update
*Type:* FUNCTION
Update current user's clan

**Parameters**

- `project_id (REQUIRED)` (integer) - Project ID.
- `callback` (function) - Optional callback function
- `retry_policy` (table) - Optional retry policy
- `cancellation_token` (table) - Optional cancellation token
