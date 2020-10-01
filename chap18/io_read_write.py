with open('file2.txt',"r") as rf:
    with open('file1.txt', 'a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f"{name} ---> {salary}")