from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout

def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/member/profile')

    return render(request, 'AuthenApp/login.html')

def signout(request):
    logout(request)
    return redirect('/')

def warning(request):
    return render(request, 'AuthenApp/warning.html')

def member(request):
    return render(request, 'AuthenApp/member.html')