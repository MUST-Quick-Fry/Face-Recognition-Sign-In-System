# Generated by Django 3.2.7 on 2021-11-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
