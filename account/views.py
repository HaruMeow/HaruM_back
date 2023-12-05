from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from .forms import UserRegistrationForm, UserLoginForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            nickname = form.cleaned_data['nickname']
            UserProfile.objects.create(user=user, nickname=nickname)
            login(request, user)
            return redirect('index')  
    else:
        form = UserRegistrationForm()
    return render(request, 'account/join.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def join_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            nickname = form.cleaned_data['nickname']
            login(request, user)
            return redirect('cal:tutorial1')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/join.html', {'form': form})

def join_form(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'account/join.html', {'form': form})
    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            nickname = form.cleaned_data['nickname']
            login(request, user)
            return redirect('index')
    return render(request, 'account/join.html', {'form': form})

def index(request):
    return render(request, 'account/index.html')