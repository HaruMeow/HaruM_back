from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from .forms import UserRegistrationForm, UserLoginForm




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
    return render(request, 'account/join.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def join_view(request):
    return render(request, 'account/join.html')