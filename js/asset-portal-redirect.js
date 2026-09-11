(() => {
	const link = document.getElementById("asset-portal-redirect");
	const target = new URL(link.href, window.location.origin);
	// Explicit filters on an old URL override that page's tag and sort defaults.
	new URLSearchParams(window.location.search).forEach((value, key) => {
		target.searchParams.set(key, value);
	});
	target.hash = window.location.hash;
	link.href = target.href;
	window.location.replace(target.href);
})();
