(function() {
	function initFrontpageCarousel() {
		const rawGames = Array.isArray(window.frontpageGames) ? window.frontpageGames : [];
		if (rawGames.length === 0) {
			return;
		}

		const featuredIds = Array.isArray(window.frontpageFeaturedGameIds)
			? window.frontpageFeaturedGameIds
			: [];

		const config = window.frontpageCarouselConfig || {};
		const maxGames = Math.max(1, Number(config.maxGames) || 8);
		const intervalMs = Math.max(1000, Number(config.intervalMs) || 10000);

		const featuredGames = [];
		const seenIds = new Set();
		featuredIds.forEach(function(gameId) {
			if (!gameId || seenIds.has(gameId)) {
				return;
			}
			const game = rawGames.find(function(candidate) {
				return candidate.id === gameId;
			});
			if (game) {
				featuredGames.push(game);
				seenIds.add(gameId);
			}
		});

		const sourceGames = featuredGames.length > 0 ? featuredGames : rawGames;
		const games = sourceGames.slice(0, maxGames);

		const carousel = document.getElementById('frontpage-showcase-carousel');
		const dotsContainer = document.getElementById('game-carousel-dots');
		if (!carousel || !dotsContainer) {
			return;
		}

		let currentIndex = 0;
		let rotationTimer = null;
		let isTransitioning = false;
		let slides = [];
		let carouselInViewport = true;
		let pageVisible = !document.hidden;

		function getImageSrc(game) {
			return '/images/games/' + game.image;
		}

		function trackImpression(game) {
			if (typeof gtag === 'undefined') {
				return;
			}
			gtag('event', 'game_impression', {
				'game_id': game.id,
				'source_location': 'frontpage_hero'
			});
		}

		function bindBannerClick(game) {
			const slide = slides[currentIndex];
			if (!slide) {
				return;
			}
			slide.onclick = function() {
				if (typeof gtag === 'undefined') {
					return;
				}
				gtag('event', 'game_click', {
					'game_id': game.id,
					'source_location': 'frontpage_banner'
				});
			};
		}

		function canRotate() {
			return games.length > 1 && carouselInViewport && pageVisible;
		}

		function stopAutoRotation() {
			if (rotationTimer) {
				clearInterval(rotationTimer);
				rotationTimer = null;
			}
		}

		function startAutoRotation() {
			if (rotationTimer || !canRotate()) {
				return;
			}
			rotationTimer = setInterval(nextGame, intervalMs);
		}

		function restartAutoRotation() {
			stopAutoRotation();
			startAutoRotation();
		}

		function createSlide(game, isActive) {
			const slide = document.createElement('a');
			slide.href = '/showcase';
			slide.className = 'frontpage-showcase-slide game-banner-link';
			if (isActive) {
				slide.classList.add('active');
			}
			slide.dataset.gameId = game.id;
			slide.setAttribute('aria-label', game.name);

			const img = document.createElement('img');
			img.alt = game.name;
			img.decoding = 'async';
			img.loading = isActive ? 'eager' : 'lazy';

			if (isActive) {
				img.src = getImageSrc(game);
				img.dataset.loaded = 'true';
			} else {
				img.dataset.src = getImageSrc(game);
			}

			slide.appendChild(img);
			return slide;
		}

		function ensureImageLoaded(slide) {
			const img = slide.querySelector('img');
			if (!img || img.dataset.loaded === 'true') {
				return Promise.resolve();
			}

			return new Promise(function(resolve) {
				let done = false;
				function finish() {
					if (done) {
						return;
					}
					done = true;
					img.dataset.loaded = 'true';
					resolve();
				}

				img.addEventListener('load', finish, { once: true });
				img.addEventListener('error', finish, { once: true });

				if (!img.src) {
					img.src = img.dataset.src;
				}

				if (img.complete) {
					finish();
				}
			});
		}

		function updateDots() {
			const dots = dotsContainer.querySelectorAll('.game-carousel-dot');
			dots.forEach(function(dot, index) {
				const isActive = index === currentIndex;
				dot.classList.toggle('active', isActive);
				dot.setAttribute('aria-current', isActive ? 'true' : 'false');
			});
		}

		function preloadNextImage() {
			if (slides.length <= 1) {
				return;
			}
			const nextIndex = (currentIndex + 1) % slides.length;
			ensureImageLoaded(slides[nextIndex]);
		}

		function renderCurrentGame() {
			const game = games[currentIndex];
			updateDots();
			bindBannerClick(game);
			trackImpression(game);
			preloadNextImage();
		}

		function showSlide(nextIndex) {
			if (nextIndex === currentIndex || isTransitioning) {
				return;
			}

			isTransitioning = true;
			const currentSlide = slides[currentIndex];
			const nextSlide = slides[nextIndex];

			ensureImageLoaded(nextSlide).then(function() {
				currentSlide.classList.remove('active');
				nextSlide.classList.add('active');
				currentIndex = nextIndex;
				renderCurrentGame();
			}).finally(function() {
				window.setTimeout(function() {
					isTransitioning = false;
				}, 700);
			});
		}

		function nextGame() {
			const nextIndex = (currentIndex + 1) % games.length;
			showSlide(nextIndex);
		}

		function initSlides() {
			const fallbackSlide = carousel.querySelector('.frontpage-showcase-slide');
			slides = [];

			games.forEach(function(game, index) {
				let slide;
				if (index === 0 && fallbackSlide) {
					slide = fallbackSlide;
					slide.dataset.gameId = game.id;
					slide.setAttribute('aria-label', game.name);
					slide.classList.add('active');
					const img = slide.querySelector('img');
					img.src = getImageSrc(game);
					img.alt = game.name;
					img.dataset.loaded = 'true';
					img.decoding = 'async';
					img.loading = 'eager';
				} else {
					slide = createSlide(game, false);
					carousel.insertBefore(slide, dotsContainer);
				}
				slides.push(slide);
			});
		}

		function createDots() {
			dotsContainer.innerHTML = '';
			games.forEach(function(game, index) {
				const dot = document.createElement('button');
				dot.type = 'button';
				dot.className = 'game-carousel-dot';
				dot.setAttribute('aria-label', 'Show game ' + (index + 1) + ': ' + game.name);
				dot.addEventListener('click', function() {
					showSlide(index);
					restartAutoRotation();
				});
				dotsContainer.appendChild(dot);
			});

			if (games.length <= 1) {
				dotsContainer.style.display = 'none';
			}
		}

		function trackMoreGamesButton() {
			const moreGamesButton = document.querySelector('#frontpage-more-games-button a');
			if (!moreGamesButton) {
				return;
			}
			moreGamesButton.addEventListener('click', function() {
				if (typeof gtag === 'undefined') {
					return;
				}
				gtag('event', 'game_click', {
					'game_id': games[currentIndex].id,
					'source_location': 'frontpage_more_button'
				});
			});
		}

		function setupAutoPause() {
			if ('IntersectionObserver' in window) {
				const observer = new IntersectionObserver(function(entries) {
					entries.forEach(function(entry) {
						if (entry.target !== carousel) {
							return;
						}
						carouselInViewport = entry.isIntersecting && entry.intersectionRatio > 0.2;
						if (canRotate()) {
							startAutoRotation();
						} else {
							stopAutoRotation();
						}
					});
				}, {
					threshold: [0, 0.2, 0.5]
				});
				observer.observe(carousel);
			}

			document.addEventListener('visibilitychange', function() {
				pageVisible = !document.hidden;
				if (canRotate()) {
					startAutoRotation();
				} else {
					stopAutoRotation();
				}
			});
		}

		initSlides();
		createDots();
		renderCurrentGame();
		trackMoreGamesButton();
		setupAutoPause();
		startAutoRotation();
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', initFrontpageCarousel);
	} else {
		initFrontpageCarousel();
	}
})();
