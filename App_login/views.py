from django.shortcuts import render
from django.views import generic
from App_login.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import  reverse
from django import forms

# Create your views here.
def home(request):
    return render(request, 'home.html', context = {'title':'Home'})

def sign_up(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('App_login:login')) 
    context = {'form':form}
    return render(request, 'Authentication/signup.html', context= context)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form =AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'Authentication/login.html', context={'form':form})

@login_required
def logout(request):
    logout(request)
    return render(request, 'home.html')