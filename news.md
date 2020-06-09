---
layout: hero_and_text
title: Defold News
description: All Defold News
nav: floating
background: /images/hero/defold-top-bg-transparent-2.png
after: [donors_and_partners.html]
---

[⇠ Back to Press room](/press)

### All news
{%- for post in site.posts -%}
{%- if post.type == "press" -%}
{%- include post_preview.html post=post -%}
{%- endif -%}
{%- endfor -%}

[⇠ Back to Press room](/press)
