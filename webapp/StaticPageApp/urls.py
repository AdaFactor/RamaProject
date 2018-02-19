from django.urls import path
from . import views

app_name = 'StaticPageApp'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('demo/', views.demo, name='demo'),
    path('adminmenu/', views.adminmenu, name='adminmenu'),
    
]