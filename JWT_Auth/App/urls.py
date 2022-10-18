from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegistrationView , LoginView ,UserProfileView ,ChangePassView

urlpatterns = [
    path('reg/', UserRegistrationView.as_view() , name='registration'),
    path('login/', LoginView.as_view() , name='login'),
    path('profile/', UserProfileView.as_view() , name='profile'),
    path('changepassword/', ChangePassView.as_view() , name='ChangePass'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    ]
