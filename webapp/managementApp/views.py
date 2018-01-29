from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'managementApp/index.html')


def landing(request):
    return render(request, 'managementApp/landing.html')


def demo(request):
    return render(request, 'managementApp/demo_tree.html')