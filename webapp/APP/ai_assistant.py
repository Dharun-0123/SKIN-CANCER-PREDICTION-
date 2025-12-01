"""
DermaGenie - AI Skin Care Assistant
Powered by OpenAI GPT
"""
import openai
from django.conf import settings
import markdown
from markdown.extensions import fenced_code, tables, nl2br


def format_ai_response(text):
    """
    Format AI response with markdown to HTML conversion
    Simple conversion without custom classes - CSS handles styling
    """
    # Configure markdown extensions
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'tables',
        'nl2br',
        'sane_lists'
    ])
    
    # Convert markdown to HTML - no custom classes needed
    html = md.convert(text)
    
    return html


def get_dermagenie_response(user_message, conversation_history=None):
    """
    Get response from DermaGenie AI Assistant
    
    Args:
        user_message (str): User's question or message
        conversation_history (list): Previous conversation messages
        
    Returns:
        dict: Response with formatted text and metadata
    """
    try:
        # Get API key from settings
        api_key = getattr(settings, 'OPENAI_API_KEY', None)
        if not api_key:
            return {
                'success': False,
                'error': 'API key not configured',
                'message': 'Please configure your OpenAI API key in settings.'
            }
        
        # Initialize OpenAI client (works with Perplexity API too)
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.perplexity.ai"
        )
        
        # System prompt for DermaGenie
        system_prompt = """You are DermaGenie, an intelligent AI assistant specializing in skin care and dermatology education. 

Your role:
- Provide accurate, helpful information about skin conditions
- Explain skin care routines and best practices
- Offer guidance on when to see a dermatologist
- Answer questions about skin cancer prevention
- Educate users about various skin conditions

Important guidelines:
- Always emphasize that you're an educational tool, not a replacement for professional medical advice
- Encourage users to consult dermatologists for diagnosis and treatment
- Use clear, easy-to-understand language
- Format your responses with:
  * **Bold** for important terms
  * *Italic* for emphasis
  * Bullet points for lists
  * Numbered lists for steps
  * Headings (##) for sections
- Be empathetic and supportive
- Provide actionable advice when appropriate
- Include disclaimers when discussing medical conditions

Remember: You're here to educate and guide, not diagnose or prescribe treatment."""

        # Build messages array
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        # Call Perplexity API (OpenAI-compatible)
        response = client.chat.completions.create(
            model="sonar",  # Perplexity's Sonar model
            messages=messages,
            max_tokens=1000,
            temperature=0.7,
            top_p=0.9
            # Note: Perplexity doesn't support both frequency_penalty and presence_penalty
        )
        
        # Extract response text
        ai_response = response.choices[0].message.content
        
        # Format the response
        formatted_response = format_ai_response(ai_response)
        
        return {
            'success': True,
            'raw_text': ai_response,
            'formatted_html': formatted_response,
            'tokens_used': response.usage.total_tokens,
            'model': response.model
        }
        
    except openai.AuthenticationError:
        return {
            'success': False,
            'error': 'authentication_error',
            'message': '🔑 Invalid API key. Please check your OpenAI API key configuration in settings.py'
        }
    except openai.RateLimitError:
        return {
            'success': False,
            'error': 'rate_limit',
            'message': '⏱️ Rate limit exceeded. Your OpenAI account has reached its usage limit. Please:\n\n1. Wait a few minutes and try again\n2. Check your OpenAI account usage at: https://platform.openai.com/usage\n3. Add credits to your account if needed\n4. Verify your API key has sufficient quota'
        }
    except openai.APIError as e:
        return {
            'success': False,
            'error': 'api_error',
            'message': f'⚠️ OpenAI API error: {str(e)}\n\nPlease check:\n- Your internet connection\n- OpenAI service status\n- Your API key validity'
        }
    except Exception as e:
        return {
            'success': False,
            'error': 'unknown_error',
            'message': f'❌ An error occurred: {str(e)}\n\nPlease try again or contact support if the issue persists.'
        }


def get_quick_suggestions():
    """
    Get quick suggestion prompts for users
    """
    return [
        "What are the early signs of skin cancer?",
        "How can I protect my skin from sun damage?",
        "What's the difference between a mole and melanoma?",
        "How often should I check my skin for changes?",
        "What are the best ingredients for anti-aging?",
        "How do I treat acne naturally?",
        "What causes dry skin and how to fix it?",
        "When should I see a dermatologist?"
    ]


def save_conversation(user, message, response):
    """
    Save conversation to database for history
    """
    from .models import ChatConversation
    
    try:
        conversation = ChatConversation.objects.create(
            user=user,
            user_message=message,
            ai_response=response['raw_text'],
            tokens_used=response.get('tokens_used', 0),
            model=response.get('model', 'gpt-3.5-turbo')
        )
        return conversation
    except Exception as e:
        print(f"Error saving conversation: {str(e)}")
        return None
