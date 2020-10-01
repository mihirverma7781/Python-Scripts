# l = [1,2,3,4]

# def square(a):
#     return a**2

def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func

s = outer_func()
s() #executing inner function

def outer_func2(msg):
    def inner_func2():
        print(f'message ----> {msg}')
    return inner_func2

m = outer_func2('this is outer function !')
m()
