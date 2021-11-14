from django.conf.urls import url
from django.urls import path, re_path
from . import views

# namespace

app_name = 'tasks'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/',views.api,name='api'),
    path('sign_in_records/', views.sign_in_records, name='sign_in_records'),
    path('retroactive_records/', views.retroactive_records, name='retroactive_records'),
]
