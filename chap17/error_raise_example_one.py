# raise example 1
# not implemented error
# abstracted error

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to define method in subclass')
        

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return ' bhow'

class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'meow'

doggy = Dog('maggi','doberman')
print(doggy.sound())
