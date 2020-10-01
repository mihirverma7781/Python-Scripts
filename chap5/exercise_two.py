def reverse_list(l):
    empty = []
    for i in range(len(l)):
    # l.reverse() will not return anything
    # return l use this
    # return l[::-1]
        num = l.pop()
        empty.append(num)
    return empty
    
number = list(range(1,11))
print(reverse_list(number))
        