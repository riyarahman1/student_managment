from django.urls import path
from .views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('',LoginView.as_view(), name='login'),
    path('signup/',RegisterView.as_view(), name='signup'),
    path('logout/',LogoutView.as_view(), name='logout'),
]


