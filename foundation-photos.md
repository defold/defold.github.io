---
layout: page
title: Defold Foundation photos
description: High-resolution photos of the Defold Foundation board members for press, articles, interviews, and event coverage.
nav: floating
---

{%- capture page_hero_copy -%}
<p>Download high-resolution photos of the Defold Foundation board members for press, articles, interviews, event pages, and other coverage.</p>
{%- endcapture -%}

{%- capture page_hero_actions -%}
{% include primary_button.html link="#foundation-photos" text="Browse photos" %}
{% include secondary_button.html link="/press-kit" text="Back to press kit" %}
{%- endcapture -%}

{%- capture page_hero_panel -%}
<img class="page-hero-graphic" src="/images/icons/icon-loudspeaker.svg" alt="Defold Foundation photos illustration" loading="eager" fetchpriority="high">
{%- endcapture -%}

{% include page_hub_hero.html hero_class="foundation-photos-hub-hero" title="Defold Foundation Photos" copy=page_hero_copy actions=page_hero_actions panel=page_hero_panel aria_label="Defold Foundation photos overview" %}

<div class="section dark page-dark-section gradient-background-top-dark" id="foundation-photos" markdown="0">
	<div class="container">
		<div class="page-section-heading">
			<h2>Photo downloads</h2>
			<p>Each card opens the original high-resolution image.</p>
		</div>
		<div class="page-feature-grid page-grid-auto-fill page-grid-three page-grid-flush">
			{% include page_feature_card.html title="Sara Cederberg" body="High-resolution Foundation board member photo." link="/images/foundation/highres/Sara Cederberg_2020_RW.jpg" thumbnail="/images/foundation/thumbs/Sara Cederberg_2020_RW.jpg" hide_badge=true cta_text="Open high-resolution image" %}
			{% include page_feature_card.html title="Romain Sididris" body="High-resolution Foundation board member photo." link="/images/foundation/highres/romain.jpg" thumbnail="/images/foundation/thumbs/romain.jpg" hide_badge=true cta_text="Open high-resolution image" %}
			{% include page_feature_card.html title="Mathias Westerdahl" body="High-resolution Foundation board member photo." link="/images/foundation/highres/Mathias Westerdahl_2020_RW.jpg" thumbnail="/images/foundation/thumbs/Mathias Westerdahl_2020_RW.jpg" hide_badge=true cta_text="Open high-resolution image" %}
			{% include page_feature_card.html title="Björn Ritzl" body="High-resolution Foundation board member photo." link="/images/foundation/highres/Bjorn Ritzl_2020_RW.jpg" thumbnail="/images/foundation/thumbs/Bjorn Ritzl_2020_RW.jpg" hide_badge=true cta_text="Open high-resolution image" %}
		</div>
	</div>
</div>

{% include donors_and_partners.html %}
