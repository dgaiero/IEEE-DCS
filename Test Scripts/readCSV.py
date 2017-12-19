# Reading parts CSV file, making them Django objects, and storing them in a database
# Author: Russell Caletena
# Date Created: 12/17/17

# Helpful link: https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
import csv
'''
# Need to see how this import works:
from SPL.app_Transaction.models import Part
'''
with open('splParts.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        p = Part("part_Name_Text='{}'".format(row[0]))
        p.save()
