from django.conf.urls import url
from django.urls import path, re_path
from . import views

# namespace

app_name = 'tasks'

urlpatterns = [
    path('tasks/dashboard/', views.dashboard, name='dashboard'),
]
