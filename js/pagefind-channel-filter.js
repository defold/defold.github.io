export const channelLabel = (channel) => channel[0].toUpperCase() + channel.slice(1);

let countIndex;
let lastQuery;
let lastCounts;

const getCountIndex = () => {
	if (!countIndex) {
		countIndex = import("/_pagefind/pagefind.js").then(async (pagefind) => {
			const index = pagefind.createInstance({});
			await index.filters();
			return index;
		}).catch((error) => {
			countIndex = null;
			throw error;
		});
	}
	return countIndex;
};

const getApiCounts = (query) => {
	if (query !== lastQuery || !lastCounts) {
		lastQuery = query;
		// Count every channel within the API section, independently of the selected filters.
		const request = getCountIndex()
			.then((index) => index.search(query || null, { filters: { section: "API" } }))
			.then((result) => result.filters["API channel"] || {});
		lastCounts = request;
		request.catch(() => {
			if (lastCounts === request) lastCounts = null;
		});
	}
	return lastCounts;
};

export const createChannelFilter = (element, onChange) => {
	const inputs = [...element.querySelectorAll('input[name="channel"]')];
	const getValue = () => inputs.find((input) => input.checked).value;
	const setValue = (value) => {
		const channel = inputs.some((input) => input.value === value) ? value : "stable";
		inputs.forEach((input) => { input.checked = input.value === channel; });
	};

	element.addEventListener("change", (event) => {
		if (inputs.includes(event.target) && event.target.checked) onChange(getValue());
	});

	let currentQuery;
	let requestId = 0;
	let timer;
	const renderCounts = (counts, placeholder = "—") => {
		inputs.forEach((input) => {
			const count = counts ? counts[channelLabel(input.value)] || 0 : placeholder;
			input.parentElement.querySelector("[data-pagefind-channel-count]").textContent = `(${count})`;
		});
	};

	const updateCounts = (term) => {
		const query = term.trim();
		if (query === currentQuery) return;
		currentQuery = query;
		const id = ++requestId;
		window.clearTimeout(timer);
		renderCounts(null, "…");
		element.setAttribute("aria-busy", "true");
		timer = window.setTimeout(async () => {
			try {
				const counts = await getApiCounts(query);
				if (id === requestId) renderCounts(counts);
			} catch (error) {
				if (id === requestId) {
					renderCounts(null);
					currentQuery = undefined;
				}
				console.warn("Could not load API channel counts", error);
			} finally {
				if (id === requestId) element.removeAttribute("aria-busy");
			}
		}, 180);
	};

	return { getValue, setValue, updateCounts };
};
