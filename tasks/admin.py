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
    list_display = ['cid', 'name', 'weekday', 'start_time', 'finish_time']
    list_per_page = 10
    search_fields = ('name',)
    actions_on_top = True


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # display para
    list_display = ['sid', 'stu_name', 'img_path']
    list_per_page = 10
    search_fields = ('sid',)
    actions_on_top = True


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # display para
    list_display = ['name', 'account', 'pwd']
    list_per_page = 10
    search_fields = ('tid', 'name')
    actions_on_top = True


@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    # display para
    list_display = ['student_id', 'student_name', 'course_name', 'time']
    list_per_page = 10
    search_fields = ('sid__sid', 'cid__name')
    actions_on_top = True

    def course_name(self, obj):
        return "weekday {} : {}".format(obj.cid.weekday, obj.cid.name)

    def student_name(self, obj):
        return obj.sid.stu_name

    def student_id(self, obj):
        return obj.sid.sid

    student_id.admin_order_field = 'sid__sid'
    student_name.admin_order_field = 'sid__stu_name'
    course_name.admin_order_field = 'cid__name'


@admin.register(TakeClass)
class TakeClassAdmin(admin.ModelAdmin):
    # display para
    list_display = ['student_id', 'student_name', 'course_name']
    list_per_page = 10
    search_fields = ('sid__sid', 'cid__name', 'sid__name')
    actions_on_top = True

    def course_name(self, obj):
        return obj.cid.name

    def student_name(self, obj):
        return obj.sid.stu_name

    def student_id(self, obj):
        return obj.sid.sid

    student_id.admin_order_field = 'sid__sid'
    student_name.admin_order_field = 'sid__stu_name'
    course_name.admin_order_field = 'cid__name'
