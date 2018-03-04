from django.urls import path
from . import views

app_name = 'MemberApp'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
]