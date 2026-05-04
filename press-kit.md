---
layout: page
title: Defold Press Kit
description: Current Defold brand assets, logo and trademark guidance, and high-resolution Defold Foundation photos for press and media use.
nav: floating
---

{%- capture page_hero_copy -%}
<p>Use the Defold Press Kit for current brand assets, logo and trademark guidance, and high-resolution Defold Foundation photos.</p>
<p>These resources are intended for articles, interviews, videos, event pages, and other coverage of Defold.</p>
{%- endcapture -%}

{%- capture page_hero_actions -%}
{% include primary_button.html link="/logo-and-trademark" text="Logo guidelines" %}
{% include secondary_button.html link="/press" text="Press room" %}
{%- endcapture -%}

{%- capture page_hero_panel -%}
<img class="page-hero-graphic" src="/images/icons/icons-learn-export_ic-learn-documents.svg" alt="Defold press kit illustration" loading="eager" fetchpriority="high">
{%- endcapture -%}

{% include page_hub_hero.html hero_class="press-kit-hub-hero" title="Defold Press Kit" copy=page_hero_copy actions=page_hero_actions panel=page_hero_panel aria_label="Defold press kit overview" %}

<div class="section dark page-dark-section gradient-background-top-dark" markdown="0">
	<div class="container">
		<div class="page-section-heading">
			<h2>Press kit resources</h2>
		</div>
		<div class="page-feature-grid page-grid-two page-grid-flush">
			{% include page_feature_card.html title="Logos and trademark" body="View Defold logo usage rules, download official logo assets, and find the Made with Defold marks for projects and media." link="/logo-and-trademark" thumbnail="/images/logo/logo-on-blue.png" card_class="page-feature-card-manuals" %}
			{% include page_feature_card.html title="Foundation photos" body="Browse high-resolution photos of Defold Foundation board members for articles, interviews, event pages, and other coverage." link="/foundation-photos" thumbnail="/images/foundation/thumbs/Bjorn Ritzl_2020_RW.jpg" card_class="page-feature-card-reference"%}
		</div>
	</div>
</div>

{% include donors_and_partners.html %}
