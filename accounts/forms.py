from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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