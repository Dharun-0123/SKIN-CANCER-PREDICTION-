/**
 * DermaGenie AI Widget - Quick Access Chatbot
 * Floating button in bottom-left for skin-related questions
 */

// Widget state
let widgetOpen = false;
let conversationHistory = [];

// Initialize widget when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeDermaGenieWidget();
});

/**
 * Initialize the DermaGenie widget
 */
function initializeDermaGenieWidget() {
    // Only show for authenticated users (not on login/register pages)
    const isAuthPage = window.location.pathname.includes('/login') || 
                       window.location.pathname.includes('/register') ||
                       window.location.pathname.includes('/admin');
    
    if (isAuthPage) {
        return; // Don't show on auth pages
    }
    
    // Create widget HTML
    createWidgetHTML();
    
    // Attach event listeners
    attachWidgetEventListeners();
    
    // Add suggested questions
    addSuggestedQuestions();
}

/**
 * Create widget HTML structure
 */
function createWidgetHTML() {
    const widgetHTML = `
        <!-- DermaGenie AI Widget Button -->
        <div class="dermagenie-widget-button" id="dermagenieButton" title="Ask DermaGenie AI">
            <i class="fas fa-magic"></i>
            <span class="widget-label">DermaGenie AI</span>
            <span class="widget-pulse"></span>
        </div>

        <!-- DermaGenie AI Chat Widget -->
        <div class="dermagenie-widget-container" id="dermagenieWidget">
            <div class="widget-header">
                <div class="widget-header-content">
                    <div class="widget-avatar">
                        <i class="fas fa-magic"></i>
                    </div>
                    <div class="widget-title">
                        <h3>DermaGenie AI</h3>
                        <p class="widget-status">
                            <span class="status-dot"></span>
                            Online - Skin Health Assistant
                        </p>
                    </div>
                </div>
                <button class="widget-close" id="widgetClose">
                    <i class="fas fa-times"></i>
                </button>
            </div>

            <div class="widget-body" id="widgetBody">
                <div class="widget-welcome">
                    <div class="welcome-icon">
                        <i class="fas fa-magic"></i>
                    </div>
                    <h4>Welcome to DermaGenie AI!</h4>
                    <p>I'm your AI-powered skin health assistant. Ask me anything about:</p>
                    <ul>
                        <li>🔬 Skin conditions and lesions</li>
                        <li>🛡️ Skin cancer prevention</li>
                        <li>💊 Skincare recommendations</li>
                        <li>📊 Understanding your analysis results</li>
                        <li>🏥 When to see a dermatologist</li>
                    </ul>
                </div>

                <div class="suggested-questions" id="suggestedQuestions">
                    <p class="suggested-title">Quick Questions:</p>
                    <div class="suggested-buttons" id="suggestedButtons">
                        <!-- Populated by JavaScript -->
                    </div>
                </div>

                <div class="chat-messages" id="chatMessages">
                    <!-- Messages will be added here -->
                </div>
            </div>

            <div class="widget-footer">
                <form class="widget-input-form" id="widgetForm">
                    <input 
                        type="text" 
                        id="widgetInput" 
                        placeholder="Ask about skin health..."
                        autocomplete="off"
                    >
                    <button type="submit" class="widget-send-btn" id="widgetSend">
                        <i class="fas fa-paper-plane"></i>
                    </button>
                </form>
                <p class="widget-disclaimer">
                    <i class="fas fa-info-circle"></i>
                    AI assistant for educational purposes only. Not medical advice.
                </p>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', widgetHTML);
}

/**
 * Attach event listeners to widget elements
 */
function attachWidgetEventListeners() {
    const button = document.getElementById('dermagenieButton');
    const widget = document.getElementById('dermagenieWidget');
    const closeBtn = document.getElementById('widgetClose');
    const form = document.getElementById('widgetForm');
    const input = document.getElementById('widgetInput');
    
    // Toggle widget
    button.addEventListener('click', toggleWidget);
    closeBtn.addEventListener('click', closeWidget);
    
    // Handle form submission
    form.addEventListener('submit', handleMessageSubmit);
    
    // Close widget when clicking outside
    document.addEventListener('click', function(e) {
        if (widgetOpen && 
            !widget.contains(e.target) && 
            !button.contains(e.target)) {
            closeWidget();
        }
    });
}

/**
 * Toggle widget open/close
 */
function toggleWidget() {
    const widget = document.getElementById('dermagenieWidget');
    const button = document.getElementById('dermagenieButton');
    
    widgetOpen = !widgetOpen;
    
    if (widgetOpen) {
        widget.classList.add('widget-open');
        button.classList.add('widget-active');
        document.getElementById('widgetInput').focus();
    } else {
        widget.classList.remove('widget-open');
        button.classList.remove('widget-active');
    }
}

/**
 * Close widget
 */
function closeWidget() {
    const widget = document.getElementById('dermagenieWidget');
    const button = document.getElementById('dermagenieButton');
    
    widgetOpen = false;
    widget.classList.remove('widget-open');
    button.classList.remove('widget-active');
}

/**
 * Add suggested questions
 */
function addSuggestedQuestions() {
    const questions = [
        "What is melanoma?",
        "How to prevent skin cancer?",
        "What are common skin lesions?",
        "When should I see a dermatologist?",
        "How accurate is AI skin analysis?",
        "What is a benign mole?"
    ];
    
    const container = document.getElementById('suggestedButtons');
    
    questions.forEach(question => {
        const button = document.createElement('button');
        button.className = 'suggested-question-btn';
        button.textContent = question;
        button.addEventListener('click', function() {
            handleSuggestedQuestion(question);
        });
        container.appendChild(button);
    });
}

/**
 * Handle suggested question click
 */
function handleSuggestedQuestion(question) {
    document.getElementById('widgetInput').value = question;
    handleMessageSubmit(new Event('submit'));
}

/**
 * Handle message submission
 */
async function handleMessageSubmit(e) {
    e.preventDefault();
    
    const input = document.getElementById('widgetInput');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Clear input
    input.value = '';
    
    // Hide suggested questions after first message
    const suggestedSection = document.getElementById('suggestedQuestions');
    if (suggestedSection) {
        suggestedSection.style.display = 'none';
    }
    
    // Add user message to chat
    addMessageToChat('user', message);
    
    // Show typing indicator
    showTypingIndicator();
    
    // Send to backend
    try {
        const response = await fetch('/dermagenie-chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                message: message,
                history: conversationHistory
            })
        });
        
        const data = await response.json();
        
        // Remove typing indicator
        removeTypingIndicator();
        
        if (data.success) {
            // Add AI response to chat
            addMessageToChat('ai', data.response);
            
            // Update conversation history
            conversationHistory.push({
                user: message,
                ai: data.response
            });
        } else {
            addMessageToChat('ai', 'Sorry, I encountered an error. Please try again or visit the full DermaGenie page.');
        }
    } catch (error) {
        console.error('Error:', error);
        removeTypingIndicator();
        addMessageToChat('ai', 'Sorry, I\'m having trouble connecting. Please try again later.');
    }
}

/**
 * Add message to chat
 */
function addMessageToChat(type, message) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${type}-message`;
    
    if (type === 'ai') {
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-magic"></i>
            </div>
            <div class="message-content">
                <div class="message-text">${formatMessage(message)}</div>
                <div class="message-time">${getCurrentTime()}</div>
            </div>
        `;
    } else {
        messageDiv.innerHTML = `
            <div class="message-content">
                <div class="message-text">${escapeHtml(message)}</div>
                <div class="message-time">${getCurrentTime()}</div>
            </div>
            <div class="message-avatar">
                <i class="fas fa-user"></i>
            </div>
        `;
    }
    
    chatMessages.appendChild(messageDiv);
    
    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Show typing indicator
 */
function showTypingIndicator() {
    const chatMessages = document.getElementById('chatMessages');
    const typingDiv = document.createElement('div');
    typingDiv.className = 'chat-message ai-message typing-indicator';
    typingDiv.id = 'typingIndicator';
    typingDiv.innerHTML = `
        <div class="message-avatar">
            <i class="fas fa-magic"></i>
        </div>
        <div class="message-content">
            <div class="typing-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;
    
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

/**
 * Remove typing indicator
 */
function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) {
        indicator.remove();
    }
}

/**
 * Format AI message (preserve line breaks, add links, etc.)
 */
function formatMessage(message) {
    // Escape HTML
    let formatted = escapeHtml(message);
    
    // Convert line breaks to <br>
    formatted = formatted.replace(/\n/g, '<br>');
    
    // Convert **bold** to <strong>
    formatted = formatted.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Convert bullet points
    formatted = formatted.replace(/^- /gm, '• ');
    
    return formatted;
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Get current time formatted
 */
function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit' 
    });
}

/**
 * Get CSRF token from cookies
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Export functions for global use
window.toggleDermaGenieWidget = toggleWidget;
window.closeDermaGenieWidget = closeWidget;
