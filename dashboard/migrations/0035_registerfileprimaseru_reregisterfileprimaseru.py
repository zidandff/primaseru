# Generated by Django 3.2.5 on 2021-08-27 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_auto_20210826_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterFilePrimaseru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100, verbose_name='Nama Berkas')),
            ],
        ),
        migrations.CreateModel(
            name='ReRegisterFilePrimaseru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100, verbose_name='Nama Berkas')),
            ],
        ),
    ]