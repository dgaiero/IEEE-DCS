# Generated by Django 2.0 on 2017-12-19 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Transaction', '0002_auto_20171219_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date_And_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 19, 1, 16, 29, 376765)),
        ),
    ]