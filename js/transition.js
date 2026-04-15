(function() {
	var transitionSelector = '.slideinleft, .slideinright, .slideinbottom, .fadein';
	var elementsToShow = Array.prototype.slice.call(document.querySelectorAll(transitionSelector));

	if (!elementsToShow.length) {
		return;
	}

	function revealElement(element) {
		if (!element.classList.contains('is-visible')) {
			element.classList.add('is-visible');
		}
	}

	if ('IntersectionObserver' in window) {
		var remainingCount = elementsToShow.length;
		var observer = new IntersectionObserver(function(entries) {
			Array.prototype.forEach.call(entries, function(entry) {
				if (!entry.isIntersecting && entry.intersectionRatio <= 0) {
					return;
				}

				revealElement(entry.target);
				observer.unobserve(entry.target);
				remainingCount -= 1;

				if (remainingCount <= 0) {
					observer.disconnect();
				}
			});
		}, {
			threshold: 0.12,
			rootMargin: '0px 0px -8% 0px'
		});

		Array.prototype.forEach.call(elementsToShow, function(element) {
			observer.observe(element);
		});

		return;
	}

	function isElementInViewport(element) {
		var rect = element.getBoundingClientRect();
		var viewportHeight = window.innerHeight || document.documentElement.clientHeight;

		return (
			(rect.top <= 0 && rect.bottom >= 0)
			|| (rect.bottom >= viewportHeight && rect.top <= viewportHeight)
			|| (rect.top >= 0 && rect.bottom <= viewportHeight)
		);
	}

	var scheduleFrame = window.requestAnimationFrame || function(callback) {
		return window.setTimeout(callback, 1000 / 60);
	};
	var scheduled = false;
	var pendingElements = elementsToShow.slice();

	function removeFallbackListeners() {
		window.removeEventListener('load', requestVisibilityUpdate);
		window.removeEventListener('scroll', requestVisibilityUpdate);
		window.removeEventListener('resize', requestVisibilityUpdate);
		window.removeEventListener('orientationchange', requestVisibilityUpdate);
	}

	function updateVisibility() {
		scheduled = false;
		var stillPending = [];

		Array.prototype.forEach.call(pendingElements, function(element) {
			if (isElementInViewport(element)) {
				revealElement(element);
				return;
			}

			stillPending.push(element);
		});

		pendingElements = stillPending;
		if (!pendingElements.length) {
			removeFallbackListeners();
		}
	}

	function requestVisibilityUpdate() {
		if (scheduled || !pendingElements.length) {
			return;
		}

		scheduled = true;
		scheduleFrame(updateVisibility);
	}

	window.addEventListener('load', requestVisibilityUpdate);
	window.addEventListener('scroll', requestVisibilityUpdate);
	window.addEventListener('resize', requestVisibilityUpdate);
	window.addEventListener('orientationchange', requestVisibilityUpdate);

	requestVisibilityUpdate();
})();
