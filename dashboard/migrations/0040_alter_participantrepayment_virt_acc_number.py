# Generated by Django 3.2.5 on 2021-08-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_paymentbanner_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantrepayment',
            name='virt_acc_number',
            field=models.CharField(help_text='Nomor Virtual Account Bank Mandiri.', max_length=30, null=True, verbose_name='Nomor Virtual Account'),
        ),
    ]