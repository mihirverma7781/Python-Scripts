# instance methods

# l = [1,2,3]
# # print(l.pop())


# how to make instance method

class Person:
    def __init__(self,f_name,l_name,age):
        self.fname = f_name
        self.lname = l_name
        self.age =  age
    
    # initializing a method
    def full_name(self):
        return f"your full name : {self.fname } {self.lname}"
    def is_above_18(self):
        if (self.age >= 18):
            return "you are eligible"
        return "you are not eligible"

p1 = Person('mihir','verma',19)
p2 = Person("mitu","verma",17)
print(p1.full_name())
print(p2.full_name())
print(p1.is_above_18())
print(p2.is_above_18())

# one more method to call a method 
print(Person.full_name(p2))


# more examples
l = [1,2,30]

# clear , pop
print(list.clear(l))
# l.clear()

l.append(10)
# or
list.append(l,10)

# takes first argument always as a self
print(l)