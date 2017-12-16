from django.db import models
import datetime

class Part(models.Model):
    part_Name_Text              = models.CharField(max_length=100)
    quantity_Number             = models.IntegerField(default=0)
    quantity_Checked_Out_Number = models.IntegerField(default=0)
    #ID                  = models.IntegerField(blank=True, null=True)

class User(models.Model):
    first_Name_text     = models.CharField(max_length=100)
    last_Name_text      = models.CharField(max_length=100)
    user_Type_text      = models.CharField(max_length=100)
    iso_Number          = models.IntegerField(default=0)
    library_Code_Number = models.IntegerField(default=0)
    parts               = models.ManyToManyField(Part)

class Transaction(models.Model):
    #userid
    #part
    #date
    pass

class Lab(models.Model):
    course_Name_Text = models.CharField(max_length=100)
    section_Number   = models.IntegerField(default=0)
    week_Number      = models.IntegerField(default=0)

class Log(models.Model):
    #date_And_Time        = models.DateTimeField(default=datetime.now(), blank=True)
    client_Name_text     = models.CharField(max_length=100)
    tech_Name_text       = models.CharField(max_length=100)
    #part checked out
    quantity_Number      = models.IntegerField(default=0)
    transaction_Complete = models.BooleanField(default=False)
