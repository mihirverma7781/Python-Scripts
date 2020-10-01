with open('file1.txt','r') as rea:
    with open('file2.txt','a') as appe:
        appe.write(rea.read())
