from django.contrib import admin
from django.urls import path, include
from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include("Authentication.urls")),
    path('pages/', include("pages.urls")),
]
