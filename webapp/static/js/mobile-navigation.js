/**
 * Mobile Navigation JavaScript - With Comprehensive Debug Logging
 * Handles mobile menu toggle, interactions, and accessibility
 */

document.addEventListener('DOMContentLoaded', function () {
    console.log('========================================');
    console.log('📱 MOBILE NAVIGATION DEBUG LOG');
    console.log('========================================');
    console.log('⏰ Script loaded at:', new Date().toLocaleTimeString());
    console.log('📐 Window width:', window.innerWidth + 'px');
    console.log('📱 Is mobile view:', window.innerWidth <= 767 ? 'YES' : 'NO');
    
    // Get mobile navigation elements
    const mobileNavToggle = document.getElementById('mobileNavToggle');
    const mobileNavMenu = document.getElementById('mobileNavMenu');
    const navbar = document.getElementById('navbar');
    const body = document.body;
    
    // Check if elements exist
    console.log('\n🔍 ELEMENT CHECK:');
    console.log('   Toggle button (#mobileNavToggle):', mobileNavToggle ? '✅ FOUND' : '❌ NOT FOUND');
    console.log('   Menu (#mobileNavMenu):', mobileNavMenu ? '✅ FOUND' : '❌ NOT FOUND');
    console.log('   Navbar (#navbar):', navbar ? '✅ FOUND' : '❌ NOT FOUND');
    
    if (!mobileNavToggle || !mobileNavMenu) {
        console.error('❌ CRITICAL: Mobile navigation elements not found!');
        console.log('   Check that base.html has:');
        console.log('   - <button id="mobileNavToggle">');
        console.log('   - <div id="mobileNavMenu">');
        return;
    }
    
    // Initialize state based on CSS classes
    let isMenuOpen = mobileNavMenu.classList.contains('active');
    
    // Debug function to show current state
    function logCurrentState(action) {
        console.log('\n📊 STATE CHECK (' + action + '):');
        console.log('   Menu has .active class:', mobileNavMenu.classList.contains('active') ? '✅ YES' : '❌ NO');
        console.log('   Body has .mobile-nav-open:', body.classList.contains('mobile-nav-open') ? '✅ YES' : '❌ NO');
        console.log('   JS isMenuOpen variable:', isMenuOpen ? '✅ TRUE' : '❌ FALSE');
        console.log('   Menu visibility (computed):', getComputedStyle(mobileNavMenu).visibility);
        console.log('   Menu opacity (computed):', getComputedStyle(mobileNavMenu).opacity);
        console.log('   Menu transform (computed):', getComputedStyle(mobileNavMenu).transform);
    }
    
    /**
     * Toggle mobile menu open/close
     */
    function toggleMobileMenu() {
        console.log('\n🔄 TOGGLE FUNCTION CALLED');
        
        // Check current state from DOM - check both possible classes
        const hasActiveClass = mobileNavMenu.classList.contains('active');
        const hasBodyClass = body.classList.contains('mobile-nav-open');
        const currentlyOpen = hasActiveClass || hasBodyClass;
        
        console.log('   Checking state:');
        console.log('   - .active class:', hasActiveClass);
        console.log('   - body.mobile-nav-open:', hasBodyClass);
        console.log('   - Determined state:', currentlyOpen ? 'OPEN → will CLOSE' : 'CLOSED → will OPEN');
        
        if (currentlyOpen) {
            closeMobileMenu();
        } else {
            openMobileMenu();
        }
    }
    
    /**
     * Open mobile menu
     */
    function openMobileMenu() {
        console.log('\n🟢 OPENING MENU...');
        
        isMenuOpen = true;
        
        // Apply both classes for maximum compatibility
        mobileNavMenu.classList.add('active');
        body.classList.add('mobile-nav-open');
        
        // Update toggle button
        mobileNavToggle.innerHTML = '<i class="fas fa-times"></i>';
        mobileNavToggle.setAttribute('aria-expanded', 'true');
        mobileNavToggle.setAttribute('aria-label', 'Close navigation menu');
        
        // Focus management
        mobileNavMenu.setAttribute('aria-hidden', 'false');
        
        console.log('   ✅ Added .active to menu');
        console.log('   ✅ Added .mobile-nav-open to body');
        console.log('   ✅ Changed icon to X (fa-times)');
        
        // Verify after a short delay
        setTimeout(() => {
            logCurrentState('After Opening');
        }, 100);
    }
    
    /**
     * Close mobile menu
     */
    function closeMobileMenu() {
        console.log('\n🔴 CLOSING MENU...');
        
        isMenuOpen = false;
        
        // Remove both classes for maximum compatibility
        mobileNavMenu.classList.remove('active');
        body.classList.remove('mobile-nav-open');
        
        // Update toggle button
        mobileNavToggle.innerHTML = '<i class="fas fa-bars"></i>';
        mobileNavToggle.setAttribute('aria-expanded', 'false');
        mobileNavToggle.setAttribute('aria-label', 'Open navigation menu');
        
        // Focus management
        mobileNavMenu.setAttribute('aria-hidden', 'true');
        
        console.log('   ✅ Removed .active from menu');
        console.log('   ✅ Removed .mobile-nav-open from body');
        console.log('   ✅ Changed icon to hamburger (fa-bars)');
        
        // Verify after a short delay
        setTimeout(() => {
            logCurrentState('After Closing');
        }, 100);
    }
    
    // Event Listeners
    console.log('\n🎯 SETTING UP EVENT LISTENERS...');
    
    // Toggle button click
    mobileNavToggle.addEventListener('click', function(e) {
        console.log('\n========================================');
        console.log('👆 HAMBURGER BUTTON CLICKED!');
        console.log('========================================');
        console.log('   Event type:', e.type);
        console.log('   Target:', e.target.tagName);
        console.log('   Time:', new Date().toLocaleTimeString());
        
        e.preventDefault();
        e.stopPropagation();
        
        logCurrentState('Before Toggle');
        toggleMobileMenu();
    });
    console.log('   ✅ Click listener added to toggle button');
    
    // Close menu when clicking on navigation links
    const mobileNavLinks = mobileNavMenu.querySelectorAll('a');
    console.log('   📎 Found', mobileNavLinks.length, 'navigation links in menu');
    
    mobileNavLinks.forEach((link, index) => {
        link.addEventListener('click', function() {
            console.log('\n🔗 NAV LINK CLICKED:', this.textContent.trim());
            closeMobileMenu();
        });
    });
    console.log('   ✅ Click listeners added to all nav links');
    
    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        const menuIsActive = mobileNavMenu.classList.contains('active');
        const clickedOnToggle = mobileNavToggle.contains(e.target);
        const clickedInMenu = mobileNavMenu.contains(e.target);
        
        if (menuIsActive && !clickedOnToggle && !clickedInMenu) {
            console.log('\n🌍 CLICKED OUTSIDE MENU - Closing...');
            closeMobileMenu();
        }
    });
    console.log('   ✅ Outside click listener added');
    
    // Handle escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && mobileNavMenu.classList.contains('active')) {
            console.log('\n⌨️ ESCAPE KEY PRESSED - Closing...');
            closeMobileMenu();
        }
    });
    console.log('   ✅ Escape key listener added');
    
    // Close menu on window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 767 && mobileNavMenu.classList.contains('active')) {
            console.log('\n📐 WINDOW RESIZED TO DESKTOP - Closing...');
            closeMobileMenu();
        }
    });
    console.log('   ✅ Resize listener added');
    
    // Initialize accessibility attributes and ensure proper initial state
    function initializeAccessibility() {
        console.log('\n🔧 INITIALIZING...');
        
        // Ensure menu starts closed
        mobileNavMenu.classList.remove('active');
        body.classList.remove('mobile-nav-open');
        
        // Set initial ARIA attributes
        mobileNavToggle.setAttribute('aria-expanded', 'false');
        mobileNavToggle.setAttribute('aria-label', 'Open navigation menu');
        mobileNavToggle.setAttribute('aria-controls', 'mobileNavMenu');
        
        mobileNavMenu.setAttribute('aria-hidden', 'true');
        mobileNavMenu.setAttribute('role', 'navigation');
        mobileNavMenu.setAttribute('aria-label', 'Mobile navigation menu');
        
        // Ensure hamburger icon is shown initially
        mobileNavToggle.innerHTML = '<i class="fas fa-bars"></i>';
        
        console.log('   ✅ Cleared all active classes');
        console.log('   ✅ Set ARIA attributes');
        console.log('   ✅ Set hamburger icon');
        
        logCurrentState('After Initialization');
    }
    
    // Initialize immediately
    initializeAccessibility();
    
    console.log('\n========================================');
    console.log('✅ MOBILE NAVIGATION READY!');
    console.log('========================================');
    console.log('📱 Click the hamburger button (☰) to test');
    console.log('🔍 Watch this console for debug output');
    console.log('========================================\n');
});