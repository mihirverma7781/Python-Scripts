from csv import writer

with open('file3.csv','w',newline="") as f:
    csv_writer = writer(f)

    # write row
    # write rows
    csv_writer.writerow(['name','phone'])
    csv_writer.writerow(['najnji','44444'])
    csv_writer.writerow(['naka','54354'])
    csv_writer.writerow(['nanu','65856'])

    csv_writer.writerows([['name','phone'],['najnji','44444']])