from django.db import models
import datetime

# Create Part model with necessary attributes
class Part(models.Model):
    part_Name_Text              = models.CharField(max_length=100)
    quantity_Number             = models.IntegerField(default=0)
    quantity_Checked_Out_Number = models.IntegerField(default=0)
    id_Number                   = models.IntegerField(blank=True, null=True)

# Create User model with necessary attributes
class User(models.Model):
    first_Name_text     = models.CharField(max_length=100)
    last_Name_text      = models.CharField(max_length=100)
    user_Type_text      = models.CharField(max_length=100)
    user_email          = models.CharField(max_length=100)
    iso_Number          = models.IntegerField(default=0)
    library_Code_Number = models.IntegerField(default=0)
    parts               = models.ManyToManyField(Part)

# Create Transaction model with necessary attributes
# We'll worry about this later...
# What is the difference between transaction and log?
class Transaction(models.Model):
    #userid
    #part
    #date
    pass

# Create Lab model with necessary attributes
class Lab(models.Model):
    course_Name_Text = models.CharField(max_length=100)
    section_Number   = models.IntegerField(default=0)
    week_Number      = models.IntegerField(default=0)
    parts            = models.ManyToManyField(Part)
    # possible things to add: professor name

# Create Log model with necessary attributes
class Log(models.Model):
    date_And_Time        = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    client_Name_text     = models.CharField(max_length=100)
    tech_Name_text       = models.CharField(max_length=100)
    parts                = models.ManyToManyField(Part)
    transaction_Complete = models.BooleanField(default=False)
