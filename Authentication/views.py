from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html', context = {'title':'Home'})

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('')
    template_name = "Authentication/signup.html"

class Login(generic.CreateView):
    pass

