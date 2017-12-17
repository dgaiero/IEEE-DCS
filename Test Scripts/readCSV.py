# Reading parts CSV file, making them Django objects, and storing them in a database
# Author: Russell Caletena
# Date Created: 12/17/17

# Helpful link: https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
import csv

with open('splParts.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print (row)
