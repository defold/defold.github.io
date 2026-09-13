const { createChannelFilter, channelLabel } = await import(`./pagefind-channel-filter.js${new URL(import.meta.url).search}`);

const initSearch = () => {
	const root = document.querySelector("#pagefind-search");
	const channelElement = document.querySelector("#search-channel");
	const urlParams = new URLSearchParams(window.location.search);
	let currentQuery = urlParams.get("q") || "";

	const updateUrl = () => {
		const url = new URL(window.location.href);
		if (currentQuery.trim()) url.searchParams.set("q", currentQuery.trim());
		else url.searchParams.delete("q");
		url.searchParams.set("channel", channelFilter.getValue());
		window.history.replaceState(null, "", url);
	};

	const channelFilter = createChannelFilter(channelElement, (channel) => {
		// Preserve the section selections when changing the API channel.
		const filters = { "API channel": [channelLabel(channel)] };
		root.querySelectorAll('input[type="checkbox"]:checked').forEach((input) => {
			if (input.name !== "API channel") (filters[input.name] ||= []).push(input.value);
		});
		search.triggerFilters(filters);
		updateUrl();
	});
	channelFilter.setValue(urlParams.get("channel"));
	const updateQuery = (term) => {
		currentQuery = term;
		channelFilter.updateCounts(term);
		updateUrl();
	};

	const normalizeSearchTerm = (term) => (term || "")
		.toLowerCase()
		.trim()
		.replace(/[\.`~!@#\$%\^&\*\(\)\{\}\[\]\\\|:;'",<>\/\?\-]/g, "")
		.replace(/\s{2,}/g, " ")
		.trim();

	const boostExactSubResultMatch = (result) => {
		const normalizedQuery = normalizeSearchTerm(currentQuery);
		if (!normalizedQuery || !Array.isArray(result.sub_results)) return result;

		for (const subResult of result.sub_results) {
			if (normalizeSearchTerm(subResult.title) !== normalizedQuery) continue;
			const locations = Array.isArray(subResult.locations) ? subResult.locations : [];
			const lastLocation = locations.length ? locations[locations.length - 1] : 0;
			subResult.locations = locations.concat(Array(8).fill(lastLocation));
			break;
		}
		return result;
	};

	const search = new PagefindUI({
		element: "#pagefind-search",
		pageSize: 10,
		showSubResults: true,
		showImages: false,
		excerptLength: 25,
		processResult: boostExactSubResultMatch,
		processTerm: (term) => {
			updateQuery(term);
			return term;
		},
		resetStyles: false,
		showEmptyFilters: true,
		openFilters: ["section"]
	});

	// Pagefind creates and removes its filter panel as the search state changes.
	const placeChannelFilter = () => {
		const panel = root.querySelector(".pagefind-ui__filter-panel");
		if (panel && channelElement.parentElement !== panel) {
			panel.querySelector("legend").after(channelElement);
			channelElement.hidden = false;
		}
	};
	new MutationObserver(placeChannelFilter).observe(root, { childList: true, subtree: true });
	placeChannelFilter();

	root.addEventListener("input", (event) => {
		if (event.target.matches('input[type="text"]')) {
			updateQuery(event.target.value);
		}
	});
	// Pagefind's Clear button does not dispatch an input event.
	root.addEventListener("click", (event) => {
		if (event.target.closest(".pagefind-ui__search-clear")) updateQuery("");
	});

	search.triggerFilters({ "API channel": [channelLabel(channelFilter.getValue())] });
	channelFilter.updateCounts(currentQuery);
	if (currentQuery) search.triggerSearch(currentQuery);
};

if (document.readyState === "loading") {
	document.addEventListener("DOMContentLoaded", initSearch, { once: true });
} else {
	initSearch();
}
