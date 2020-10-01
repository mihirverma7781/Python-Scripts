from functools import wraps


def print_func_data(func):
    @wraps(func)
    def wrapper_function(*args,**kwargs):
        print(func.__doc__)
        print('You are calling add function')
        return func(*args,**kwargs)
    return wrapper_function




@print_func_data
def add(a,b):
    '''this func takes two numbers as arguments and return their sum'''
    return a+b 

print(add(2,3))