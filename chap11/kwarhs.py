# **(kwargs)= keyword arguments

# double star arguments
def func(mname,**kwargs):
    for k,v in kwargs.items():
        print(f"keys ={k} and values = {v}")
    # print(kwargs)
    # print(type(kwargs))
    # # dictionary unpacking

d= {'name':'harshit','age':24}
func('sunil',fname ='mihir', lname ='verma')
func('sunil',**d)