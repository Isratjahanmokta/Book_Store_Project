from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from App_login.models import CustomUser


class CustomUserCreationForm(UserChangeForm):
    first_name = forms.CharField(
        required=True,
        label='', 
        widget=forms.TextInput(
            attrs={'placeholder': 'First name'})
        )
    last_name = forms.CharField(
        required=True, 
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Last Name'})
        )
    username = forms.CharField(
        required=True, 
        label='', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'})
        )
    email = forms.EmailField(
        required=True, 
        label='', 
        widget=forms.TextInput(
        attrs={'placeholder': 'Email'})
        )
    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password Confirmation'})
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password', 'password1')
