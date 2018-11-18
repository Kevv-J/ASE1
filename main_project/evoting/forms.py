from django import forms
from django.contrib.auth.models import User
from .models import Voters_Profile

class Registration_form1(forms.ModelForm):
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'input_boxes',
                'placeholder': 'Password'
            }
        )
    )

    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'input_boxes',
                'placeholder': 'Username'
            }
        )
    )

    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'input_boxes',
                'placeholder': 'Email (abc@gmail.com)',
                'pattern': '[a-z0-9._%+-]+@[g]+[m]+[a]+[i]+[l]+\.[c]+[o]+[m]$',
                'oninvalid': 'this.setCustomValidity("Email must be in (example@gmail.com) format")'
            }
        )
    )



    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class Registration_form2(forms.ModelForm):
    voter_dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2002)))
    fullname = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'input_boxes',
                'placeholder': 'Fullname'
            }
        )
    )

    voterId = forms.IntegerField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'input_boxes',
                'placeholder': 'Voter Id',
                'name': 'voterId'
            }
        )
    )

    class Meta():
        model = Voters_Profile
        fields = ('fullname', 'voterId', 'voter_dob')
