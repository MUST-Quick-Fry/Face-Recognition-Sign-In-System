from django.contrib import admin

# Register your models here.

admin.site.site_header = 'MUST Information Management System'  # header
admin.site.site_title = 'MUST Information Management System'  # title
admin.site.index_title = 'MUST Information Management System'

from .models import Task

admin.site.register(Task)
