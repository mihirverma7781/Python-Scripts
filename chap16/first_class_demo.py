# class keyword id used to define a class in python

class Person:
    # here init method is constructor
    def __init__(self,f_name,l_name,age):
        print('init method called')
        # instance variable initializeation
        self.f_name = f_name
        self.l_name = l_name
        self.age =age

# object creation

p1 = Person('mihir','verma',18)
p2 = Person('rama','sri',23)
print(p1.f_name) 
print(p2.f_name)

# practice

class laptop:
    def __init__(self,model,price,color):
        print('init method called')
        self.model= model
        self.price = price
        self.color = color

p1 = laptop('r7',12000,'black')
print(p1.model)