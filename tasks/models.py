from django.db import models
from django.utils import timezone


# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', 'Not started'
    ONGOING = 'o', 'ongoing'
    FINISHED = 'f', 'Finished'


class Task(models.Model):
    name = models.CharField(verbose_name = 'Task Name', max_length = 50, unique = True)
    status = models.CharField(verbose_name = 'Status Name', max_length = 1, choices = Status.choices)

    class Meta:
        verbose_name = 'Our Task'
        verbose_name_plural = 'Our Task'

    def __str__(self):
        return self.name


class Course(models.Model):
    cid = models.BigAutoField(primary_key = True)
    tid = models.ForeignKey('Teacher', on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    weekday = models.IntegerField(choices = zip(range(1,8),range(1,8)),blank=True)
    start_time = models.TimeField()
    finish_time = models.TimeField()

    def __str__(self):
        return self.name


class Student(models.Model):
    sid = models.CharField(max_length = 50, primary_key = True)
    stu_name = models.CharField(max_length = 50)
    img_path = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return "{}({})".format(self.stu_name,self.sid)


class Teacher(models.Model):
    tid = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    account = models.CharField(max_length = 50, unique = True)
    pwd = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class SignIn(models.Model):
    sid = models.ForeignKey('Student', on_delete = models.CASCADE)
    cid = models.ForeignKey('Course', on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now = True)


class TakeClass(models.Model):
    sid = models.ForeignKey('Student', on_delete = models.CASCADE)
    cid = models.ForeignKey('Course', on_delete = models.CASCADE)

    class Meta:
        unique_together = (("sid", "cid"),)
