# Generated by Django 3.2.12 on 2022-07-14 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imgtemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='模板名称')),
                ('img_template', models.FileField(max_length=128, upload_to='TemplateLib/', verbose_name='模板图片')),
            ],
        ),
    ]
