---
layout: page
title: Defold news
description: Official Defold announcements, Foundation updates, partnerships, roadmap posts, showreels, and other news.
nav: floating
stylesheets:
  - catalog
  - newsletter
---

{%- assign news_posts = site.posts | where: "tags", "news" -%}

{%- capture news_hero_copy -%}
<p>Read official Defold announcements, Foundation updates, partnership news, roadmap posts, showreels, and other news from the Defold team.</p>
{%- endcapture -%}

{%- capture news_hero_actions -%}
{% include primary_button.html link="#news-posts" text="Browse latest news" %}
{% include secondary_button.html link="/press" text="Press room" %}
{%- endcapture -%}

{%- capture news_hero_panel -%}
<img class="page-hero-graphic" src="/images/icons/icon-loudspeaker.svg" alt="Defold news section icon" loading="eager" fetchpriority="high" decoding="async">
{%- endcapture -%}

{% include page_hub_hero.html title="Defold News" copy=news_hero_copy actions=news_hero_actions panel=news_hero_panel aria_label="Defold news illustration" %}

<div class="section asset-hub-section" markdown="0">
	<div class="container">
		<div class="asset-hub-catalog-layout" data-learn-tag-catalog data-default-title="All news" data-initial-sort="date-desc">
			<div class="asset-hub-sidebar">
				<div class="learn-tag-filter asset-hub-toolbar page-surface-panel asset-hub-surface-panel" data-learn-tag-filter data-filter-singular="topic" data-result-items="news posts" data-filter-excluded-tags="news">
					<div class="asset-hub-filter-shell">
						<div class="asset-hub-filter-group asset-hub-filter-search">
							<h3 class="asset-hub-filter-label">Filter</h3>
							{% include catalog_search_field.html id="news-search-posts" input_class="learnsearch" data_attribute_name="data-learn-search" field_type="filter" icon_name="filter" placeholder="Filter news by title or description" aria_label="Filter news by title or description" %}
						</div>
						<div class="asset-hub-filter-group asset-hub-sort-row">
							<h3 class="asset-hub-filter-label">Sort by</h3>
							<div class="asset-hub-sort-links">
								<button type="button" class="filter active" data-learn-sort="date-desc" data-learn-sort-label="Newest" aria-pressed="true">
									{% include site_icon.html name=site.data.asset_tag_icons.timestamp class="asset-hub-filter-icon" %}
									<span class="asset-hub-filter-text">Newest</span>
								</button>
								<button type="button" class="filter" data-learn-sort="date-asc" data-learn-sort-label="Oldest" aria-pressed="false">
									{% include site_icon.html name=site.data.asset_tag_icons.timestamp class="asset-hub-filter-icon" %}
									<span class="asset-hub-filter-text">Oldest</span>
								</button>
							</div>
						</div>
						<div class="asset-hub-filter-group">
							<h3 class="asset-hub-filter-label">Topics</h3>
							<div class="learn-tag-chip-row asset-hub-filter-grid" data-tag-chip-row>
								<button type="button" class="learn-tag-chip filter" data-tag="all" aria-pressed="true">
									{% include site_icon.html name=site.data.asset_tag_icons.all class="asset-hub-filter-icon" %}
									<span class="asset-hub-filter-text">All ({{ news_posts.size }})</span>
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="asset-hub-main">
				<section class="page-card-group learn-tag-group asset-hub-results" data-learn-tag-group id="news-posts">
					<div class="asset-hub-results-header">
						<div class="asset-hub-results-copy">
							<p class="asset-hub-filter-label">Results</p>
							<h3 data-learn-results-title>All news</h3>
							<p class="compact asset-hub-results-summary" data-tag-results>Showing {{ news_posts.size }} of {{ news_posts.size }} news posts.</p>
						</div>
					</div>
					<div class="page-card-group-heading">
						<p>Start with the newest Defold news, then narrow the list by topic or switch the date order with the shared controls in the sidebar.</p>
					</div>
					<div class="page-feature-grid page-grid-auto-fill page-grid-three page-grid-flush" data-learn-sort-grid>
						{%- for post in news_posts -%}
							{% include post_catalog_card.html post=post %}
						{%- endfor -%}
					</div>
				</section>
			</div>
		</div>
	</div>
</div>

{% include newsletter_section.html title="Get Defold news in your inbox" body="Subscribe for Defold release news, product updates, showcase highlights, and other announcements worth following. Emails are occasional and you can unsubscribe at any time." %}

{% include donors_and_partners.html %}

<script src="/js/learn-tag-filter.js"></script>
