# Generated by Django 3.2.5 on 2022-02-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_testimonialmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialmodel',
            name='photo',
            field=models.ImageField(null=True, upload_to='testimoni/', verbose_name='Photo'),
        ),
    ]
