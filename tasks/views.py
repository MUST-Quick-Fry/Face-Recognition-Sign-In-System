from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Task


# Create your views here.
def dashboard(request):
    user_count = User.objects.count()
    task_count = Task.objects.count()

    context = {'user_count': user_count, 'task_count': task_count}
    return render(request, 'tasks/dashboard.html', context)
