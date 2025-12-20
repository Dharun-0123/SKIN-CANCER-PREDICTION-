from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from keras.models import load_model
import cv2
import numpy as np
import pickle
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import json
from PIL import Image
import os
from django.conf import settings


# Global variable to hold the model
_model = None

def get_model():
    """Lazy load the model only when needed"""
    global _model
    if _model is None:
        model_path = os.path.join(settings.BASE_DIR, "models", "CNN_skin-cancer.h5")
        _model = load_model(model_path, compile=False)
    return _model

def predict(img, algo): 
    # Assuming img is already the file path to the image
    # Read and resize the image
    img = cv2.imread(img)
    img = cv2.resize(img, (48, 48))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0 
    print("*********")
    print(img) # Normalize the image
    # Reshape the image to match the model input shape
    img = np.reshape(img, (1, 48, 48, 3))
    if algo == "inc":
        mob = get_model()
        predictions = mob.predict(img)
        return predictions


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    email_verified = models.BooleanField(default=False)  # Email verification status
    email_notifications = models.BooleanField(default=True)
    first_analysis_email_sent = models.BooleanField(default=False)  # Track if first analysis email sent
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    @property
    def total_predictions(self):
        return UserPredictModel.objects.filter(user=self.user).count()

    @property
    def recent_predictions(self):
        return UserPredictModel.objects.filter(user=self.user).order_by('-created_at')[:5]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a profile when a new user is created"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the profile when the user is saved"""
    if hasattr(instance, 'profile'):
        instance.profile.save()


class UserPredictModel(models.Model):
    MODEL_CHOICES = [
        ('auto', 'Auto (Smart Selection)'),
        ('efficientnet', 'EfficientNetB0 (Primary)'),
        ('cnn', 'CNN (Secondary)'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to = 'images/')
    label = models.CharField(max_length=200, default='data')
    model_preference = models.CharField(max_length=20, choices=MODEL_CHOICES, default='auto')
    model_used = models.CharField(max_length=50, blank=True, null=True)  # Which model was actually used
    confidence_score = models.FloatField(blank=True, null=True)  # Confidence of the prediction
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)
    
    class Meta:
        ordering = ['-created_at']


class ChatConversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_conversations')
    user_message = models.TextField()
    ai_response = models.TextField()
    tokens_used = models.IntegerField(default=0)
    model = models.CharField(max_length=50, default='sonar')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Chat Conversation'
        verbose_name_plural = 'Chat Conversations'
    


# Email Verification OTP Model
class EmailOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='email_otp')
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Email OTP'
        verbose_name_plural = 'Email OTPs'
    
    def __str__(self):
        return f"OTP for {self.user.username}"
    
    def is_expired(self):
        """Check if OTP is expired (10 minutes)"""
        from django.utils import timezone
        from datetime import timedelta
        expiry_time = self.created_at + timedelta(minutes=getattr(settings, 'OTP_EXPIRY_MINUTES', 10))
        return timezone.now() > expiry_time
    
    @classmethod
    def create_or_update(cls, user, otp):
        """Create or update OTP for user"""
        obj, created = cls.objects.update_or_create(
            user=user,
            defaults={'otp': otp, 'is_verified': False}
        )
        return obj


# Password Reset OTP Model
class PasswordResetOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='password_reset_otp')
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Password Reset OTP'
        verbose_name_plural = 'Password Reset OTPs'
    
    def __str__(self):
        return f"Password Reset OTP for {self.user.username}"
    
    def is_expired(self):
        """Check if OTP is expired (15 minutes for password reset)"""
        from django.utils import timezone
        from datetime import timedelta
        expiry_time = self.created_at + timedelta(minutes=15)  # 15 minutes for password reset
        return timezone.now() > expiry_time
    
    @classmethod
    def create_or_update(cls, user, otp):
        """Create or update password reset OTP for user"""
        obj, created = cls.objects.update_or_create(
            user=user,
            defaults={'otp': otp, 'is_used': False}
        )
        return obj
