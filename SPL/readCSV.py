# Reading parts CSV file, making them Django objects, and storing them in a database

import datetime
# Bypassing manage.py
# Set DJANGO_SETTINGS_MODULE enviroment variable to SPL.settings
import os

os.environ['DJANGO_SETTINGS_MODULE']='SPL.settings'

import django
django.setup()

import csv
from app_Transaction.models import User
from django.core.exceptions import ObjectDoesNotExist

# Take parts in CSV file, create Django parts objects, and save them in database
with open('member_detail.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        member_number = row[0]
        first_name = row[2]
        last_name = row[1]
        email = row[3]
        expire_date = datetime.datetime.strptime(row[4], "%m/%d/%Y")
        try:
            current_user = User.objects.get(ieee_member_number=member_number)
            current_user.createUserType()
            print(f"USER: {first_name} {last_name} EXISTS")
        except ObjectDoesNotExist:
            print(f"#{member_number} | Name: {first_name} {last_name} | Email: {email} | Expire: {expire_date}")
            new_user = User(first_Name=first_name, last_Name=last_name, cal_Poly_Email=email,
                            ieee_member_number=member_number, ieee_member_expiration_date=expire_date)
            new_user.save()
        # p = Part(part_Name_Text=row[0])
        # p.save()
