from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.models import UserProfile
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
    return render(request, 'account/join.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@require_POST
def join_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['id']
            password = form.cleaned_data['password']
            nickname = form.cleaned_data['nickname']
            login(request, user)
            # POST 요청이 완료되면 GET 요청으로 index로 이동
            return redirect('index')

    # GET 요청에 대한 처리
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
            username = form.cleaned_data['id']
            password = form.cleaned_data['password']
            nickname = form.cleaned_data['nickname']
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/join.html', {'form': form})