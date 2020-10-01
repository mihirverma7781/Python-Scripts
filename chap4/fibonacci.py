def fibonacci(num):
    p=0
    i=0
    j=1
    if num == 1:
        print(i)
    elif num == 2:
        print(i, j)
    else:
        print(i,j,end=" ")
        for p in range(num-2):
            
            k=i+j
            i=j
            j=k
            print(j , end=" ")
fibonacci(10)