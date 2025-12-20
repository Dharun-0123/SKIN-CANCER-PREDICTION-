/**
 * Tooltip System for SkinCare AI
 * Provides contextual help throughout the application
 */

// Tooltip data structure
const tooltips = {
    // Home page tooltips
    'model-accuracy': 'Our AI models achieve 92% accuracy on test datasets. This represents the percentage of correct predictions on unseen data.',
    'analysis-time': 'Average time to process and analyze a skin lesion image using our AI models.',
    'classifications': 'Number of different skin condition types our AI can identify and classify.',
    'your-analyses': 'Total number of skin lesion images you have analyzed using our system.',
    
    // Analysis page tooltips
    'model-selection': 'Choose which AI model to use for analysis. Auto mode intelligently selects the best model based on image characteristics.',
    'efficientnet-model': 'EfficientNetB0: State-of-the-art deep learning model trained on 25,331 professional medical images from ISIC 2019 dataset.',
    'cnn-model': 'CNN: Reliable convolutional neural network trained on 3,297 images with proven accuracy.',
    'auto-mode': 'Automatically selects the most appropriate AI model based on your image quality and characteristics.',
    'image-upload': 'Upload a clear, well-lit photo of the skin lesion. For best results, ensure good lighting and focus.',
    'image-quality': 'Higher quality images produce more accurate results. Avoid blurry, dark, or poorly lit photos.',
    
    // Results tooltips
    'confidence-score': 'Indicates how confident the AI model is in its prediction. Higher values suggest more certainty.',
    'model-used': 'The specific AI model that analyzed your image and generated the results.',
    'classification-result': 'The AI\'s prediction of the skin condition type based on visual analysis.',
    
    // History tooltips
    'export-pdf': 'Download a professional PDF report of this analysis for your records or to share with healthcare providers.',
    'compare-analyses': 'Compare multiple analyses side-by-side to track changes over time.',
    
    // General tooltips
    'medical-disclaimer': 'This tool is for educational and informational purposes only. It is NOT a medical diagnostic device and should not replace professional medical advice.',
    'consult-doctor': 'Always consult a qualified dermatologist or healthcare provider for proper diagnosis and treatment.',
    'image-limitations': 'Results may vary as images are captured with standard cameras, not medical-grade equipment or dermoscopy.',
};

// Initialize tooltips when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeTooltips();
    initializeDisclaimerModal();
});

/**
 * Initialize all tooltips on the page
 */
function initializeTooltips() {
    // Find all elements with data-tooltip attribute
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(element => {
        const tooltipKey = element.getAttribute('data-tooltip');
        const tooltipText = tooltips[tooltipKey] || 'Information not available';
        
        // Create tooltip element
        const tooltip = document.createElement('div');
        tooltip.className = 'tooltip-popup';
        tooltip.textContent = tooltipText;
        tooltip.style.display = 'none';
        document.body.appendChild(tooltip);
        
        // Show tooltip on hover
        element.addEventListener('mouseenter', function(e) {
            showTooltip(tooltip, element);
        });
        
        element.addEventListener('mouseleave', function() {
            hideTooltip(tooltip);
        });
        
        // Add tooltip icon if not present
        if (!element.querySelector('.tooltip-icon')) {
            const icon = document.createElement('i');
            icon.className = 'fas fa-info-circle tooltip-icon';
            icon.style.marginLeft = '0.5rem';
            icon.style.color = 'var(--accent-cyan)';
            icon.style.cursor = 'help';
            icon.style.fontSize = '0.9em';
            element.appendChild(icon);
        }
    });
}

/**
 * Show tooltip at appropriate position
 */
function showTooltip(tooltip, element) {
    const rect = element.getBoundingClientRect();
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
    
    tooltip.style.display = 'block';
    tooltip.style.opacity = '0';
    
    // Position tooltip
    const tooltipRect = tooltip.getBoundingClientRect();
    let top = rect.bottom + scrollTop + 10;
    let left = rect.left + scrollLeft + (rect.width / 2) - (tooltipRect.width / 2);
    
    // Adjust if tooltip goes off screen
    if (left < 10) left = 10;
    if (left + tooltipRect.width > window.innerWidth - 10) {
        left = window.innerWidth - tooltipRect.width - 10;
    }
    
    // If tooltip goes below viewport, show above element
    if (top + tooltipRect.height > window.innerHeight + scrollTop) {
        top = rect.top + scrollTop - tooltipRect.height - 10;
    }
    
    tooltip.style.top = top + 'px';
    tooltip.style.left = left + 'px';
    
    // Fade in
    setTimeout(() => {
        tooltip.style.opacity = '1';
    }, 10);
}

/**
 * Hide tooltip
 */
function hideTooltip(tooltip) {
    tooltip.style.opacity = '0';
    setTimeout(() => {
        tooltip.style.display = 'none';
    }, 200);
}

/**
 * Initialize Terms & Conditions and Info modal
 */
function initializeDisclaimerModal() {
    // Check if user has accepted terms
    const hasAcceptedTerms = localStorage.getItem('skincare_ai_terms_accepted');
    
    if (!hasAcceptedTerms) {
        // Show terms on first visit
        setTimeout(() => {
            showTermsModal();
        }, 800);
    }
    
    // Enable/disable accept button based on checkbox
    const termsCheckbox = document.getElementById('termsAccept');
    const acceptBtn = document.getElementById('acceptTermsBtn');
    
    if (termsCheckbox && acceptBtn) {
        termsCheckbox.addEventListener('change', function() {
            acceptBtn.disabled = !this.checked;
        });
    }
}

/**
 * Show Terms & Conditions modal
 */
function showTermsModal() {
    const modal = document.getElementById('termsModal');
    if (modal) {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }
}

/**
 * Accept Terms & Conditions
 */
function acceptTerms() {
    const checkbox = document.getElementById('termsAccept');
    if (checkbox && checkbox.checked) {
        const modal = document.getElementById('termsModal');
        if (modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
            localStorage.setItem('skincare_ai_terms_accepted', 'true');
            localStorage.setItem('skincare_ai_terms_date', new Date().toISOString());
        }
    }
}

/**
 * Decline Terms & Conditions
 */
function declineTerms() {
    if (confirm('You must accept the Terms & Conditions to use SkinCare AI. Would you like to review them again?')) {
        // Keep modal open
        return;
    } else {
        // Redirect to landing page or logout
        window.location.href = '/';
    }
}

/**
 * Show Info modal (softer disclaimer)
 */
function showInfoModal() {
    const modal = document.getElementById('infoModal');
    if (modal) {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }
}

/**
 * Hide Info modal
 */
function hideInfoModal() {
    const modal = document.getElementById('infoModal');
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

// Export functions for global use
window.showTermsModal = showTermsModal;
window.acceptTerms = acceptTerms;
window.declineTerms = declineTerms;
window.showInfoModal = showInfoModal;
window.hideInfoModal = hideInfoModal;
