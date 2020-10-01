# scope
x=5 #global variable
def func():
    global x #operating on global variable
    x=7 # local variable
    return x 
# def func2():
#     print(x)
print(x)
print(func()) 
print(x)