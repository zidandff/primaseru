# Generated by Django 3.2.5 on 2021-08-27 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_profile', '0017_auto_20210825_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfileparticipant',
            name='semester',
            field=models.CharField(choices=[('SEM_1', 'Semester 1'), ('SEM_2', 'Semester 2'), ('SEM_3', 'Semester 3'), ('SEM_4', 'Semester 4')], help_text='Pilih raport semester berapa yang di unggah.', max_length=5, verbose_name='Raport Semester'),
        ),
    ]
