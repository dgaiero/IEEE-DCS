# Reading parts CSV file, making them Django objects, and storing them in a database

# Bypassing manage.py
# Set DJANGO_SETTINGS_MODULE enviroment variable to SPL.settings
import os
os.environ['DJANGO_SETTINGS_MODULE']='SPL.settings'

import django
django.setup()

import csv
from app_Transaction.models import Part

# Take parts in CSV file, create Django parts objects, and save them in database
with open('splParts.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        p = Part(part_Name_Text=row[0])
        p.save()
