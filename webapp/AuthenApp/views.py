from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm

def registration(request):
    if request.POST:
        form = RegistrationForm(request, data=request.POST)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.expiry_date = new_member.cal_expiry_date()
            new_member.save()
            send_mail(
                'Ada Test Email System',
                'Testing massage is ready for Email system',
                'arkane.ka@adafactor.com',
                ['adadesions@gmail.com'],
                fail_silently=False
            )
            return redirect('StaticPageApp:landing')
            
    form = RegistrationForm(request)
    return render(request, 'AuthenApp/registration.html', {'form': form})

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
