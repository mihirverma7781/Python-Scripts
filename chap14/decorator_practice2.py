
def only_int_allow(func):
    def wrapper_function(*args,**kwargs):
        if all([type(i)==int for i in args]):
            return func(*args,*kwargs)
        print('invalid arguments')
    return wrapper_function
        

    #     datatype = []
    #     for i in args:
    #         datatype.append(type(i)==int)
    #     if all(datatype):
    #         return func(*args,*kwargs)
    #     else:
    #         print('invalid arguments')
    # return wrapper_function
    
@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1,2,3,4,'mihir'))