(function () {
	function initStickyNavOffset() {
		var page = document.getElementById("page");
		if (!page) {
			return;
		}

		var topNav = page.querySelector(".nav.nav-floating, .nav.nav-solid");
		var secondaryNav = page.querySelector(".nav.learn");
		if (!topNav || !secondaryNav) {
			return;
		}

		var scheduled = false;

		function updateOffset() {
			scheduled = false;
			var topNavHeight = Math.ceil(topNav.getBoundingClientRect().height);
			document.documentElement.style.setProperty("--topnav-sticky-offset", topNavHeight + "px");
		}

		function scheduleUpdate() {
			if (scheduled) {
				return;
			}
			scheduled = true;
			window.requestAnimationFrame(updateOffset);
		}

		scheduleUpdate();
		window.addEventListener("load", scheduleUpdate, { passive: true });
		window.addEventListener("resize", scheduleUpdate, { passive: true });

		if ("ResizeObserver" in window) {
			var resizeObserver = new ResizeObserver(scheduleUpdate);
			resizeObserver.observe(topNav);
		}

		var menuDetails = topNav.querySelectorAll("details");
		menuDetails.forEach(function (details) {
			details.addEventListener("toggle", scheduleUpdate);
		});
	}

	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", initStickyNavOffset, { once: true });
	} else {
		initStickyNavOffset();
	}
})();
