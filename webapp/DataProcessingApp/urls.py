from django.urls import path
from . import views

app_name = 'DataProcessingApp'
urlpatterns = [
    path('report/', views.report, name='report'),
]