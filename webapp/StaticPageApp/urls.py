from django.urls import path
from . import views

app_name = 'StaticPageApp'
urlpatterns = [
    path('', views.landing, name='landing'),
]