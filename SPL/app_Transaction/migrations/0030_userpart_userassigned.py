# Generated by Django 2.0.1 on 2018-01-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Transaction', '0029_remove_userpart_userassigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpart',
            name='userAssigned',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]