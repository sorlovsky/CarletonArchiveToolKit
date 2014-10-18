import csv, os

#create parent directory

#reading digital content
with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        os.mkdir(row[0])