---
layout: hero_and_text
title: Defold blog
description: The Defold blog contains a mix of Defold news and development updates. From time to time we also invite guest bloggers.
nav: floating
background: /images/hero/defold-top-bg-transparent-2.png
after: [newsletter_signup_link.html, donors_and_partners.html]
---

{%- assign tags = "" | split: "," -%}
{%- for post in site.posts -%}
{%- assign tags = tags | concat: post.tags | uniq | sort -%}
{%- endfor -%}

<h3 class="white">Tags</h3>
<ul class="tags">
{%- for tag in tags -%}
<li><a href="#{{ tag }}">{{ tag | capitalize }}</a></li>
{%- endfor -%}
</ul>

<h3 class="white">Latest posts</h3>
{% for post in site.posts limit: 10 %}
{%- include post_preview.html post=post -%}
{% endfor %}


{%- for tag in tags -%}
<br/>
<h5 class="white"><a id="{{ tag }}"></a>{{ tag | capitalize }}</h5>
{%- for post in site.posts -%}
{%- if post.tags contains tag -%}
{%- include post_preview_small.html post=post -%}
{%- endif -%}
{%- endfor -%}
{%- endfor -%}

<h3 class="white">Tags</h3>
<ul class="tags">
{%- for tag in tags -%}
<li><a href="#{{ tag }}">{{ tag | capitalize }}</a></li>
{%- endfor -%}
</ul>
