def even_odd(l):
    empty=[[],[]]
    for i in l:
        if i%2==0:
            empty[0].append(i)
        else:
            empty[1].append(i)
    return empty
number = list(range(1,11))
print(even_odd(number))

