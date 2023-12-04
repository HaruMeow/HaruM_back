# account/urls.py

from django.urls import path
from .views import join_form, register, user_login, user_logout, join_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('join/', join_view, name='join'),
    path('join-form/', join_form, name='join-form'),  # join_form을 추가해주세요
]
