from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Member
# from .forms import MemberForm
from datetime import date


def index(request):
    return render(request, 'StaticPageApp/index.html')


def landing(request):
    return render(request, 'StaticPageApp/landing.html')


def demo(request):
    return render(request, 'StaticPageApp/demo_tree.html')

# def new_member(request):
#     if request.POST:
#         form = MemberForm(request, data=request.POST)
#         if form.is_valid():
#             new_member = form.save(commit=False)
#             new_member.expiry_date = new_member.cal_expiry_date()
#             new_member.save()
#             return redirect('landing')
            
#     form = MemberForm(request)
#     return render(request, 'StaticPageApp/new_member.html', {'form': form})