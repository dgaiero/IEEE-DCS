# Generated by Django 2.0 on 2017-12-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_Name_Text', models.CharField(max_length=100)),
                ('section_Number', models.IntegerField(default=0)),
                ('week_Number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_Name_text', models.CharField(max_length=100)),
                ('tech_Name_text', models.CharField(max_length=100)),
                ('quantity_Number', models.IntegerField(default=0)),
                ('transaction_Complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_Name_Text', models.CharField(max_length=100)),
                ('quantity_Number', models.IntegerField(default=0)),
                ('quantity_Checked_Out_Number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name_text', models.CharField(max_length=100)),
                ('last_Name_text', models.CharField(max_length=100)),
                ('user_Type_text', models.CharField(max_length=100)),
                ('iso_Number', models.IntegerField(default=0)),
                ('library_Code_Number', models.IntegerField(default=0)),
                ('parts', models.ManyToManyField(to='app_Transaction.Part')),
            ],
        ),
    ]