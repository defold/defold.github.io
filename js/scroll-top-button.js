(function () {
	function initScrollTopButton() {
		var buttons = document.querySelectorAll("[data-scroll-top]");
		if (!buttons.length) {
			return;
		}

		var scheduled = false;
		var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
		var topTarget = document.getElementById("page");

		function updateVisibility() {
			scheduled = false;
			var scrollTop = window.pageYOffset || document.documentElement.scrollTop || 0;
			var shouldShow = scrollTop > window.innerHeight;

			buttons.forEach(function (button) {
				button.classList.toggle("is-visible", shouldShow);
			});
		}

		function scheduleUpdate() {
			if (scheduled) {
				return;
			}
			scheduled = true;
			window.requestAnimationFrame(updateVisibility);
		}

		buttons.forEach(function (button) {
			button.addEventListener("click", function () {
				if (topTarget) {
					topTarget.scrollIntoView({
						behavior: reducedMotion.matches ? "auto" : "smooth",
						block: "start"
					});
					return;
				}

				window.scrollTo({
					top: 0,
					behavior: reducedMotion.matches ? "auto" : "smooth"
				});
			});
		});

		updateVisibility();
		window.addEventListener("scroll", scheduleUpdate, { passive: true });
		window.addEventListener("resize", scheduleUpdate, { passive: true });
	}

	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", initScrollTopButton, { once: true });
	} else {
		initScrollTopButton();
	}
})();
