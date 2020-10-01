def any_sum(*args):
    if all([(type(arg)==int or type(arg)== float) for arg in args]):
        total = 0
        for i in args:
            total =total+i
        return total
    else:
        print('wrong input')

print(any_sum(1,2,3,4))