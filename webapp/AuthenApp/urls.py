from django.urls import path
from . import views

app_name = 'AuthenApp'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('warning/', views.warning, name='warning'),
    path('member/', views.member, name='member'),    
]