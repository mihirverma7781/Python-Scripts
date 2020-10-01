def add(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    else:
        raise TypeError('you have passed invalid type of value')

print(add('2','3'))