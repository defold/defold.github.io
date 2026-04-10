(() => {
	const normalize = (value) =>
		(value || "")
			.toString()
			.toLowerCase()
			.trim();

	const normalizeTag = (value) => {
		const normalized = normalize(value);
		const aliases = {
			fonts: "text",
			meshcomponent: "mesh",
			templateprojects: "template",
			templates: "template"
		};

		return aliases[normalized.replace(/\s+/g, "")] || normalized.replace(/\s+/g, "");
	};

	const parseTags = (value) =>
		(value || "")
			.split("|")
			.map(normalizeTag)
			.filter(Boolean);

	const trackEvent = (name, params) => {
		const payload = {
			...(params || {}),
			page_path: window.location.pathname
		};

		if (typeof window.gtag === "function") {
			window.gtag("event", name, payload);
			return;
		}

		if (Array.isArray(window.dataLayer)) {
			window.dataLayer.push({ event: name, ...payload });
		}
	};

	const getTagLabel = (button, fallback) => {
		if (!button) {
			return fallback;
		}

		return button.dataset.assetTagLabel || fallback;
	};

	document.addEventListener("DOMContentLoaded", () => {
		const catalogs = Array.from(document.querySelectorAll("[data-asset-catalog]"));
		if (!catalogs.length) {
			return;
		}

		catalogs.forEach((catalog) => {
			const filterToggle = catalog.querySelector("[data-asset-filter-toggle]");
			const filterPanel = catalog.querySelector("[data-asset-filter-panel]");
			const grid = catalog.querySelector("[data-asset-grid]");
			const searchInput = catalog.querySelector("[data-asset-search]");
			const titleEl = catalog.querySelector("[data-asset-results-title]");
			const summaryEl = catalog.querySelector("[data-asset-results-summary]");
			const items = Array.from(catalog.querySelectorAll("[data-asset-item='true']"));
			const tagButtons = Array.from(catalog.querySelectorAll("[data-asset-tag]"));
			const sortButtons = Array.from(catalog.querySelectorAll("[data-asset-sort]"));

			if (!grid || !items.length || !tagButtons.length || !sortButtons.length) {
				return;
			}

			if (filterToggle && filterPanel) {
				const desktopQuery = window.matchMedia("(min-width: 981px)");
				let mobileExpanded = false;

				const syncFilterPanel = () => {
					if (desktopQuery.matches) {
						filterPanel.hidden = false;
						filterToggle.setAttribute("aria-expanded", "true");
						return;
					}

					filterPanel.hidden = !mobileExpanded;
					filterToggle.setAttribute("aria-expanded", mobileExpanded ? "true" : "false");
				};

				filterToggle.addEventListener("click", () => {
					if (desktopQuery.matches) {
						return;
					}

					mobileExpanded = !mobileExpanded;
					syncFilterPanel();
				});

				if (typeof desktopQuery.addEventListener === "function") {
					desktopQuery.addEventListener("change", syncFilterPanel);
				} else if (typeof desktopQuery.addListener === "function") {
					desktopQuery.addListener(syncFilterPanel);
				}

				syncFilterPanel();
			}

			const totalCount = items.length;
			const defaultTitle = catalog.dataset.defaultTitle || "All assets";
			let selectedTag = normalizeTag(catalog.dataset.initialTag) || "all";
			let sortOrder = normalize(catalog.dataset.initialSort) === "timestamp" ? "timestamp" : "stars";

			if (!tagButtons.some((button) => button.dataset.assetTag === selectedTag)) {
				selectedTag = "all";
			}

			const sortItems = () => {
				const ordered = [...items].sort((a, b) => {
					const metricA = Number.parseFloat(a.dataset[`asset${sortOrder === "timestamp" ? "Timestamp" : "Stars"}`] || "0");
					const metricB = Number.parseFloat(b.dataset[`asset${sortOrder === "timestamp" ? "Timestamp" : "Stars"}`] || "0");
					if (metricA !== metricB) {
						return metricB - metricA;
					}

					return (a.dataset.name || "").localeCompare(b.dataset.name || "");
				});

				ordered.forEach((item) => grid.appendChild(item));
			};

			const updateSummary = (visibleCount) => {
				if (!summaryEl) {
					return;
				}

				if (!visibleCount) {
					summaryEl.textContent = "No assets match the current tag and search.";
					return;
				}

				const parts = [`Showing ${visibleCount} of ${totalCount} assets`];
				if (selectedTag !== "all") {
					const activeTagButton = tagButtons.find((button) => button.dataset.assetTag === selectedTag);
					parts.push(`for ${getTagLabel(activeTagButton, defaultTitle)}`);
				}

				const rawQuery = (searchInput?.value || "").trim();
				if (rawQuery) {
					parts.push(`matching "${rawQuery}"`);
				}

				summaryEl.textContent = `${parts.join(" ")}.`;
			};

			const applyState = () => {
				sortItems();

				const rawQuery = (searchInput?.value || "").trim();
				const query = normalize(rawQuery);
				let visibleCount = 0;

				items.forEach((item) => {
					const tags = parseTags(item.dataset.assetTags);
					const matchesTag = selectedTag === "all" || tags.includes(selectedTag);
					const name = normalize(item.dataset.name);
					const description = normalize(item.dataset.description);
					const matchesQuery = !query || name.includes(query) || description.includes(query);
					const visible = matchesTag && matchesQuery;
					item.classList.toggle("asset-hub-hidden", !visible);
					if (visible) {
						visibleCount += 1;
					}
				});

				tagButtons.forEach((button) => {
					const active = button.dataset.assetTag === selectedTag;
					button.classList.toggle("active", active);
					button.setAttribute("aria-pressed", active ? "true" : "false");
				});

				sortButtons.forEach((button) => {
					const active = button.dataset.assetSort === sortOrder;
					button.classList.toggle("active", active);
					button.setAttribute("aria-pressed", active ? "true" : "false");
				});

				if (titleEl) {
					if (selectedTag === "all") {
						titleEl.textContent = defaultTitle;
					} else {
						const activeTagButton = tagButtons.find((button) => button.dataset.assetTag === selectedTag);
						titleEl.textContent = getTagLabel(activeTagButton, defaultTitle);
					}
				}

				updateSummary(visibleCount);
			};

			tagButtons.forEach((button) => {
				button.addEventListener("click", () => {
					selectedTag = normalizeTag(button.dataset.assetTag) || "all";
					applyState();
					trackEvent("asset_portal_tag_filter_select", {
						tag: selectedTag,
						sort_order: sortOrder
					});
				});
			});

			sortButtons.forEach((button) => {
				button.addEventListener("click", () => {
					sortOrder = button.dataset.assetSort === "timestamp" ? "timestamp" : "stars";
					applyState();
					trackEvent("asset_portal_sort_select", {
						tag: selectedTag,
						sort_order: sortOrder
					});
				});
			});

			if (searchInput) {
				const onInput = () => applyState();
				searchInput.addEventListener("input", onInput);
				searchInput.addEventListener("propertychange", onInput);
			}

			applyState();
		});
	});
})();
