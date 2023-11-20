# account/urls.py

from django import views
from django.urls import path
from .views import register, user_login, user_logout, join_view


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('join/', join_view, name='join'),
]
