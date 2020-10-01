class Person:
    count_instance = 0
    def __init__(self, f_name,l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        Person.count_instance+=1
    
# class method declaration
    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__}"


    def name(self):
            return f" your name = {self.f_name} {self.l_name}"

    def above(self):
            return self.age>=18

p1 = Person('mihir','verma',19)
p2 = Person('mohit','verma',17)

print(p2.name())
print(p2.above())
print(Person.count_instances())