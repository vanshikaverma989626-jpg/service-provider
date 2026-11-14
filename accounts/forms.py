from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[
            ('customer', 'Customer'),
            ('provider', 'Provider')
        ]
    )
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'role',
            'password1',
            'password2'
        ]

class ProviderProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone',
            'society',
            'category',
            'price_per_visit',
            'experience_years',
            'is_available'
        ]
        labels = {
            'price_per_visit': 'Hourly Rate (₹/hour)'
        }