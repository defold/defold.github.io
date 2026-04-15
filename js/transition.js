(function() {
	var transitionSelector = '.slideinleft, .slideinright, .slideinbottom, .fadein';
	var elementsToShow = document.querySelectorAll(transitionSelector);

	if (!elementsToShow.length) {
		return;
	}

	function setVisibleState(element, isVisible) {
		element.classList.toggle('is-visible', isVisible);
	}

	if ('IntersectionObserver' in window) {
		var observer = new IntersectionObserver(function(entries) {
			Array.prototype.forEach.call(entries, function(entry) {
				setVisibleState(entry.target, entry.isIntersecting || entry.intersectionRatio > 0);
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

	function updateVisibility() {
		scheduled = false;

		Array.prototype.forEach.call(elementsToShow, function(element) {
			setVisibleState(element, isElementInViewport(element));
		});
	}

	function requestVisibilityUpdate() {
		if (scheduled) {
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
