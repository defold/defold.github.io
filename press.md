---
layout: hero_and_text
title: Press
description: Defold Newsroom
nav: floating
after: corporate_partners.html
---

### Media inquiries
For all media inquiries please email [press@defold.se](mailto:press@defold.se).

### Latest news
{%- for post in site.posts -%}
{%- if post.type == "press" -%}
{%- include post_preview.html post=post -%}
{%- endif -%}
{%- endfor -%}
