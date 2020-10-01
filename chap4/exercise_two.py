def greater(a,b,c):
    if a>b and a>c:
        return a
    else:
        if b>a and b>c:
            return b
        else:
            return c
num1 = input('enter num 1 : ')
num2 = input('enter num 2 : ')
num3 = input('enter num 3 : ')
print(greater(num1,num2,num3))
