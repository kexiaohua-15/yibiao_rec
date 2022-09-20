# Generated by Django 3.2.12 on 2022-07-22 07:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_auto_20220722_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2022, 7, 22, 7, 2, 54, 286528, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='welldanger',
            name='imgRec',
            field=models.FileField(max_length=128, upload_to='yolov5_master/number/', verbose_name='识别图片'),
        ),
    ]