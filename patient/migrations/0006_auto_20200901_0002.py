# Generated by Django 3.1 on 2020-08-31 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_auto_20200831_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='intervention',
            field=models.CharField(default='intervention', max_length=250),
        ),
    ]