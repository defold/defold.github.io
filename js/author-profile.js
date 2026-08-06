(() => {
	const normalize = (value) =>
		(value || "")
			.toString()
			.toLowerCase()
			.trim();

	const allowedTypes = new Set(["all", "assets", "examples"]);

	document.addEventListener("DOMContentLoaded", () => {
		const catalogs = Array.from(document.querySelectorAll("[data-author-catalog]"));
		catalogs.forEach((catalog) => {
			const items = Array.from(catalog.querySelectorAll("[data-author-contribution='true']"));
			const filterButtons = Array.from(document.querySelectorAll("[data-author-filter]"));
			const searchInput = catalog.querySelector("[data-author-search]");
			const resultsTitle = catalog.querySelector("[data-author-results-title]");
			const resultsSummary = catalog.querySelector("[data-author-results-summary]");
			const emptyMessage = catalog.querySelector("[data-author-empty]");

			if (!items.length || !filterButtons.length) {
				return;
			}

			let selectedType = "all";

			const readUrlState = () => {
				const params = new URLSearchParams(window.location.search);
				const requestedType = normalize(params.get("type"));
				selectedType = allowedTypes.has(requestedType) ? requestedType : "all";
				if (selectedType !== "all" && !items.some((item) => item.dataset.authorContributionType === selectedType)) {
					selectedType = "all";
				}
				if (searchInput) {
					searchInput.value = params.get("q") || "";
				}
			};

			const syncUrl = () => {
				const params = new URLSearchParams(window.location.search);
				const query = (searchInput?.value || "").trim();

				if (selectedType === "all") {
					params.delete("type");
				} else {
					params.set("type", selectedType);
				}

				if (query) {
					params.set("q", query);
				} else {
					params.delete("q");
				}

				const search = params.toString();
				const nextUrl = `${window.location.pathname}${search ? `?${search}` : ""}${window.location.hash}`;
				window.history.replaceState({}, "", nextUrl);
			};

			const itemSearchText = (item) =>
				normalize([
					item.dataset.name,
					item.dataset.description,
					item.dataset.learnTitle,
					item.dataset.learnDescription,
					item.dataset.learnAuthor,
					item.textContent
				].join(" "));

			const applyState = () => {
				const query = normalize(searchInput?.value);
				let visibleCount = 0;

				items.forEach((item) => {
					const matchesType = selectedType === "all" || item.dataset.authorContributionType === selectedType;
					const matchesQuery = !query || itemSearchText(item).includes(query);
					const visible = matchesType && matchesQuery;
					item.hidden = !visible;
					item.setAttribute("aria-hidden", visible ? "false" : "true");
					if (visible) {
						visibleCount += 1;
					}
				});

				filterButtons.forEach((button) => {
					const active = button.dataset.authorFilter === selectedType;
					button.classList.toggle("active", active);
					button.setAttribute("aria-pressed", active ? "true" : "false");
				});

				const label = selectedType === "assets"
					? "Assets"
					: selectedType === "examples"
						? "Examples"
						: "All contributions";
				if (resultsTitle) {
					resultsTitle.textContent = label;
				}
				if (resultsSummary) {
					const filteredTotal = selectedType === "all"
						? items.length
						: items.filter((item) => item.dataset.authorContributionType === selectedType).length;
					const itemLabel = selectedType === "all" ? "contributions" : selectedType;
					const querySuffix = query ? ` matching “${(searchInput?.value || "").trim()}”` : "";
					resultsSummary.textContent = `Showing ${visibleCount} of ${filteredTotal} ${itemLabel}${querySuffix}.`;
				}
				if (emptyMessage) {
					emptyMessage.hidden = visibleCount !== 0;
					emptyMessage.textContent = query
						? `No ${label.toLowerCase()} match “${(searchInput?.value || "").trim()}”.`
						: `No ${label.toLowerCase()} are available.`;
				}
			};

			filterButtons.forEach((button) => {
				button.addEventListener("click", () => {
					const requestedType = normalize(button.dataset.authorFilter);
					if (!allowedTypes.has(requestedType)) {
						return;
					}
					selectedType = requestedType;
					applyState();
					syncUrl();
				});
			});

			if (searchInput) {
				searchInput.addEventListener("input", () => {
					applyState();
					syncUrl();
				});
			}

			window.addEventListener("popstate", () => {
				readUrlState();
				applyState();
			});

			readUrlState();
			applyState();
		});
	});
})();
