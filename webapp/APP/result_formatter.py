"""
Legal-Compliant AI Result Formatter
Generates educational, non-diagnostic results following legal guidelines
"""

import random

def format_legal_result(prediction, confidence, model_used):
    """
    Format AI prediction into legally-compliant educational result
    
    Args:
        prediction (str): Raw AI prediction class name
        confidence (float): Model confidence score (0-1)
        model_used (str): Which model was used
    
    Returns:
        dict: Formatted result with all required legal components
    """
    
    # Normalize prediction name
    prediction_lower = prediction.lower().strip()
    
    # Check if this is an unclear/invalid image case
    if any(phrase in prediction_lower for phrase in ['may not be suitable', 'may need adjustment', 'may not be optimal']):
        return format_unclear_image_result(prediction, model_used)
    
    # Determine risk level based on condition and confidence
    risk_level = determine_risk_level(prediction_lower, confidence)
    
    # Get condition information
    condition_info = get_condition_info(prediction_lower)
    
    # Format the complete result
    result = {
        'card_title': 'AI Visual Pattern Analysis Result',
        'pattern_classification': condition_info['name'],
        'risk_label': get_risk_label(risk_level),
        'risk_color': get_risk_color(risk_level),
        'educational_description': condition_info['description'],
        'ai_explanation': generate_ai_explanation(prediction_lower, confidence, model_used),
        'visual_patterns': condition_info['patterns'],
        'confidence_display': f"{confidence*100:.1f}% (Model-specific estimate, not clinical certainty)",
        'professional_guidance': get_professional_guidance(risk_level),
        'disclaimer': get_mandatory_disclaimer(),
        'footer_disclaimer': get_footer_disclaimer(),
        'prevention_info': condition_info['prevention'],
        'precautions': condition_info['precautions']
    }
    
    return result

def format_unclear_image_result(prediction, model_used):
    """Format result for unclear or suboptimal images with gentle language"""
    
    result = {
        'card_title': 'AI Visual Pattern Analysis Result',
        'pattern_classification': 'Image Quality Assessment',
        'risk_label': 'Analysis May Be Limited',
        'risk_color': '#f59e0b',  # Amber color
        'educational_description': 'The uploaded image may not provide optimal conditions for reliable AI analysis. Image quality, lighting, focus, and angle can significantly affect the accuracy of visual pattern recognition.',
        'ai_explanation': f'The AI system using {model_used} has detected that this image may not meet the optimal conditions for reliable analysis. Factors such as lighting, image clarity, focus, or the content of the image may limit the system\'s ability to identify clear visual patterns.',
        'visual_patterns': [
            'Image quality may affect pattern recognition',
            'Lighting conditions may not be optimal',
            'Focus or clarity may be insufficient for analysis'
        ],
        'confidence_display': 'Analysis confidence may be limited due to image conditions',
        'professional_guidance': 'If you have concerns about your skin, consider consulting with a qualified healthcare professional who can perform a proper examination using appropriate medical equipment and clinical expertise.',
        'disclaimer': get_mandatory_disclaimer(),
        'footer_disclaimer': get_footer_disclaimer(),
        'prevention_info': 'For better AI analysis results, try uploading a clear, well-lit image taken in good lighting conditions.',
        'precautions': 'Consider retaking the image with better lighting and focus, or consult a healthcare professional for proper skin examination.'
    }
    
    return result

def determine_risk_level(prediction_lower, confidence):
    """Determine risk level based on condition type and confidence"""
    
    # High attention conditions
    high_risk_conditions = ['melanoma', 'basal cell carcinoma', 'squamous cell carcinoma']
    
    # Moderate attention conditions  
    moderate_risk_conditions = ['actinic keratoses', 'vascular lesions']
    
    # Low attention conditions
    low_risk_conditions = ['melanocytic nevi', 'benign keratosis like lesions', 'dermatofibroma', 'not_skin_cancer']
    
    if any(condition in prediction_lower for condition in high_risk_conditions):
        return 'red'
    elif any(condition in prediction_lower for condition in moderate_risk_conditions):
        return 'amber'  
    elif any(condition in prediction_lower for condition in low_risk_conditions):
        return 'green'
    else:
        return 'amber'  # Default to moderate for unknown conditions

def get_risk_label(risk_level):
    """Get appropriate risk label text"""
    labels = {
        'green': 'Likely Benign Visual Patterns',
        'amber': 'Non-Specific Visual Patterns Detected', 
        'red': 'High-Attention Visual Patterns Detected'
    }
    return labels.get(risk_level, 'Non-Specific Visual Patterns Detected')

def get_risk_color(risk_level):
    """Get color code for risk level"""
    colors = {
        'green': '#22c55e',
        'amber': '#f59e0b',
        'red': '#ef4444'
    }
    return colors.get(risk_level, '#f59e0b')

def get_condition_info(prediction_lower):
    """Get educational information about the condition"""
    
    conditions = {
        'actinic keratoses': {
            'name': 'Actinic Keratosis',
            'description': 'Actinic keratosis is a medical condition that may present as rough, scaly patches on sun-exposed areas of the skin. This condition can develop from prolonged sun exposure and may require professional medical evaluation.',
            'patterns': [
                'Rough or scaly surface texture',
                'Irregular pigmentation patterns', 
                'Variable size and shape characteristics'
            ],
            'prevention': 'Sun protection measures may help reduce risk, including wearing sunscreen, protective clothing, and avoiding prolonged sun exposure during peak hours.',
            'precautions': 'Monitor for any changes in size, texture, or appearance. Professional evaluation is recommended for proper assessment.'
        },
        
        'basal cell carcinoma': {
            'name': 'Basal Cell Carcinoma-Like Patterns',
            'description': 'Basal cell carcinoma is a medical condition that may present with certain visual characteristics on the skin. This condition requires professional medical evaluation for accurate assessment and appropriate care.',
            'patterns': [
                'Pearl-like or translucent appearance',
                'Irregular border characteristics',
                'Variable pigmentation patterns'
            ],
            'prevention': 'Sun protection measures are important, including regular use of sunscreen, protective clothing, and avoiding excessive UV exposure.',
            'precautions': 'Professional medical evaluation is strongly recommended for any concerning skin changes or new growths.'
        },
        
        'melanoma': {
            'name': 'Melanoma-Like Visual Patterns',
            'description': 'Melanoma is a serious medical condition that may present with specific visual characteristics on the skin. Early professional medical evaluation is crucial for proper assessment and care.',
            'patterns': [
                'Asymmetrical shape characteristics',
                'Irregular border patterns',
                'Color variation within the lesion',
                'Diameter changes over time'
            ],
            'prevention': 'Sun protection is essential, including daily sunscreen use, protective clothing, and avoiding tanning beds. Regular skin examinations are important.',
            'precautions': 'Immediate professional medical evaluation is strongly recommended for any suspicious skin changes or new growths.'
        },
        
        'melanocytic nevi': {
            'name': 'Melanocytic Nevus',
            'description': 'A melanocytic nevus is a common skin growth that may appear as a pigmented spot on the skin. These growths are frequently observed and can vary in appearance.',
            'patterns': [
                'Relatively uniform coloration',
                'Regular border patterns',
                'Symmetrical appearance',
                'Consistent size characteristics'
            ],
            'prevention': 'Sun protection may help prevent new mole development. Regular monitoring of existing moles is recommended.',
            'precautions': 'Monitor for any changes in size, shape, color, or texture. Professional evaluation is recommended if changes occur.'
        },
        
        'benign keratosis like lesions': {
            'name': 'Benign Keratosis-Like Lesions',
            'description': 'Benign keratosis-like lesions are common skin growths that may appear with certain visual characteristics. These growths can vary in appearance and typically require professional evaluation.',
            'patterns': [
                'Waxy or rough surface texture',
                'Well-defined border characteristics',
                'Variable pigmentation patterns'
            ],
            'prevention': 'Sun protection measures may help reduce the development of new growths.',
            'precautions': 'Monitor for any changes and consult a healthcare professional for proper evaluation.'
        },
        
        'dermatofibroma': {
            'name': 'Dermatofibroma',
            'description': 'Dermatofibroma is a benign skin growth that may appear as a firm bump on the skin. These growths can vary in appearance and typically require professional evaluation for accurate assessment.',
            'patterns': [
                'Firm, raised appearance',
                'Variable coloration patterns',
                'Well-defined border characteristics'
            ],
            'prevention': 'Avoiding skin trauma may help reduce risk. Gentle skin care practices are recommended.',
            'precautions': 'Monitor for any changes in size, color, or texture. Professional evaluation is recommended for proper assessment.'
        },
        
        'vascular lesions': {
            'name': 'Vascular Lesions',
            'description': 'Vascular lesions are skin growths that may involve blood vessels and can present with certain visual characteristics. Professional medical evaluation is recommended for proper assessment.',
            'patterns': [
                'Red or purple coloration',
                'Variable size characteristics',
                'Smooth or raised surface texture'
            ],
            'prevention': 'Protecting skin from injury may help. Gentle skin care practices are recommended.',
            'precautions': 'Monitor for any changes and consult a healthcare professional for evaluation.'
        },
        
        'squamous cell carcinoma': {
            'name': 'Squamous Cell Carcinoma-Like Patterns',
            'description': 'Squamous cell carcinoma is a medical condition that may present with specific visual characteristics on the skin. Professional medical evaluation is essential for proper assessment and care.',
            'patterns': [
                'Scaly or crusty surface texture',
                'Irregular border characteristics',
                'Variable pigmentation patterns'
            ],
            'prevention': 'Sun protection is crucial, including regular sunscreen use, protective clothing, and avoiding excessive UV exposure.',
            'precautions': 'Professional medical evaluation is strongly recommended for any concerning skin changes.'
        },
        
        'not_skin_cancer': {
            'name': 'Non-Specific Skin Patterns',
            'description': 'This analysis shows visual patterns that may be associated with various non-cancerous skin conditions. Professional medical evaluation is recommended for accurate assessment.',
            'patterns': [
                'Variable appearance characteristics',
                'Non-specific visual features',
                'Requires professional assessment'
            ],
            'prevention': 'General skin care practices including sun protection and gentle cleansing are recommended.',
            'precautions': 'Monitor for any changes and consult a healthcare professional for proper evaluation.'
        }
    }
    
    # Find matching condition
    for key, info in conditions.items():
        if key in prediction_lower:
            return info
    
    # Default for unknown conditions
    return conditions['not_skin_cancer']

def generate_ai_explanation(prediction_lower, confidence, model_used):
    """Generate AI explanation text"""
    
    base_text = "Based on an AI-powered visual pattern analysis, this image shows features that may resemble patterns sometimes associated with this condition. The AI model identified visual characteristics that appear similar to those found in medical literature."
    
    limitations = "Image quality, lighting, camera angle, and device limitations may significantly affect results. This analysis is based on visual patterns only and does not consider medical history, symptoms, or other clinical factors that are essential for proper medical evaluation."
    
    return f"{base_text}\n\n⚠️ Important Limitations:\n{limitations}"

def get_professional_guidance(risk_level):
    """Get appropriate professional consultation guidance"""
    
    guidance = {
        'green': "Professional evaluation by a qualified healthcare provider is recommended if there are any changes, symptoms, or concerns. Regular skin examinations are important for maintaining skin health and early detection of any issues.",
        
        'amber': "Consultation with a qualified healthcare professional is advised for further clarification and proper medical assessment. A dermatologist can provide accurate evaluation using medical-grade equipment and clinical expertise.",
        
        'red': "Prompt evaluation by a qualified healthcare professional is strongly recommended. Please schedule an appointment with a dermatologist or healthcare provider for proper medical assessment using appropriate medical equipment and clinical evaluation."
    }
    
    return guidance.get(risk_level, guidance['amber'])

def get_mandatory_disclaimer():
    """Get the mandatory non-diagnostic disclaimer"""
    
    return """Educational use only. NOT medical advice or diagnosis."""

def get_footer_disclaimer():
    """Get the mandatory footer disclaimer"""
    
    return """⚠️ IMPORTANT LEGAL NOTICE

Educational use only. NOT medical advice or diagnosis.

• AI analysis using standard camera photos
• NOT a substitute for professional medical evaluation
• Results may be inaccurate

Always consult a healthcare professional for medical concerns."""

def format_html_result(result_dict):
    """Format the result dictionary into HTML for display"""
    
    html = f"""
    <div class="ai-result-container" style="max-width: 800px; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        
        <!-- Pattern Classification Header -->
        <div class="pattern-classification" style="text-align: center; margin-bottom: 2rem; padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; color: white;">
            <h2 style="margin: 0 0 0.5rem 0; font-size: 1.8rem; font-weight: 600;">🔍 Pattern Classification</h2>
            <h3 style="margin: 0; font-size: 1.3rem; font-weight: 500; opacity: 0.95;">{result_dict['pattern_classification']}</h3>
        </div>
        
        <!-- Risk Level Indicator -->
        <div class="risk-indicator" style="border-left: 6px solid {result_dict['risk_color']}; background: rgba({','.join(str(int(result_dict['risk_color'][i:i+2], 16)) for i in (1, 3, 5))}, 0.1); padding: 1.5rem; margin: 2rem 0; border-radius: 8px;">
            <div style="color: {result_dict['risk_color']}; font-weight: 600; font-size: 1.2rem; margin: 0;">
                {result_dict['risk_label']}
            </div>
        </div>
        
        <!-- Educational Information -->
        <div class="educational-section" style="background: #f8fafc; padding: 2rem; margin: 2rem 0; border-radius: 12px; border: 1px solid #e2e8f0;">
            <h4 style="color: #2563eb; font-size: 1.2rem; font-weight: 600; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                📚 Educational Information
            </h4>
            <p style="color: #475569; line-height: 1.7; margin: 0; font-size: 1rem;">
                {result_dict['educational_description']}
            </p>
        </div>
        
        <!-- AI Visual Pattern Analysis -->
        <div class="ai-explanation-section" style="background: #f0f9ff; padding: 2rem; margin: 2rem 0; border-radius: 12px; border: 1px solid #bae6fd;">
            <h4 style="color: #0369a1; font-size: 1.2rem; font-weight: 600; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                🤖 AI Visual Pattern Analysis
            </h4>
            <p style="color: #475569; line-height: 1.7; margin: 0 0 1.5rem 0; font-size: 1rem;">
                {result_dict['ai_explanation']}
            </p>
            
            <!-- Visual Characteristics -->
            <div class="visual-patterns" style="margin: 1.5rem 0;">
                <h5 style="color: #374151; font-weight: 600; margin: 0 0 0.75rem 0; font-size: 1rem;">
                    Identified Visual Characteristics:
                </h5>
                <ul style="margin: 0; padding-left: 1.5rem; color: #475569; line-height: 1.6;">"""
    
    for pattern in result_dict['visual_patterns']:
        html += f"""
                    <li style="margin-bottom: 0.5rem;">{pattern}</li>"""
    
    html += f"""
                </ul>
            </div>
            
            <!-- Confidence Score -->
            <div class="confidence-score" style="margin: 2rem 0 0 0; padding: 1.25rem; background: white; border-radius: 8px; border: 2px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <div style="color: #374151; font-weight: 600; font-size: 1rem;">
                    <span style="color: #059669;">📊</span> AI Pattern Similarity Score: 
                    <span style="color: #0369a1; font-weight: 700;">{result_dict['confidence_display']}</span>
                </div>
            </div>
        </div>
        
        <!-- Professional Consultation Guidance -->
        <div class="professional-guidance-section" style="background: #eff6ff; border: 2px solid #2563eb; padding: 2rem; margin: 2rem 0; border-radius: 12px;">
            <h4 style="color: #1d4ed8; font-size: 1.2rem; font-weight: 600; margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.5rem;">
                ⚕️ Professional Consultation Guidance
            </h4>
            <p style="color: #475569; line-height: 1.7; margin: 0; font-size: 1rem;">
                {result_dict['professional_guidance']}
            </p>
        </div>
        
        <!-- Legal Notice -->
        <div class="footer-disclaimer" style="background: #1e293b; color: #e2e8f0; padding: 2rem; margin: 2rem 0; border-radius: 12px; border: 1px solid #334155;">
            <div style="font-size: 0.95rem; line-height: 1.6; white-space: pre-wrap; font-family: inherit;">
                {result_dict['footer_disclaimer']}
            </div>
        </div>
        
    </div>
    """
    
    return html