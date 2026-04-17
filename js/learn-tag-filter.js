(() => {
	const normalize = (value) =>
		(value || "")
			.toString()
			.toLowerCase()
			.trim();

	const toSlug = (value) =>
		normalize(value)
			.replace(/\s+/g, "-");

	const toLabel = (tag) => {
		const map = {
			"ui-art": "UI / Art",
			"two-d": "2D",
			"three-d": "3D",
			"gui": "GUI",
			"ios": "iOS"
		};
		if (map[tag]) {
			return map[tag];
		}

		return tag
			.split("-")
			.map((word) => word.charAt(0).toUpperCase() + word.slice(1))
			.join(" ");
	};

	const parseTags = (raw) =>
		(raw || "")
			.split("|")
			.map(toSlug)
			.filter(Boolean);

	const getSortLabel = (button, fallback) => {
		if (!button) {
			return fallback;
		}

		return button.dataset.learnSortLabel || fallback;
	};

	const createDefaultFilterIcon = () => {
		const siteIcon = document.createElement("span");
		siteIcon.className = "site-icon asset-hub-filter-icon";
		siteIcon.setAttribute("aria-hidden", "true");

		const octicon = document.createElement("span");
		octicon.className = "octicon";
		octicon.setAttribute("style", "fill: currentColor; zoom: 1; vertical-align: middle;");

		const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
		svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
		svg.setAttribute("width", "15");
		svg.setAttribute("height", "16");
		svg.setAttribute("viewBox", "0 0 15 16");

		const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
		path.setAttribute("fill-rule", "evenodd");
		path.setAttribute(
			"d",
			"M7.73 1.73C7.26 1.26 6.62 1 5.96 1H3.5C2.13 1 1 2.13 1 3.5v2.47c0 .66.27 1.3.73 1.77l6.06 6.06c.39.39 1.02.39 1.41 0l4.59-4.59a.996.996 0 0 0 0-1.41L7.73 1.73zM2.38 7.09c-.31-.3-.47-.7-.47-1.13V3.5c0-.88.72-1.59 1.59-1.59h2.47c.42 0 .83.16 1.13.47l6.14 6.13-4.73 4.73-6.13-6.15zM3.01 3h2v2H3V3h.01z"
		);

		svg.appendChild(path);
		octicon.appendChild(svg);
		siteIcon.appendChild(octicon);
		return siteIcon;
	};

	const createFilterText = (text) => {
		const label = document.createElement("span");
		label.className = "asset-hub-filter-text";
		label.textContent = text;
		return label;
	};

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

	const buildTagStats = (items, excludedTags) => {
		const counts = new Map();
		items.forEach((item) => {
			parseTags(item.dataset.learnTags).forEach((tag) => {
				if (excludedTags.has(tag)) {
					return;
				}
				counts.set(tag, (counts.get(tag) || 0) + 1);
			});
		});
		return counts;
	};

	const updateResultLabel = (resultEl, visibleCount, totalCount, selectedTag, filterSingular, resultItems, rawQuery) => {
		if (!resultEl) {
			return;
		}

		if (!visibleCount) {
			if (selectedTag !== "all" && rawQuery) {
				resultEl.textContent = `No ${resultItems} match the current ${filterSingular} and search.`;
				return;
			}

			if (selectedTag !== "all") {
				resultEl.textContent = `No ${resultItems} match the current ${filterSingular}.`;
				return;
			}

			if (rawQuery) {
				resultEl.textContent = `No ${resultItems} match the current search.`;
				return;
			}
		}

		if (selectedTag === "all" && !rawQuery) {
			resultEl.textContent = `Showing ${visibleCount} of ${totalCount} ${resultItems}.`;
			return;
		}

		const parts = [`Showing ${visibleCount} of ${totalCount} ${resultItems}`];
		if (selectedTag !== "all") {
			parts.push(`for ${filterSingular}: ${toLabel(selectedTag)}`);
		}
		if (rawQuery) {
			parts.push(`matching "${rawQuery}"`);
		}
		resultEl.textContent = `${parts.join(" ")}.`;
	};

	document.addEventListener("DOMContentLoaded", () => {
		const catalogs = Array.from(document.querySelectorAll("[data-learn-tag-catalog]"));
		if (!catalogs.length) {
			return;
		}

		catalogs.forEach((catalog) => {
			const filterRoot = catalog.querySelector("[data-learn-tag-filter]");
			const chipRow = catalog.querySelector("[data-tag-chip-row]");
			const resultEl = catalog.querySelector("[data-tag-results]");
			const resultTitleEl = catalog.querySelector("[data-learn-results-title]");
			const searchInput = catalog.querySelector("[data-learn-search]");
			const groups = Array.from(catalog.querySelectorAll("[data-learn-tag-group]"));
			const items = Array.from(catalog.querySelectorAll("[data-learn-tag-item='true']"));
			const sortButtons = Array.from(catalog.querySelectorAll("[data-learn-sort]"));
			const sortGrid = catalog.querySelector("[data-learn-sort-grid]");
			const filterToggle = catalog.querySelector("[data-asset-filter-toggle]");
			const filterPanel = catalog.querySelector("[data-asset-filter-panel]");
			if (!filterRoot || !chipRow || !items.length) {
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

			const excludedTags = new Set(parseTags(filterRoot.dataset.filterExcludedTags));
			const tagStats = buildTagStats(items, excludedTags);
			const sortedTags = Array.from(tagStats.entries())
				.sort((a, b) => toLabel(a[0]).localeCompare(toLabel(b[0])))
				.map(([tag]) => tag);

			const totalCount = items.length;
			const filterSingular = filterRoot.dataset.filterSingular || "tag";
			const resultItems = filterRoot.dataset.resultItems || "resources";
			const defaultTitle = catalog.dataset.defaultTitle || `All ${resultItems}`;
			let selectedTag = "all";
			let sortOrder = normalize(catalog.dataset.initialSort) || (sortButtons[0]?.dataset.learnSort || "");
			let requestedTag = "";
			const preRenderedChips = Array.from(chipRow.querySelectorAll(".learn-tag-chip"));
			const hasPreRenderedTagChips = preRenderedChips.some((chip) => (chip.dataset.tag || "") !== "all");
			const forceGeneratedTagChips = filterRoot.dataset.forceGeneratedChips === "true";

			try {
				const params = new URLSearchParams(window.location.search);
				requestedTag = toSlug(
					params.get("tag") ||
					params.get(filterSingular) ||
					window.location.hash.replace(/^#/, "")
				);
			} catch (error) {
				requestedTag = toSlug(window.location.hash.replace(/^#/, ""));
			}

			if (requestedTag && (requestedTag === "all" || tagStats.has(requestedTag))) {
				selectedTag = requestedTag;
			}

			const sortItems = () => {
				if (!sortGrid || !sortButtons.length) {
					return;
				}

				const ordered = [...items].sort((a, b) => {
					if (sortOrder === "date-asc" || sortOrder === "date-desc") {
						const dateA = Number.parseInt(a.dataset.learnDate || "0", 10);
						const dateB = Number.parseInt(b.dataset.learnDate || "0", 10);
						if (dateA !== dateB) {
							return sortOrder === "date-asc" ? dateA - dateB : dateB - dateA;
						}
					}

					return (a.dataset.learnTitle || "").localeCompare(b.dataset.learnTitle || "");
				});

				ordered.forEach((item) => sortGrid.appendChild(item));
			};

			const renderChips = () => {
				if (hasPreRenderedTagChips && !forceGeneratedTagChips) {
					return;
				}

				chipRow.innerHTML = "";
				const allChip = document.createElement("button");
				allChip.type = "button";
				allChip.className = "learn-tag-chip filter";
				allChip.dataset.tag = "all";
				allChip.appendChild(createDefaultFilterIcon());
				allChip.appendChild(createFilterText(`All (${totalCount})`));
				chipRow.appendChild(allChip);

				sortedTags.forEach((tag) => {
					const chip = document.createElement("button");
					chip.type = "button";
					chip.className = "learn-tag-chip filter";
					chip.dataset.tag = tag;
					chip.appendChild(createDefaultFilterIcon());
					chip.appendChild(createFilterText(`${toLabel(tag)} (${tagStats.get(tag)})`));
					chipRow.appendChild(chip);
				});
			};

			const applyFilter = () => {
				sortItems();
				const rawQuery = (searchInput?.value || "").trim();
				const query = normalize(rawQuery);
				let visibleCount = 0;

				items.forEach((item) => {
					const tags = parseTags(item.dataset.learnTags);
					const title = normalize(item.dataset.learnTitle);
					const description = normalize(item.dataset.learnDescription);
					const author = normalize(item.dataset.learnAuthor);
					const matchesTag = selectedTag === "all" || tags.includes(selectedTag);
					const matchesQuery = !query || title.includes(query) || description.includes(query) || author.includes(query);
					const visible = matchesTag && matchesQuery;
					item.classList.toggle("learn-tag-hidden", !visible);
					if (visible) {
						visibleCount += 1;
					}
				});

				groups.forEach((group) => {
					const hasVisibleItem = Boolean(group.querySelector("[data-learn-tag-item='true']:not(.learn-tag-hidden)"));
					group.classList.toggle("learn-tag-hidden", !hasVisibleItem);
				});

				chipRow.querySelectorAll(".learn-tag-chip").forEach((chip) => {
					const active = chip.dataset.tag === selectedTag;
					chip.classList.toggle("active", active);
					chip.setAttribute("aria-pressed", active ? "true" : "false");
				});

				sortButtons.forEach((button) => {
					const active = button.dataset.learnSort === sortOrder;
					button.classList.toggle("active", active);
					button.setAttribute("aria-pressed", active ? "true" : "false");
				});

				if (resultTitleEl) {
					if (selectedTag === "all") {
						resultTitleEl.textContent = defaultTitle;
					} else {
						resultTitleEl.textContent = toLabel(selectedTag);
					}
				}

				updateResultLabel(resultEl, visibleCount, totalCount, selectedTag, filterSingular, resultItems, rawQuery);
			};

			renderChips();
			chipRow.addEventListener("click", (event) => {
				const chip = event.target.closest(".learn-tag-chip");
				if (!chip) {
					return;
				}
				selectedTag = chip.dataset.tag || "all";
				applyFilter();

				trackEvent("learn_tag_filter_select", {
					tag: selectedTag,
					sort_order: sortOrder,
					visible_resources: catalog.querySelectorAll("[data-learn-tag-item='true']:not(.learn-tag-hidden)").length,
					total_resources: totalCount
				});
			});

			sortButtons.forEach((button) => {
				button.addEventListener("click", () => {
					sortOrder = button.dataset.learnSort || sortOrder;
					applyFilter();

					trackEvent("learn_tag_sort_select", {
						tag: selectedTag,
						sort_order: getSortLabel(button, sortOrder).toLowerCase().replace(/\s+/g, "_"),
						visible_resources: catalog.querySelectorAll("[data-learn-tag-item='true']:not(.learn-tag-hidden)").length,
						total_resources: totalCount
					});
				});
			});

			if (searchInput) {
				const onInput = () => applyFilter();
				searchInput.addEventListener("input", onInput);
				searchInput.addEventListener("propertychange", onInput);
			}

			applyFilter();
		});
	});
})();
