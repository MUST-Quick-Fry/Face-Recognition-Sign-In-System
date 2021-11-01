from django.db import models

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



