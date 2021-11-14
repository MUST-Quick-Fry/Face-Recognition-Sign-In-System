from django.contrib import admin
from simpleui import forms

# Register your models here.

admin.site.site_header = 'MUST Information Management System'  # header
admin.site.site_title = 'MUST Information Management System'  # title
admin.site.index_title = 'MUST Information Management System'

from .models import *

admin.site.register(Task)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # display para
    list_display = ('cid','name','weekday','start_time','finish_time')
    list_per_page = 10
    search_fields = ('cid','name')
    actions_on_top = True


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # display para
    list_display = ('sid','stu_name','img_path')
    list_per_page = 10
    search_fields = ('sid','stu_name')
    actions_on_top = True


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # display para
    list_display = ('name','account','pwd')
    list_per_page = 10
    search_fields = ('tid','name')
    actions_on_top = True


@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    # display para
    list_display = ('sid','cid','time')
    list_per_page = 10
    search_fields = ('sid','time')
    actions_on_top = True


@admin.register(TakeClass)
class TakeClassAdmin(admin.ModelAdmin):
    # display para
    list_display = ('sid','cid')
    list_per_page = 10
    search_fields = ('sid','cid')
    actions_on_top = True