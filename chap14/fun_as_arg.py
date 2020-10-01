# function as an argument

l = [1,2,3,4]

def square(a):
    return a**2

# l = list(map(square,l))
# print(l)

def my_map(func,l):
    m = []
    for item in l:
        m.append(func(item))
    return m

print(my_map(lambda a: a**2,l))

# def mm(func,k):
#     li = [a**2 for a in l]
#     print(li)

# mm(l) 