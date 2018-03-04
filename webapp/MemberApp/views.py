from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'MemberApp/profile.html')

@login_required
def registration(request):
    if request.POST:
        form = RegistrationForm(request, data=request.POST)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.expiry_date = new_member.cal_expiry_date()
            new_member.save()
            # Email Module
            # send_mail(
            #     'Ada Test Email System',
            #     'Testing massage is ready for Email system',
            #     'arkane.ka@adafactor.com',
            #     ['adadesions@gmail.com'],
            #     fail_silently=False
            # )
            return redirect('StaticPageApp:landing')

    return render(request, 'MemberApp/registration.html')
