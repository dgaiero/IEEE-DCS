# Generated by Django 2.0 on 2017-12-19 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolyCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polyCard_Data_Text', models.CharField(max_length=100)),
                ('iso_Number', models.IntegerField(null=True)),
                ('library_Code_Number', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='log',
            old_name='client_Name_text',
            new_name='client_Name_Text',
        ),
        migrations.RenameField(
            model_name='log',
            old_name='tech_Name_text',
            new_name='tech_Name_Text',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_Name_text',
            new_name='first_Name_Text',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_Name_text',
            new_name='last_Name_Text',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_Type_text',
            new_name='user_Type_Text',
        ),
        migrations.RemoveField(
            model_name='log',
            name='quantity_Number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='iso_Number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='library_Code_Number',
        ),
        migrations.AddField(
            model_name='lab',
            name='parts',
            field=models.ManyToManyField(to='app_Transaction.Part'),
        ),
        migrations.AddField(
            model_name='log',
            name='date_And_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 12, 19, 1, 13, 26, 465417)),
        ),
        migrations.AddField(
            model_name='log',
            name='parts',
            field=models.ManyToManyField(to='app_Transaction.Part'),
        ),
        migrations.AddField(
            model_name='part',
            name='id_Number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_Email',
            field=models.EmailField(max_length=100, null=True, verbose_name='Email'),
        ),
    ]