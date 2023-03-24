from django.urls import path
from .views import SignUp

app_name = 'Authentication'
urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]
