(() => {
	const links = Array.from(document.querySelectorAll("[data-api-channel]"));

	const preserveLocation = () => {
		for (const link of links) {
			const target = new URL(link.href);
			target.search = window.location.search;
			target.hash = link.dataset.preserveFragment === "true" ? window.location.hash : "";
			link.href = target.href;
		}
	};

	preserveLocation();
	window.addEventListener("hashchange", preserveLocation);
})();
