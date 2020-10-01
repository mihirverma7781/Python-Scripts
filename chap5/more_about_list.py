# generate lists with range function

numbers = list(range(1,11))
print(numbers)

#something more about pop method
poped = print(numbers.pop())
print(numbers)

# index method

print(numbers.index(5))

# function in list

def negative(l):
    empty =[]
    for i in l:
        empty.append(-i)
    return empty
print(negative(numbers))  
