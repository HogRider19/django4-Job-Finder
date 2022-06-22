from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'userProfile/signup.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(
                    request,
                    'userProfile/signup.html',
                    {'form':UserCreationForm(), 'error':'Имя пользователя уже занято'}
                )
        else:
            return render(
                request,
                'userProfile/signup.html',
                {'form':UserCreationForm(), 'error':'Введенные пароли не совпадают'}
            )


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'userProfile/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            return render(request, 'userProfile/login.html', {'form':AuthenticationForm(), 'error':'Неправельный логин или пароль'})
        else:
            login(request, user)
            return redirect('home') 


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
