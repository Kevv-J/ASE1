from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    fullname = forms.CharField(
        required=True,
        label='FullName',
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'class': 'input_box'
            }
        )
    )

    username = forms.CharField(
        required=True,
        label='Username',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'input_box'
            }
        )
    )

    id = forms.CharField(
        required=True,
        label='Voter Id',
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'class': 'input_box'
            }
        )
    )

    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'class': 'input_box'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'fullname', 'id', 'email', 'password1', 'password2']
