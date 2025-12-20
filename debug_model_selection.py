#!/usr/bin/env python3
"""
Debug script to test model selection functionality
"""

import os
import sys
import django

# Setup Django
sys.path.append('webapp')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT.settings')
django.setup()

from APP.models import UserPredictModel
from django.contrib.auth.models import User

def debug_model_selection():
    print("🔍 Debugging Model Selection")
    print("=" * 40)
    
    # Check if we have any users
    users = User.objects.all()
    print(f"Total users: {users.count()}")
    
    if users.exists():
        user = users.first()
        print(f"Testing with user: {user.username}")
        
        # Check recent predictions
        predictions = UserPredictModel.objects.filter(user=user).order_by('-created_at')[:5]
        print(f"\nRecent predictions: {predictions.count()}")
        
        for i, pred in enumerate(predictions, 1):
            print(f"\n{i}. Prediction ID: {pred.id}")
            print(f"   Model Preference: {pred.model_preference}")
            print(f"   Model Used: {pred.model_used}")
            print(f"   Confidence: {pred.confidence_score}")
            print(f"   Created: {pred.created_at}")
            print(f"   Label: {pred.label[:50]}...")
    
    # Check model choices
    print(f"\nModel Choices:")
    for choice in UserPredictModel.MODEL_CHOICES:
        print(f"   {choice[0]} -> {choice[1]}")
    
    return True

if __name__ == "__main__":
    debug_model_selection()