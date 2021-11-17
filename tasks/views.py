from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Task, SignIn, Course, Student, Teacher, TakeClass
import json
import datetime


# Create your views here.
def dashboard(request):
    user_count = User.objects.count()
    task_count = Task.objects.count()

    context = {'user_count': user_count, 'task_count': task_count}
    return render(request, 'tasks/dashboard.html', context)


def sign_in_records(request):
    course = Course.objects.all()
    sign_in = SignIn.objects.all()
    student = Student.objects.all()
    take_class = TakeClass.objects.all()

    context = {'all_course': course,
               'all_sign_in': sign_in,
               'all_students': student,
               'all_take_class': take_class}
    return render(request, 'tasks/sign_in.html', context)


# def retroactive_records(request):
#     return render(request, 'tasks/retroactive.html')


def api(request):
    cid = request.GET.get('cid')
    course = Course.objects.all().filter(cid = cid)[0]
    take_class = TakeClass.objects.all().filter(cid = cid)
    total_student = len(take_class)

    start_time = course.start_time
    finish_time = course.finish_time

    date = datetime.datetime.strptime(request.GET.get('date'), '%Y-%m-%d')
    start = datetime.datetime(date.year, date.month, date.day,
                              start_time.hour,
                              start_time.minute,
                              start_time.second)
    end = datetime.datetime(date.year, date.month, date.day,
                            finish_time.hour,
                            finish_time.minute,
                            finish_time.second)
    sign_in = SignIn.objects.all().filter(cid = cid, time__range = [date, start])
    late_sign_in=SignIn.objects.all().filter(cid=cid,time__range=[start,end])

    signed = []
    late=[]
    for row in sign_in:
        signed.append(row.sid)
    for row in late_sign_in:
        if row.sid not in signed:
            late.append(row.sid)
    sign_in_num = len(set(signed))
    late_num=len(set(late))

    statistics = {
        'total_student': total_student,
        'sign_in_num': sign_in_num,
        'late_num': late_num,
        'not_sign_in_num': total_student - sign_in_num - late_num,
        'percentage': round(sign_in_num / total_student * 100),
        'late_percentage': round(late_num / total_student * 100)
    }
    return HttpResponse(json.dumps(statistics))
