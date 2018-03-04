from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Member
from MemberApp.forms import RegistrationForm, AddressForm


@login_required
def profile(request):
    return render(request, 'MemberApp/profile.html')

# @login_required
def registration(request):
    if request.POST:
        new_member = Member()
        new_member.create_from_post(request.POST)
        new_member.clean()
        new_member.save()      
        return redirect('StaticPageApp:landing')

    return render(request, 'MemberApp/registration.html')
