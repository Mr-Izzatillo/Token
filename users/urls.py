from django.urls import path
from .views import LoginView, RegisterView, ResetPasswordView, UserView, UserDetailView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/<int:id>/', UserDetailView.as_view(), name='detail'),
    path('reset-password/', ResetPasswordView.as_view())
    
]