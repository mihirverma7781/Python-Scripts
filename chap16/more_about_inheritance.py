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

    def full_name(self):
        return f"{self.brand}  {self.ram}  {self.camara}  {self._price}  {self.model}"

class flagship(Smartphone):
    def __init__(self,brand,model,price,ram, internal_storage  , camara,processor):
        # Phone.__init__(self, brand, model, price)    
        super().__init__(brand, model, price,ram, internal_storage ,camara)
        self.processor = processor
        
    def full_name(self):
        return f"{self.brand}  {self.ram}  {self.camara}  {self._price}  {self.model}  {self.processor}"

      
       
    




p1= Smartphone('samsung','a51',20000, 6,128,48)
p2 = flagship('samsung','s20 ultra',72000, 12,512,108,'snampdragon 865')

print(p2.full_name())
print(p2.ram)
# print(p2.internal_storage)
# print(p2.camara)
# print(help(flagship))


# is_instance()  if we want to confirm the object belong to which class

print(isinstance(p1,flagship))

print(isinstance(p2,Phone))

print(issubclass(Smartphone,Phone))

print(issubclass(Smartphone,flagship))