from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

import logging

def home(request):
    return render(request, "home/index.html")

def login(request):
    if request.user.is_authenticated:  # 로그인 후 로그인 페이지 막기 위함
        return redirect('accounts:home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('accounts:home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.user.is_authenticated:  # 로그인 후 회원가입 페이지 막기 위함
        return redirect('accounts:home')

    if request.method == "POST":

        if User.objects.filter(username=request.POST["username"]).exists():
            return render(request, 'accounts/signup.html', {'error': 'username is Duplicate'})


        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request, user)
            return redirect('accounts:home')
        return render(request, "accounts/signup.html", {'pwd_error': 'The passwords are different.'} )

    return render(request, "accounts/signup.html")

def logout(request):
    auth.logout(request)
    return redirect('accounts:home')



