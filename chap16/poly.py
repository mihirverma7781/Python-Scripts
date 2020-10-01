# dunder methods or double underscore methods
# operator overloading
# polymorphism


class Phone:
    def __init__(self,brand , model  , price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
    
    def make_a_call(self,phone_number):
        print(f" calling {phone_number}....")

    def full_name(self):
        return f"{self.brand} {self.model} {self._price }"


    # str, repr dunder  methods
    def __repr__(self):
        return f"{self.brand}{self._price }"
    def __str__(self):
        return f"{self.brand}{self._price } {self._price}"

    def __len__(self):
        return len(self.full_name())
    def __add__(self,other):
        return self._price + other._price

# 2+3 =5
# mihir+verma =mihir verma


myphone = Phone('samsung','s20 ultra',72000)
myphone2 = Phone('samsung','note',2000)
print(myphone+myphone2)

print(len(myphone))