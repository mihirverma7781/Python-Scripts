class Mobile:
    def __init__(self,name):
        self.name = name

class Mobilestore:
    def __init__(self):
        self.mobiles = []
    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of mobile class')

oneplus = Mobile('oneplus 6')
samsung = 's20 ultra'
mobostore = Mobilestore()
mobostore.add_mobile(oneplus)
# print(mobostore.mobiles)
var = mobostore.mobiles

print(var[0])
