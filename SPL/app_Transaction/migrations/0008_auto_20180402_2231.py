# Generated by Django 2.0.3 on 2018-04-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Transaction', '0007_user_is_super'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cal_Poly_Email',
            field=models.EmailField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ieee_member_number',
            field=models.CharField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='polyCard_Data',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
    ]
