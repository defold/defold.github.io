(() => {
	const debounceMs = 180;

	const getInstance = (instanceName) => {
		const components = window.PagefindComponents;
		const manager = components && components.getInstanceManager && components.getInstanceManager();
		return manager && manager.getInstance(instanceName);
	};

	const buildSearchUrl = (term) => {
		const params = new URLSearchParams();
		if (term) {
			params.set("q", term);
		}
		const query = params.toString();
		return query ? `/search?${query}` : "/search";
	};

	const initSearch = (form) => {
		if (form.dataset.pagefindNavSearchReady === "true") {
			return true;
		}

		const instanceName = form.getAttribute("data-pagefind-search-instance");
		const input = form.querySelector("[data-pagefind-nav-search-input]");
		const panel = form.querySelector("[data-pagefind-nav-search-panel]");
		const allResultsLink = form.querySelector("[data-pagefind-nav-search-all-results]");
		const instance = getInstance(instanceName);

		if (!input || !panel || !instance) {
			return false;
		}

		form.dataset.pagefindNavSearchReady = "true";

		input.inputEl = input;
		input.setAttribute("autocomplete", "off");
		input.setAttribute("aria-controls", panel.id);
		input.setAttribute("aria-expanded", "false");
		instance.registerInput(input, { keyboardNavigation: true });

		let searchTimer = null;

		const getTerm = () => input.value.trim();

		const syncFixedPanelPosition = () => {
			if (!form.hasAttribute("data-pagefind-fixed-panel") || panel.hidden) {
				return;
			}

			const rect = input.getBoundingClientRect();
			const viewportPadding = 16;
			const panelWidth = Math.min(448, window.innerWidth - viewportPadding * 2);
			const align = form.getAttribute("data-pagefind-panel-align") || "left";
			const alignedLeft = align === "right" ? rect.right - panelWidth : rect.left;
			const maxLeft = window.innerWidth - panelWidth - viewportPadding;
			const left = Math.max(viewportPadding, Math.min(alignedLeft, maxLeft));

			panel.style.position = "fixed";
			panel.style.top = `${Math.round(rect.bottom + 8)}px`;
			panel.style.left = `${Math.round(left)}px`;
			panel.style.right = "auto";
			panel.style.width = `${Math.round(panelWidth)}px`;
			panel.style.maxWidth = `calc(100vw - ${viewportPadding * 2}px)`;
		};

		const setPanelOpen = (isOpen) => {
			panel.hidden = !isOpen;
			input.setAttribute("aria-expanded", isOpen ? "true" : "false");
			form.classList.toggle("pagefind-nav-search-open", isOpen);
			if (isOpen) {
				syncFixedPanelPosition();
			}
		};

		const updateAllResultsLink = () => {
			if (allResultsLink) {
				allResultsLink.href = buildSearchUrl(getTerm());
			}
		};

		const triggerSearch = () => {
			const term = getTerm();
			updateAllResultsLink();

			if (!term) {
				instance.triggerSearch("");
				setPanelOpen(false);
				return;
			}

			setPanelOpen(true);
			instance.triggerSearch(term);
		};

		const queueSearch = () => {
			updateAllResultsLink();
			window.clearTimeout(searchTimer);
			searchTimer = window.setTimeout(triggerSearch, debounceMs);
		};

		input.addEventListener("input", queueSearch);

		input.addEventListener("focus", () => {
			instance.triggerLoad();
			updateAllResultsLink();
			if (getTerm()) {
				setPanelOpen(true);
			}
		});

		input.addEventListener("keydown", (event) => {
			if (event.key === "ArrowDown" && getTerm()) {
				event.preventDefault();
				setPanelOpen(true);
				instance.focusNextResults(input);
			}

			if (event.key === "Escape") {
				window.clearTimeout(searchTimer);
				setPanelOpen(false);
			}
		});

		document.addEventListener("click", (event) => {
			if (!form.contains(event.target)) {
				setPanelOpen(false);
			}
		});

		window.addEventListener("resize", syncFixedPanelPosition, { passive: true });
		document.addEventListener("scroll", syncFixedPanelPosition, { passive: true, capture: true });

		form.addEventListener("submit", () => {
			updateAllResultsLink();
		});

		return true;
	};

	const init = () => {
		return Array.from(document.querySelectorAll("[data-pagefind-nav-search]")).every(initSearch);
	};

	const initWhenReady = (attemptsLeft = 20) => {
		if (!window.PagefindComponents) {
			if (attemptsLeft > 0) {
				window.setTimeout(() => initWhenReady(attemptsLeft - 1), 50);
			}
			return;
		}

		if (window.customElements && window.customElements.whenDefined && !window.customElements.get("pagefind-results")) {
			window.customElements.whenDefined("pagefind-results").then(() => initWhenReady(attemptsLeft));
			return;
		}

		if (!init() && attemptsLeft > 0) {
			window.setTimeout(() => initWhenReady(attemptsLeft - 1), 50);
		}
	};

	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", () => initWhenReady(), { once: true });
	} else {
		initWhenReady();
	}
})();
