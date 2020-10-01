def func(f):
    for i in range(1,f+1):
        if  i%2==0:
            yield(i)
        else:
            pass
for j in func(10):
    print(j)