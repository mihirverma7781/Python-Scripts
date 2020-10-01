class Laptop:
    def __init__(self,price,model,company):
        self.price = price
        self.model = model
        self.company = company
        
    def apply_Discount(self,per):
        self.per = per
        return self.price-self.price*self.per/100

c1 = Laptop(69000,'cromebook360','HP')
print(c1.apply_Discount(10))


        