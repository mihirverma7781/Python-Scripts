class a:


    def class_a_method(self):
        return 'i am class a mthod'

    
    def hello(self):
        return 'hello from a'

class b:


    def class_b_method(self):
        return 'i am class b mthod'

    
    def hello(self):
        return 'hello from b'


class c(b,a):
    pass


instance_c = c()

print(instance_c.class_a_method())

print(instance_c.class_b_method())

print(instance_c.hello())

print(help(c))