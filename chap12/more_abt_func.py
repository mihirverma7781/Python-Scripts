# what are doc string
#this are indication to user into the program 


# how to write docstring

def addi(a,b):
    '''this take two inputs'''
    return a+b

print(addi.__doc__)
print(addi(1,2))

# how to see docstring
print(len.__doc__)
print(sorted.__doc__)
print(max.__doc__)



# what is help function
print(help(sum))
print(sum(10,0))