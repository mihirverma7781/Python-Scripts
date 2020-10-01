number = list(range(1,11))
def square(l):
    empty=[]
    for i in l:
        empty.append(i*i)
    return empty

print(square(number))