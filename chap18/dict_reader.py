from csv import DictReader

with open('file.csv','r') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row['name'])