/**
 * YouTube Lazy Loading
 * Replaces thumbnails with actual iframes when clicked
 * Uses proactive thumbnail detection to avoid 404 errors
 */

// Cache for thumbnail availability to avoid duplicate checks
window.thumbnailCache = new Map();

// Check if a thumbnail URL is available without triggering 404 errors
function checkThumbnailAvailability(videoId, quality) {
    const cacheKey = `${videoId}_${quality}`;
    
    // Return cached result if available
    if (window.thumbnailCache.has(cacheKey)) {
        return Promise.resolve(window.thumbnailCache.get(cacheKey));
    }
    
    return new Promise((resolve) => {
        const img = new Image();
        const url = `https://img.youtube.com/vi/${videoId}/${quality}.jpg`;
        
        img.onload = () => {
            // Additional check: YouTube returns a 120x90 placeholder for invalid videos
            // Real thumbnails are larger
            const isValid = img.width > 120 || img.height > 90;
            window.thumbnailCache.set(cacheKey, isValid);
            resolve(isValid);
        };
        
        img.onerror = () => {
            window.thumbnailCache.set(cacheKey, false);
            resolve(false);
        };
        
        img.src = url;
    });
}

// Find the best available thumbnail for a video
async function getBestThumbnail(videoId) {
    const qualities = ['maxresdefault', 'hqdefault', 'default'];
    
    for (const quality of qualities) {
        const available = await checkThumbnailAvailability(videoId, quality);
        if (available) {
            const url = `https://img.youtube.com/vi/${videoId}/${quality}.jpg`;
            console.log(`Best thumbnail for ${videoId}: ${quality}`);
            return url;
        }
    }
    
    // Fallback to icon if all thumbnails fail
    console.warn(`No valid thumbnail found for ${videoId}, using fallback icon`);
    return '/images/icons/yt_icon_rgb.svg';
}

// Set thumbnail with loading state management
async function setThumbnail(thumbnailImg, videoId) {
    const card = thumbnailImg.closest('.youtube-lazy-card');
    const container = thumbnailImg.closest('.youtube-thumbnail-container');
    
    // Add loading state
    card.classList.add('thumbnail-loading');
    
    try {
        const bestThumbnailUrl = await getBestThumbnail(videoId);
        
        // Set thumbnail with fade-in effect
        thumbnailImg.style.opacity = '0';
        thumbnailImg.src = bestThumbnailUrl;
        
        // Handle fallback icon styling
        if (bestThumbnailUrl.includes('yt_icon_rgb.svg')) {
            thumbnailImg.style.objectFit = 'contain';
            thumbnailImg.style.padding = '20px';
            thumbnailImg.style.backgroundColor = '#f9f9f9';
        }
        
        thumbnailImg.onload = () => {
            thumbnailImg.style.opacity = '1';
            card.classList.remove('thumbnail-loading');
            card.classList.add('thumbnail-loaded');
        };
        
    } catch (error) {
        console.error('Error loading thumbnail for', videoId, error);
        card.classList.remove('thumbnail-loading');
    }
}

(function() {
    'use strict';

    function initYoutubeLazy() {
        const lazyCards = document.querySelectorAll('.youtube-lazy-card');
        
        lazyCards.forEach(function(card) {
            const playButton = card.querySelector('.youtube-play-button');
            const thumbnail = card.querySelector('.youtube-thumbnail');
            const container = card.querySelector('.youtube-thumbnail-container');
            const videoId = card.dataset.videoId;
            
            // Proactively set the best thumbnail (no 404 errors)
            if (thumbnail && videoId) {
                setThumbnail(thumbnail, videoId);
            }
            
            if (playButton && container) {
                playButton.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const embedUrl = card.dataset.embed;
                    const videoId = card.dataset.videoId;
                    
                    if (embedUrl && videoId) {
                        loadYoutubeVideo(container, embedUrl);
                    }
                });

                // Also allow clicking the thumbnail itself
                thumbnail.addEventListener('click', function(e) {
                    e.preventDefault();
                    playButton.click();
                });
            }
        });
    }

    function loadYoutubeVideo(container, embedUrl) {
        // Add loading state
        container.style.opacity = '0.7';
        container.style.pointerEvents = 'none';
        
        // Create iframe
        const iframe = document.createElement('iframe');
        iframe.width = '100%';
        iframe.height = '100%';
        iframe.src = embedUrl + '?autoplay=1';
        iframe.title = 'YouTube video player';
        iframe.frameBorder = '0';
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
        iframe.allowFullscreen = true;
        iframe.style.position = 'absolute';
        iframe.style.top = '0';
        iframe.style.left = '0';
        iframe.style.width = '100%';
        iframe.style.height = '100%';
        
        // Replace content
        container.innerHTML = '';
        container.appendChild(iframe);
        
        // Reset styles
        container.style.opacity = '1';
        container.style.pointerEvents = 'auto';
        
        // Optional: Track analytics
        if (typeof gtag !== 'undefined') {
            gtag('event', 'video_play', {
                event_category: 'engagement',
                event_label: embedUrl
            });
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initYoutubeLazy);
    } else {
        initYoutubeLazy();
    }

})();