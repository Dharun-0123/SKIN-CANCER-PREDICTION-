/**
 * Mobile Navigation JavaScript
 * Handles mobile menu toggle, interactions, and accessibility
 */

document.addEventListener('DOMContentLoaded', function () {
    // Get mobile navigation elements
    const mobileNavToggle = document.getElementById('mobileNavToggle');
    const mobileNavMenu = document.getElementById('mobileNavMenu');
    const navbar = document.getElementById('navbar');
    const body = document.body;
    
    // Check if elements exist
    if (!mobileNavToggle || !mobileNavMenu) {
        console.warn('Mobile navigation elements not found');
        return;
    }
    
    // State management
    let isMenuOpen = false;
    
    /**
     * Toggle mobile menu open/close
     */
    function toggleMobileMenu() {
        isMenuOpen = !isMenuOpen;
        
        if (isMenuOpen) {
            openMobileMenu();
        } else {
            closeMobileMenu();
        }
    }
    
    /**
     * Open mobile menu
     */
    function openMobileMenu() {
        mobileNavMenu.classList.add('active');
        mobileNavToggle.innerHTML = '<i class="fas fa-times"></i>';
        mobileNavToggle.setAttribute('aria-expanded', 'true');
        mobileNavToggle.setAttribute('aria-label', 'Close navigation menu');
        body.classList.add('mobile-nav-open');
        
        // Focus management
        mobileNavMenu.setAttribute('aria-hidden', 'false');
        
        // Trap focus within menu
        trapFocus(mobileNavMenu);
    }
    
    /**
     * Close mobile menu
     */
    function closeMobileMenu() {
        mobileNavMenu.classList.remove('active');
        mobileNavToggle.innerHTML = '<i class="fas fa-bars"></i>';
        mobileNavToggle.setAttribute('aria-expanded', 'false');
        mobileNavToggle.setAttribute('aria-label', 'Open navigation menu');
        body.classList.remove('mobile-nav-open');
        
        // Focus management
        mobileNavMenu.setAttribute('aria-hidden', 'true');
        
        // Return focus to toggle button
        mobileNavToggle.focus();
    }
    
    /**
     * Trap focus within an element
     */
    function trapFocus(element) {
        const focusableElements = element.querySelectorAll(
            'a[href], button, textarea, input[type="text"], input[type="radio"], input[type="checkbox"], select'
        );
        
        if (focusableElements.length === 0) return;
        
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];
        
        element.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                if (e.shiftKey) {
                    if (document.activeElement === firstElement) {
                        lastElement.focus();
                        e.preventDefault();
                    }
                } else {
                    if (document.activeElement === lastElement) {
                        firstElement.focus();
                        e.preventDefault();
                    }
                }
            }
        });
        
        // Focus first element
        firstElement.focus();
    }
    
    // Event Listeners
    
    // Toggle button click
    mobileNavToggle.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        toggleMobileMenu();
    });
    
    // Close menu when clicking on navigation links
    const mobileNavLinks = mobileNavMenu.querySelectorAll('a');
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Small delay to allow navigation to start
            setTimeout(() => {
                isMenuOpen = false;
                closeMobileMenu();
            }, 150);
        });
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (isMenuOpen && 
            !navbar.contains(e.target) && 
            !mobileNavMenu.contains(e.target)) {
            isMenuOpen = false;
            closeMobileMenu();
        }
    });
    
    // Handle escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && isMenuOpen) {
            isMenuOpen = false;
            closeMobileMenu();
        }
    });
    
    // Close menu on window resize if screen becomes larger
    window.addEventListener('resize', function() {
        if (window.innerWidth > 767 && isMenuOpen) {
            isMenuOpen = false;
            closeMobileMenu();
        }
    });
    
    // Handle orientation change on mobile devices
    window.addEventListener('orientationchange', function() {
        if (isMenuOpen) {
            // Close menu on orientation change to prevent layout issues
            setTimeout(() => {
                isMenuOpen = false;
                closeMobileMenu();
            }, 100);
        }
    });
    
    // Initialize accessibility attributes
    function initializeAccessibility() {
        mobileNavToggle.setAttribute('aria-expanded', 'false');
        mobileNavToggle.setAttribute('aria-label', 'Open navigation menu');
        mobileNavToggle.setAttribute('aria-controls', 'mobileNavMenu');
        
        mobileNavMenu.setAttribute('aria-hidden', 'true');
        mobileNavMenu.setAttribute('role', 'navigation');
        mobileNavMenu.setAttribute('aria-label', 'Mobile navigation menu');
    }
    
    // Initialize
    initializeAccessibility();
    
    // Smooth scroll behavior for anchor links
    mobileNavLinks.forEach(link => {
        if (link.getAttribute('href').startsWith('#')) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    // Close menu first
                    isMenuOpen = false;
                    closeMobileMenu();
                    
                    // Then scroll to target
                    setTimeout(() => {
                        targetElement.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }, 300);
                }
            });
        }
    });
    
    // Performance optimization: debounce resize events
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            if (window.innerWidth > 767 && isMenuOpen) {
                isMenuOpen = false;
                closeMobileMenu();
            }
        }, 250);
    });
    
    console.log('Mobile navigation initialized successfully');
});