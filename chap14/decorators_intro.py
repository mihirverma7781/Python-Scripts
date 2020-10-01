# decorators --> enhances functionality of other functions

# @ used for decorators

def decoratr_function(any_function):
    def wrapper_function():
        print('this is awesone function')
        any_function()
    return wrapper_function

@decoratr_function #enhances the functionality
def func1():
    print('this is function 1')
@decoratr_function #enhances the functionality
def func2():
    print('this is function 2')


func1()
func2()


# s = decoratr_function(func1)
# s()