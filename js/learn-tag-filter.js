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

	const updateResultLabel = (resultEl, visibleCount, totalCount, selectedTag, filterSingular, resultItems) => {
		if (!resultEl) {
			return;
		}

		if (selectedTag === "all") {
			resultEl.textContent = `Showing ${visibleCount} of ${totalCount} ${resultItems}.`;
			return;
		}

		resultEl.textContent = `Showing ${visibleCount} of ${totalCount} ${resultItems} for ${filterSingular}: ${toLabel(selectedTag)}.`;
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
			const groups = Array.from(catalog.querySelectorAll("[data-learn-tag-group]"));
			const items = Array.from(catalog.querySelectorAll("[data-learn-tag-item='true']"));
			const sortButtons = Array.from(catalog.querySelectorAll("[data-learn-sort]"));
			const sortGrid = catalog.querySelector("[data-learn-sort-grid]");
			if (!filterRoot || !chipRow || !items.length) {
				return;
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
				chipRow.innerHTML = "";
				const allChip = document.createElement("button");
				allChip.type = "button";
				allChip.className = "learn-tag-chip filter";
				allChip.dataset.tag = "all";
				allChip.textContent = `All (${totalCount})`;
				chipRow.appendChild(allChip);

				sortedTags.forEach((tag) => {
					const chip = document.createElement("button");
					chip.type = "button";
					chip.className = "learn-tag-chip filter";
					chip.dataset.tag = tag;
					chip.textContent = `${toLabel(tag)} (${tagStats.get(tag)})`;
					chipRow.appendChild(chip);
				});
			};

			const applyFilter = () => {
				sortItems();
				let visibleCount = 0;

				items.forEach((item) => {
					const tags = parseTags(item.dataset.learnTags);
					const visible = selectedTag === "all" || tags.includes(selectedTag);
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

				updateResultLabel(resultEl, visibleCount, totalCount, selectedTag, filterSingular, resultItems);
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

			applyFilter();
		});
	});
})();
