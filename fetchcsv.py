import csv
import urllib

url = 'https://docs.google.com/spreadsheets/d/1Oqb9g4mY9L6N6UWeU4gNB-MrLmOzqaht5S3enYOswj4/edit?usp=sharing'
response = urllib.urlopen(url)
with open(response, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))