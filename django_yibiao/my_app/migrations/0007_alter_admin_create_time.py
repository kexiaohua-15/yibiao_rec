# Generated by Django 3.2.12 on 2022-07-15 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20220715_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2022, 7, 15, 11, 44, 27, 4908), verbose_name='创建时间'),
        ),
    ]
