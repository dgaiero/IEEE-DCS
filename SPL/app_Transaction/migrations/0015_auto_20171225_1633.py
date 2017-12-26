# Generated by Django 2.0 on 2017-12-26 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Transaction', '0014_auto_20171225_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_Email',
            new_name='cal_Poly_Email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_Name_Text',
            new_name='last_Name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_Phone_Number',
            new_name='phone_Number',
        ),
        migrations.AlterField(
            model_name='log',
            name='date_And_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 25, 16, 33, 7, 969634)),
        ),
    ]