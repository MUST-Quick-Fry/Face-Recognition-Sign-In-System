# Generated by Django 3.2.7 on 2021-11-14 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('weekday', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.BigAutoField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=50)),
                ('img_path', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Task Name')),
                ('status', models.CharField(choices=[('u', 'Not started'), ('o', 'ongoing'), ('f', 'Finished')], max_length=1, verbose_name='Status Name')),
            ],
            options={
                'verbose_name': 'Our Task',
                'verbose_name_plural': 'Our Task',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('account', models.CharField(max_length=50, unique=True)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SignIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.course')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.teacher'),
        ),
    ]
