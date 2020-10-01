class Circle:
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
        
    def cir(self):
        return self.radius*Circle.pi*2

c1 = Circle(4)
c2 = Circle(5)
print(c1.cir())


# example 2

