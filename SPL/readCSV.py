# Reading parts CSV file, making them Django objects, and storing them in a database

import csv

import os
os.environ['DJANGO_SETTINGS_MODULE']='SPL.settings'

import django
django.setup()

from app_Transaction.models import Part

with open('splParts.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        p = Part(part_Name_Text=row[0])
        p.save()
