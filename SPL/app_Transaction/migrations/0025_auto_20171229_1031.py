# Generated by Django 2.1 on 2017-12-29 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Transaction', '0024_auto_20171229_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date_And_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 29, 10, 31, 48, 321401)),
        ),
    ]