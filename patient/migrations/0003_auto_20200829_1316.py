# Generated by Django 3.1 on 2020-08-29 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20200829_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='asa',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mallampati',
        ),
    ]
