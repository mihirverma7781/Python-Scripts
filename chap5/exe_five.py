def cmp_list(l,m):
    empty = []
    for i in l:
        if i in m:
            empty.append(i)
            
        else:
            pass
    return empty
            
        
num1 = list(range(1,6))
num2 = list(range(4,11))
print(cmp_list(num1,num2))