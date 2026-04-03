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
		const maxGames = Math.max(1, Number(config.maxGames) || 12);
		const scrollSpeedPxPerSec = Math.max(6, Number(config.scrollSpeedPxPerSec) || 18);
		const snapStrength = Math.max(4, Number(config.snapStrength) || 9);
		const sourceLocation = config.sourceLocation || 'frontpage_hero';
		const cardClickSourceLocation = config.cardClickSourceLocation || 'frontpage_banner';
		const moreButtonSourceLocation = config.moreButtonSourceLocation || 'frontpage_more_button';

		const carousel = document.getElementById('frontpage-showcase-carousel');
		const viewport = carousel ? carousel.querySelector('.frontpage-showcase-viewport') : null;
		const track = carousel ? carousel.querySelector('.frontpage-showcase-track') : null;
		const dotsContainer = document.getElementById('game-carousel-dots');
		if (!carousel || !viewport || !track || !dotsContainer) {
			return;
		}

		const byId = new Map();
		rawGames.forEach(function(game) {
			byId.set(game.id, game);
		});

		const orderedGames = [];
		const seenIds = new Set();

		featuredIds.forEach(function(gameId) {
			if (!gameId || seenIds.has(gameId)) {
				return;
			}

			const game = byId.get(gameId);
			if (!game) {
				return;
			}

			orderedGames.push(game);
			seenIds.add(gameId);
		});

		rawGames.forEach(function(game) {
			if (!game || seenIds.has(game.id)) {
				return;
			}

			orderedGames.push(game);
			seenIds.add(game.id);
		});

		const games = orderedGames.slice(0, maxGames);
		if (games.length === 0) {
			return;
		}

		const reducedMotionMedia = window.matchMedia
			? window.matchMedia('(prefers-reduced-motion: reduce)')
			: null;

		let prefersReducedMotion = Boolean(reducedMotionMedia && reducedMotionMedia.matches);
		let cardsPerView = 1;
		let logicalPages = [];
		let dotAnchors = [];
		let loopWidth = 0;
		let currentTranslate = 0;
		let targetTranslate = 0;
		let activeDotIndex = 0;
		let isSnapping = false;
		let pageVisible = !document.hidden;
		let carouselInViewport = true;
		let lastFrameTime = 0;
		let animationFrameId = null;
		let resizeTimer = null;
		let impressionObserver = null;

		const seenImpressions = new Set();

		function getCardsPerView() {
			const width = carousel.clientWidth || window.innerWidth || 0;
			if (width >= 1120) {
				return 4;
			}
			if (width >= 760) {
				return 3;
			}
			if (width >= 520) {
				return 2;
			}
			return 1;
		}

		function buildPages(items, pageSize) {
			const groupedPages = [];
			for (let index = 0; index < items.length; index += pageSize) {
				groupedPages.push(items.slice(index, index + pageSize));
			}
			return groupedPages;
		}

		function getImagePath(filename) {
			return filename ? '/images/games/' + filename : '';
		}

		function getResponsiveImageData(game) {
			const images = game.images || {};
			const sources = [];

			if (images.third) {
				sources.push({ path: getImagePath(images.third), width: 800 });
			}
			if (images.half) {
				sources.push({ path: getImagePath(images.half), width: 1200 });
			}
			if (images.full) {
				sources.push({ path: getImagePath(images.full), width: 2000 });
			}

			const fallbackSource = sources[0] || { path: '', width: 2000 };

			return {
				src: fallbackSource.path,
				srcset: sources.map(function(source) {
					return source.path + ' ' + source.width + 'w';
				}).join(', '),
				sizes: '(min-width: 1200px) 22vw, (min-width: 800px) 30vw, (min-width: 560px) 45vw, 92vw'
			};
		}

		function trackImpression(gameId) {
			if (typeof gtag === 'undefined' || seenImpressions.has(gameId)) {
				return;
			}

			const game = byId.get(gameId);
			if (!game) {
				return;
			}

			seenImpressions.add(gameId);
			gtag('event', 'game_impression', {
				'game_id': game.id,
				'source_location': sourceLocation
			});
		}

		function trackCardClick(gameId) {
			if (typeof gtag === 'undefined') {
				return;
			}

			gtag('event', 'game_click', {
				'game_id': gameId,
				'source_location': cardClickSourceLocation
			});
		}

		function createCard(game, copyIndex, baseIndex) {
			const imageData = getResponsiveImageData(game);

			const card = document.createElement('a');
			card.href = '/showcase';
			card.className = 'frontpage-showcase-card game-banner-link';
			card.dataset.gameId = game.id;
			card.dataset.loopCopy = String(copyIndex);
			card.dataset.baseIndex = String(baseIndex);
			card.setAttribute('aria-label', game.name);
			card.addEventListener('click', function() {
				trackCardClick(game.id);
			});

			const media = document.createElement('span');
			media.className = 'frontpage-showcase-card-media';

			const img = document.createElement('img');
			img.alt = game.name;
			img.decoding = 'async';
			img.loading = copyIndex === 1 ? 'eager' : 'lazy';
			img.sizes = imageData.sizes;
			if (copyIndex === 1 && baseIndex < cardsPerView) {
				img.fetchPriority = 'high';
			}
			if (imageData.srcset) {
				img.srcset = imageData.srcset;
			}
			img.src = imageData.src;
			media.appendChild(img);

			const copy = document.createElement('span');
			copy.className = 'frontpage-showcase-card-copy';

			const title = document.createElement('span');
			title.className = 'frontpage-showcase-card-title';
			title.textContent = game.name;

			const meta = document.createElement('span');
			meta.className = 'frontpage-showcase-card-meta';
			meta.textContent = game.developer ? 'By ' + game.developer : 'Made with Defold';

			copy.appendChild(title);
			copy.appendChild(meta);
			card.appendChild(media);
			card.appendChild(copy);

			return card;
		}

		function normalizeTranslate(value) {
			if (loopWidth <= 0) {
				return value;
			}

			let normalized = value;
			while (normalized >= 0) {
				normalized -= loopWidth;
			}
			while (normalized < -2 * loopWidth) {
				normalized += loopWidth;
			}
			return normalized;
		}

		function applyTransform() {
			track.style.transform = 'translate3d(' + currentTranslate.toFixed(2) + 'px, 0, 0)';
		}

		function createDots() {
			dotsContainer.innerHTML = '';

			logicalPages.forEach(function(_, index) {
				const dot = document.createElement('button');
				dot.type = 'button';
				dot.className = 'game-carousel-dot';
				dot.setAttribute('aria-label', 'Show game set ' + (index + 1));
				dot.addEventListener('click', function() {
					scrollToDot(index);
				});
				dotsContainer.appendChild(dot);
			});

			dotsContainer.hidden = logicalPages.length <= 1;
		}

		function measureLoopWidth() {
			const firstCopyCard = track.querySelector('.frontpage-showcase-card[data-loop-copy="0"][data-base-index="0"]');
			const middleCopyCard = track.querySelector('.frontpage-showcase-card[data-loop-copy="1"][data-base-index="0"]');

			if (firstCopyCard && middleCopyCard) {
				loopWidth = middleCopyCard.offsetLeft - firstCopyCard.offsetLeft;
			} else {
				loopWidth = 0;
			}

			if (loopWidth <= 0) {
				loopWidth = track.scrollWidth / 3;
			}
		}

		function buildDotAnchors() {
			dotAnchors = logicalPages.map(function(_, pageIndex) {
				const baseIndex = pageIndex * cardsPerView;
				const card = track.querySelector('.frontpage-showcase-card[data-loop-copy="1"][data-base-index="' + baseIndex + '"]');
				return card ? -card.offsetLeft : -loopWidth;
			});
		}

		function updateActiveDot() {
			if (dotAnchors.length === 0 || loopWidth <= 0) {
				return;
			}

			let closestIndex = 0;
			let smallestDistance = Infinity;

			dotAnchors.forEach(function(anchor, index) {
				[anchor - loopWidth, anchor, anchor + loopWidth].forEach(function(candidate) {
					const distance = Math.abs(candidate - currentTranslate);
					if (distance < smallestDistance) {
						smallestDistance = distance;
						closestIndex = index;
					}
				});
			});

			activeDotIndex = closestIndex;

			const dots = dotsContainer.querySelectorAll('.game-carousel-dot');
			dots.forEach(function(dot, index) {
				const isActive = index === activeDotIndex;
				dot.classList.toggle('active', isActive);
				dot.setAttribute('aria-current', isActive ? 'true' : 'false');
			});
		}

		function getNearestAnchor(anchor) {
			if (loopWidth <= 0) {
				return anchor;
			}

			const candidates = [anchor - loopWidth, anchor, anchor + loopWidth];
			return candidates.reduce(function(bestCandidate, candidate) {
				return Math.abs(candidate - currentTranslate) < Math.abs(bestCandidate - currentTranslate)
					? candidate
					: bestCandidate;
			}, candidates[0]);
		}

		function scrollToDot(dotIndex) {
			if (!dotAnchors[dotIndex]) {
				return;
			}

			const nextTarget = getNearestAnchor(dotAnchors[dotIndex]);

			if (prefersReducedMotion) {
				currentTranslate = normalizeTranslate(nextTarget);
				targetTranslate = currentTranslate;
				isSnapping = false;
				applyTransform();
				updateActiveDot();
				return;
			}

			targetTranslate = nextTarget;
			isSnapping = true;
		}

		function observeImpressions() {
			if (impressionObserver) {
				impressionObserver.disconnect();
			}

			if (!('IntersectionObserver' in window)) {
				games.forEach(function(game) {
					trackImpression(game.id);
				});
				return;
			}

			impressionObserver = new IntersectionObserver(function(entries) {
				entries.forEach(function(entry) {
					if (!entry.isIntersecting || entry.intersectionRatio < 0.55) {
						return;
					}

					trackImpression(entry.target.dataset.gameId);
				});
			}, {
				root: viewport,
				threshold: [0.55]
			});

			track.querySelectorAll('.frontpage-showcase-card').forEach(function(card) {
				impressionObserver.observe(card);
			});
		}

		function renderTrack(anchorDotIndex) {
			cardsPerView = getCardsPerView();
			logicalPages = buildPages(games, cardsPerView);
			carousel.style.setProperty('--frontpage-showcase-visible-cards', String(cardsPerView));
			track.innerHTML = '';

			for (let copyIndex = 0; copyIndex < 3; copyIndex += 1) {
				games.forEach(function(game, baseIndex) {
					track.appendChild(createCard(game, copyIndex, baseIndex));
				});
			}

			measureLoopWidth();
			buildDotAnchors();
			createDots();

			const safeAnchorIndex = Math.max(0, Math.min(anchorDotIndex || 0, Math.max(dotAnchors.length - 1, 0)));
			currentTranslate = dotAnchors[safeAnchorIndex] || -loopWidth;
			currentTranslate = normalizeTranslate(currentTranslate);
			targetTranslate = currentTranslate;
			activeDotIndex = safeAnchorIndex;
			isSnapping = false;

			applyTransform();
			updateActiveDot();
			observeImpressions();
		}

		function shouldAnimate() {
			return !prefersReducedMotion && carouselInViewport && pageVisible && loopWidth > 0;
		}

		function animate(timestamp) {
			if (!lastFrameTime) {
				lastFrameTime = timestamp;
			}

			const deltaSeconds = Math.min(0.05, (timestamp - lastFrameTime) / 1000);
			lastFrameTime = timestamp;

			if (shouldAnimate()) {
				if (isSnapping) {
					const distance = targetTranslate - currentTranslate;
					currentTranslate += distance * Math.min(1, deltaSeconds * snapStrength);

					if (Math.abs(distance) <= 0.5) {
						currentTranslate = normalizeTranslate(targetTranslate);
						targetTranslate = currentTranslate;
						isSnapping = false;
					}
				} else {
					currentTranslate = normalizeTranslate(currentTranslate - scrollSpeedPxPerSec * deltaSeconds);
				}

				applyTransform();
				updateActiveDot();
			}

			animationFrameId = window.requestAnimationFrame(animate);
		}

		function trackMoreGamesButton() {
			const moreGamesButton = document.querySelector('#frontpage-more-games-button a');
			if (!moreGamesButton) {
				return;
			}

			moreGamesButton.addEventListener('click', function() {
				const trackedGame = logicalPages[activeDotIndex] && logicalPages[activeDotIndex][0]
					? logicalPages[activeDotIndex][0]
					: games[0];

				if (typeof gtag === 'undefined' || !trackedGame) {
					return;
				}

				gtag('event', 'game_click', {
					'game_id': trackedGame.id,
					'source_location': moreButtonSourceLocation
				});
			});
		}

		function setupVisibilityHandling() {
			if ('IntersectionObserver' in window) {
				const observer = new IntersectionObserver(function(entries) {
					entries.forEach(function(entry) {
						if (entry.target !== carousel) {
							return;
						}

						carouselInViewport = entry.isIntersecting && entry.intersectionRatio > 0.2;
					});
				}, {
					threshold: [0, 0.2, 0.5]
				});
				observer.observe(carousel);
			}

			document.addEventListener('visibilitychange', function() {
				pageVisible = !document.hidden;
				lastFrameTime = 0;
			});

			if (reducedMotionMedia) {
				const handleReducedMotionChange = function(event) {
					prefersReducedMotion = event.matches;
					lastFrameTime = 0;
					if (prefersReducedMotion) {
						isSnapping = false;
						targetTranslate = currentTranslate;
					}
				};

				if (typeof reducedMotionMedia.addEventListener === 'function') {
					reducedMotionMedia.addEventListener('change', handleReducedMotionChange);
				} else if (typeof reducedMotionMedia.addListener === 'function') {
					reducedMotionMedia.addListener(handleReducedMotionChange);
				}
			}
		}

		function setupResizeHandling() {
			window.addEventListener('resize', function() {
				clearTimeout(resizeTimer);
				resizeTimer = window.setTimeout(function() {
					const nextCardsPerView = getCardsPerView();
					if (nextCardsPerView === cardsPerView) {
						return;
					}

					renderTrack(activeDotIndex);
					lastFrameTime = 0;
				}, 150);
			});
		}

		renderTrack(0);
		trackMoreGamesButton();
		setupVisibilityHandling();
		setupResizeHandling();
		animationFrameId = window.requestAnimationFrame(animate);

		window.addEventListener('beforeunload', function() {
			if (animationFrameId) {
				window.cancelAnimationFrame(animationFrameId);
			}
			if (impressionObserver) {
				impressionObserver.disconnect();
			}
		}, { once: true });
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', initFrontpageCarousel);
	} else {
		initFrontpageCarousel();
	}
})();
