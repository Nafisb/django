from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login'),
    path('networks/', views.networks, name='networks'),
]