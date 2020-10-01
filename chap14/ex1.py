import time

def calculate_time(func):
    def wrapper_function(*args,**kwargs):
        print(f'executing .... square finder')
        t1= time.time()
        returned_value = func(*args,**kwargs)
        t2= time.time()
        total = t2-t1
        print(f"time --> {total} sec")
        return returned_value
    return wrapper_function

@calculate_time
def add(a):
    l = [i**10 for i in range(1,a+1)]
    
        
print(add(1000))

