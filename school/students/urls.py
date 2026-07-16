from django.urls import path
from . import views

urlpatterns = [
    # Remove the admin line from here!
    path('', views.home, name='home'),
]