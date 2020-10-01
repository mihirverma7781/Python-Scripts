def check(l):
    count = 0
    for i in l:
        if type(i) == list:
            count = count+1
        else:
            pass
    print(count)

li =[[1,2,3],1,4,['mihir','verma'],[2,4,6],1]
check(li)
