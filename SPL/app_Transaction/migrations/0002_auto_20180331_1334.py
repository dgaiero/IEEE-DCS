# Generated by Django 2.0.3 on 2018-03-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ieee_member_expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ieee_member_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='parts',
            field=models.ManyToManyField(blank=True, null=True, to='app_Transaction.Part'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_Number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
