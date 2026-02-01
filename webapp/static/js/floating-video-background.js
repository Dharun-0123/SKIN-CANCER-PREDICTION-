/**
 * Premium Floating Video Background Controller - Landing Page Only
 * Handles video loading, performance optimization, and user preferences
 * Updated to use frontvideo.mp4 specifically for the landing page
 */

document.addEventListener('DOMContentLoaded', function() {
    const videoBackground = document.getElementById('videoBackground');
    const video = videoBackground?.querySelector('video');
    
    if (!video) return;
    
    // Performance and accessibility settings
    const settings = {
        enableOnMobile: window.innerWidth > 768,
        respectReducedMotion: window.matchMedia('(prefers-reduced-motion: reduce)').matches,
        enableParticles: window.innerWidth > 1024,
        lowPowerMode: navigator.hardwareConcurrency < 4 || navigator.deviceMemory < 4
    };
    
    /**
     * Initialize video background with performance optimizations
     */
    function initVideoBackground() {
        console.log('🎬 Initializing landing page video background with frontvideo.mp4');
        
        // Add loading class
        videoBackground.classList.add('loading');
        
        // Disable on mobile or low-power devices if needed
        if (!settings.enableOnMobile || settings.lowPowerMode) {
            video.style.display = 'none';
            videoBackground.classList.add('no-video');
            console.log('📱 Video disabled for mobile/low-power device');
            return;
        }
        
        // Respect reduced motion preference
        if (settings.respectReducedMotion) {
            video.style.animationPlayState = 'paused';
            console.log('♿ Animation paused for reduced motion preference');
        }
        
        // Optimize video settings
        video.playbackRate = 0.8; // Slightly slower for cinematic effect
        video.volume = 0; // Ensure muted
        
        // Handle video loading
        video.addEventListener('loadeddata', handleVideoLoaded);
        video.addEventListener('canplaythrough', handleVideoReady);
        video.addEventListener('error', handleVideoError);
        
        // Intersection Observer for performance
        setupIntersectionObserver();
        
        // Handle particles
        if (!settings.enableParticles) {
            const particles = videoBackground.querySelector('.particles');
            if (particles) particles.style.display = 'none';
        }
    }
    
    /**
     * Handle video loaded event
     */
    function handleVideoLoaded() {
        console.log('🎬 Landing page video (frontvideo.mp4) loaded successfully');
        videoBackground.classList.remove('loading');
        videoBackground.classList.add('loaded');
    }
    
    /**
     * Handle video ready to play
     */
    function handleVideoReady() {
        // Ensure video plays smoothly
        video.play().catch(error => {
            console.warn('Video autoplay blocked:', error);
            // Fallback to static background
            videoBackground.classList.add('no-video');
        });
    }
    
    /**
     * Handle video loading errors
     */
    function handleVideoError(error) {
        console.warn('Video background failed to load:', error);
        videoBackground.classList.add('no-video');
        video.style.display = 'none';
    }
    
    /**
     * Setup Intersection Observer for performance optimization
     */
    function setupIntersectionObserver() {
        if (!('IntersectionObserver' in window)) return;
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Video is visible, ensure it's playing
                    if (video.paused) {
                        video.play().catch(() => {});
                    }
                } else {
                    // Video is not visible, pause for performance
                    if (!video.paused) {
                        video.pause();
                    }
                }
            });
        }, {
            threshold: 0.1
        });
        
        observer.observe(videoBackground);
    }
    
    /**
     * Handle window resize for responsive behavior
     */
    function handleResize() {
        const newWidth = window.innerWidth;
        
        // Show/hide based on screen size
        if (newWidth <= 768 && !settings.enableOnMobile) {
            video.style.display = 'none';
            videoBackground.classList.add('no-video');
        } else if (newWidth > 768 && settings.enableOnMobile) {
            video.style.display = 'block';
            videoBackground.classList.remove('no-video');
        }
        
        // Handle particles
        const particles = videoBackground.querySelector('.particles');
        if (particles) {
            particles.style.display = newWidth > 1024 ? 'block' : 'none';
        }
    }
    
    /**
     * Handle visibility change (tab switching)
     */
    function handleVisibilityChange() {
        if (document.hidden) {
            // Tab is hidden, pause video
            if (!video.paused) {
                video.pause();
            }
        } else {
            // Tab is visible, resume video
            if (video.paused && !settings.respectReducedMotion) {
                video.play().catch(() => {});
            }
        }
    }
    
    /**
     * Preload video for better performance
     */
    function preloadVideo() {
        // Create a temporary video element to preload
        const tempVideo = document.createElement('video');
        tempVideo.preload = 'metadata';
        tempVideo.src = video.src;
        tempVideo.load();
    }
    
    // Initialize everything
    initVideoBackground();
    
    // Event listeners
    window.addEventListener('resize', debounce(handleResize, 250));
    document.addEventListener('visibilitychange', handleVisibilityChange);
    
    // Preload video after a short delay
    setTimeout(preloadVideo, 1000);
    
    // Debug info (remove in production)
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        console.log('🎬 Video Background Settings:', settings);
        console.log('📱 Screen width:', window.innerWidth);
        console.log('🔧 Hardware concurrency:', navigator.hardwareConcurrency);
        console.log('💾 Device memory:', navigator.deviceMemory, 'GB');
    }
});

/**
 * Debounce function for performance
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Detect if user prefers reduced motion
 */
function respectsReducedMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

/**
 * Check if device is low-power
 */
function isLowPowerDevice() {
    return navigator.hardwareConcurrency < 4 || 
           (navigator.deviceMemory && navigator.deviceMemory < 4) ||
           /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

/**
 * Export for potential external use
 */
window.VideoBackground = {
    pause: () => document.querySelector('.video-background video')?.pause(),
    play: () => document.querySelector('.video-background video')?.play(),
    toggle: () => {
        const video = document.querySelector('.video-background video');
        if (video) {
            video.paused ? video.play() : video.pause();
        }
    }
};