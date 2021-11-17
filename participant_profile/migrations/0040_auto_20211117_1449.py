# Generated by Django 3.2.5 on 2021-11-17 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_profile', '0039_alter_participantprofile_nisn'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantprofile',
            name='special_needs',
            field=models.CharField(choices=[('Y', 'Ya, Berkebutuhan Khusus'), ('N', 'Tidak Berkebutuhan Khusus')], default='N', help_text='Apakah Anda memilika kebutuhan khusus?', max_length=1, verbose_name='Berkebutuhan Khusus'),
        ),
        migrations.AddField(
            model_name='participantprofile',
            name='special_needs_text',
            field=models.TextField(blank=True, help_text='Jelaskan seperti apa kebutuhan khusus Anda.', null=True, verbose_name='Penjelasan Kebutuhan Khusus Anda'),
        ),
    ]
