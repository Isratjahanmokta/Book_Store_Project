from django.urls import path
from .views import sign_up, login_page, logout
app_name = 'App_login'

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout, name='logout'),

]