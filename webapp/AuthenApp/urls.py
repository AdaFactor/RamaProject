from django.urls import path
from . import views

app_name = 'AuthenApp'
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('warning/', views.warning, name='warning'),
    path('member/', views.member, name='member'),    
]