# *args with normal parameters

def multiplynums(*args):
    multiply =1
    print(args)
    for i in args:
        multiply = multiply*i
    return multiply
num1 =[2,3,4]
print(multiplynums(*num1)) #here we passed for unpacking