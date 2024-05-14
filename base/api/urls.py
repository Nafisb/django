from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('user/register/', views.UserRegistrationView.as_view(), name='register'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/all/', views.UserListView.as_view(), name='user_list'),
    path('network/all/', views.NetworkListView.as_view(), name='network_list'),
    path('network/create/', views.NetworkCreateView.as_view(), name='network_create'),
    path('network/update/<str:id>/', views.update_network, name='network_update'),
    path('network/delete/<str:id>/', views.NetworkDeletionView, name='network_delete'),
]
