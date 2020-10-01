from csv import DictWriter

with open('final.csv','w',newline="") as f:
    csv_writer = DictWriter(f, fieldnames=['fname','lname','age'])
    csv_writer.writeheader()

    # wite row 
    # rite rows
#     csv_writer.writerow(
# {
#     'fname':'mihir',
#     'lname':'verma',
#     'age': 19
# } )

    csv_writer.writerows([
        {'fname':'mohit','lname':'bist','age':7},
        {'fname':'mihir','lname':'verma','age': 19}
        ])