---
layout: hero_and_text
title: Defold Press and News Room
description: The Defold Press and News Room is your one stop shop to Defold news stories and up to date press information and images.
nav: floating
background: /images/hero/defold-top-bg-transparent-2.png
after: [corporate_partners.html]
---

## Defold in the News
{%- assign counter = '0' -%}
{%- for post in site.posts -%}
{%- if post.type == "press" and counter < '3' -%}
{% capture counter %}{{ counter | plus:'1' }}{% endcapture %}
{%- include post_preview.html post=post -%}
{%- endif -%}
{%- endfor -%}

[More News ⇢](/news)

<br/>
## Press inquiries
Contact us for press inquiries at [press@defold.se](mailto:press@defold.se). For everything else, please see [available options to get in touch](/contact).

<br/>
## Press-kit

Our current brand assets including the Defold logo and Defold Foundation images.

[Press-kit ⇢](/press-kit)
