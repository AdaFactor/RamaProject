from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('demo/', views.demo, name='demo'),
    path('new_member/', views.new_member, name='new_member'),
]