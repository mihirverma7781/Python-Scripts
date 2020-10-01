# decorators --> enhances functionality of other functions

# @ used for decorators
from functools import wraps
def decoratr_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        '''this is wrapper function'''
        print('this is awesone function')
        return any_function(*args, **kwargs)
    return wrapper_function

@decoratr_function #enhances the functionality
def func(a):
    print(f'argument ---> {a}')

func(7)
@decoratr_function
def add(a,b):
    '''this is add function'''
    return a+b
print(add(2,3))

print(add.__doc__)