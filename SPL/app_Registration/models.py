from django.db import models

class First_Name(models.Model):
    first_Name_text = models.CharField(max_length=30)

class Last_Name(models.Model):
    last_Name_text = models.CharField(max_length=30)

class Cal_Poly_Email(models.Model):
    cal_Poly_Email = models.CharField(max_length=50)

class Phone_Number(models.Model):
    phone_Number = models.CharField(max_length=15)

class Poly_Card_Data(models.Model):
    poly_Card_Data = models.CharField(max_length=30)
