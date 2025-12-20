from django import forms 
from . models import UserPredictModel, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'phone', 'date_of_birth', 'profile_picture', 'email_notifications']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

        
class UserPredictForm(forms.ModelForm):
    class Meta:
        model = UserPredictModel
        fields = ['image', 'model_preference']
        widgets = {
            'model_preference': forms.Select(attrs={
                'class': 'form-control model-selector',
                'id': 'model-selector'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

