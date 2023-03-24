from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
CustomUser = get_user_model()

class CustomUserCreationForm(UserChangeForm):
    first_name = forms.CharField(required=True, label='', widget= forms.TextInput(attrs={'placeholder':'First name'}))
    last_name = forms.CharField(required=True, label='', widget= forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(required = True, label='', widget= forms.TextInput(attrs ={'placeholder':'Email'}))
    password1 = forms.CharField(
        required= True,
        label='',
        widget= forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'})
    )
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

class CustomUserChangeForm(UserCreationForm):
    model = get_user_model
    class Meta:
        fields = ("email","username")