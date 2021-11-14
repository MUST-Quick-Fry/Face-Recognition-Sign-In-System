from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Task ,SignIn ,Course ,Student ,Teacher ,TakeClass
import json

# Create your views here.
def dashboard(request):
    user_count = User.objects.count()
    task_count = Task.objects.count()

    context = {'user_count': user_count ,'task_count': task_count}
    return render(request ,'tasks/dashboard.html' ,context)


def sign_in_records(request):
    course = Course.objects.all()
    sign_in = SignIn.objects.all()
    student = Student.objects.all()
    take_class = TakeClass.objects.all()

    context = {'all_course': course ,
               'all_sign_in': sign_in ,
               'all_students': student ,
               'all_take_class': take_class}
    return render(request ,'tasks/sign_in.html' ,context)


def retroactive_records(request):
    return render(request ,'tasks/retroactive.html')


def api(request):
    cid = request.GET.get('cid')

    course = Course.objects.all().filter(cid=cid)[0]
    take_class = TakeClass.objects.all().filter(cid=cid)

    start_time = course.start_time
    finish_time = course.finish_time

    date = request.GET.get('date')
    print(date)
    # start=date+start_time
    # end=date+finish_time
    # print(start)
    # print(end)
    # sign_in = SignIn.objects.all().filter(cid=cid,time__gte=start,time__lte=end)
    # print(sign_in)

    total_student=len(take_class)
    # for row in sign_in:
    #     print(row.time)
    #     if row.time<finish_time and row.time>finish_time:
    #         print(row)

    sign_in_num=1
    statistics = {
        'total_student':total_student,
        'sign_in_num':sign_in_num,
        'not_sign_in_num':total_student-sign_in_num,
        'percentage':round(sign_in_num/total_student*100)
    }
    return HttpResponse(json.dumps(statistics))
