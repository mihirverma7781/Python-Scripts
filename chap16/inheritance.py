class Phone:
    def __init__(self,brand , model  , price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
    
    def make_a_call(self,phone_number):
        print(f" calling {phone_number}....")

    def full_name(self):
        return f"{self.brand} {self.model} {self._price }"



class Smartphone(Phone):
    def __init__(self,brand,model,price,ram, internal_storage  , camara):
        # Phone.__init__(self, brand, model, price)    
        super().__init__(brand, model, price)
        self.ram = ram
        self. internal_storage = internal_storage
        self. camara = camara

        # instantiating the parent class
        # two ways
        # 1
    

p1 = Phone('nokia',1100,1000)

print(f"{p1.full_name()} {p1.make_a_call(346465)}")

p2 = Smartphone('samsung','s20 ultra',72000, 12,512,108)

print(p2.full_name())
print(p2.ram)
print(p2.internal_storage)
print(p2.camara)