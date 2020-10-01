# *args with normal parameters

def multiplynums(num,*args):
    multiply =1
    print(num)
    print(args)
    for i in args:
        multiply = multiply*i
    return multiply
print(multiplynums(2,3,4))