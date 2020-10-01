def digit(x,y):
    if x>y:
        return x
    else:
        return y
    

def greatest(a,b,c):
    # bigger = digit(a,b)
    # return digit(bigger,c)
    return digit(digit(a,b),c)
print(greatest(211,31,8))
