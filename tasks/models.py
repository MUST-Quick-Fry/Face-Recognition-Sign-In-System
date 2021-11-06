from django.db import models
from django.utils import timezone


# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', 'Not started'
    ONGOING = 'o', 'ongoing'
    FINISHED = 'f', 'Finished'


class Task(models.Model):
    name = models.CharField(verbose_name='Task Name', max_length=50, unique=True)
    status = models.CharField(verbose_name='Status Name', max_length=1, choices=Status.choices)

    class Meta:
        verbose_name = 'Our Task'
        verbose_name_plural = 'Our Task'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(verbose_name='Course Name', max_length=80)
    # teacher_id = models.ForeignKey(on_delete=models.SET_NULL, blank=False, null=True, verbose_name='Teacher ID',
    # db_index=True)
    weekday = models.IntegerField(verbose_name='Weekday')
    start_time = models.TimeField(verbose_name='Start Time', auto_now=True)
    finish_time = models.TimeField(verbose_name='Finish Time', auto_now=True)

    def __str__(self):
        return self.name
