# Generated by Django 3.2.5 on 2021-08-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_auto_20210815_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosourceppdb',
            name='info_source',
            field=models.CharField(max_length=100, unique=True, verbose_name='Sumber Info Primaseru'),
        ),
    ]