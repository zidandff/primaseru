# Generated by Django 3.2.5 on 2021-08-13 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant_profile', '0007_alter_majorstudent_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='majorstudent',
            name='info',
        ),
    ]
