# encapsulation
# abstraction
# some special naming convenctions
# name mangling , __name(not a convension)

class Phone:
    def __init__(self,brand , model  , price):
        self.brand = brand
        self.model = model
        self._price = price
    
    def make_a_call(self,phone_number):
        print(f" calling {phone_number}....")

    def full_name(self):
        return f"{self.brand} {self.model}"

# convension
# all things are public
# _xxxx  --> convension to tell private property
# __xx__ --> dunder or double underscore methods or magic methods



m1 = Phone('samsung','s20 ultra',72000)
print(m1._price)
m1._price = 1000
print(m1._price)