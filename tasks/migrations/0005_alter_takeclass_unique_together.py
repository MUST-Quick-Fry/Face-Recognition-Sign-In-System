# Generated by Django 3.2.7 on 2021-11-14 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_takeclass'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='takeclass',
            unique_together={('sid', 'cid')},
        ),
    ]
