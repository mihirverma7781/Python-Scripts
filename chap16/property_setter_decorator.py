

class Phone:
    def __init__(self,brand , model  , price):
        self.brand = brand
        self.model = model
        self._price = price
        
        
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0


       
        # self.complete_info = f"{self.brand} {self.model} {self._price}"
    
    # this is used as property decorator
    
    @property
    def complete_info(self):
        return f"{self.brand} {self.model} {self._price}"



    # getter and setter methods to set the values if we put the negative values

    # getter declaration
    @property
    def price(self):n  
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    
    def make_a_call(self,phone_number):
        print(f" calling {phone_number}....")

    def full_name(self):
        return f"{self.brand} {self.model}"

phone1 = Phone('nokia','1100',1000)

phone1.price = -100
print(phone1._price)
print(phone1.complete_info)