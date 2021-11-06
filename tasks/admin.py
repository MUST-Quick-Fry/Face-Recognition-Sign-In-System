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
    list_display = ('id', 'name', 'weekday', 'start_time', 'finish_time')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = True

