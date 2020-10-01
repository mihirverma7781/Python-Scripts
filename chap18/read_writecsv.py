from csv import DictReader
from csv import DictWriter

with open('file.csv','r') as rf:
    with open('final.csv','w',newline="") as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['first_name','email','phone'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,email,phone,  = row['name'],row['email'],row['phone']
            csv_writer.writerow({'first_name' : fname,
            'email':email,
            'phone':phone
            
            })