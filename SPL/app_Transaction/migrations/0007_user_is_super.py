# Generated by Django 2.0.3 on 2018-04-01 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Transaction', '0006_auto_20180331_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_super',
            field=models.BooleanField(default=False),
        ),
    ]
