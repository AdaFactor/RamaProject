from django.shortcuts import render, redirect
from django.core.mail import send_mail
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

def login(request):
    return render(request, 'AuthenApp/login.html')
