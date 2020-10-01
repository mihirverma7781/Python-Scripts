from functools import wraps
def only_datatype_allow(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            if all([type(i)==datatype for i in args]):
                return func(*args,**kwargs)
            print('invalid arguments')
        return wrapper_function
    return decorator
@only_datatype_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string+=i
    return string
print(string_join('mihir',' sunil',' verma'))