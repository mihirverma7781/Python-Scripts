# looping tuples
mixed = (1,2,3,4)
for i in mixed:
    print(i)

# tuple with 1 parameter
nums =(1,)
words =('words',)

# tuple without parenthisis

bike = 'yamaha','tvs','bajaj'
print(bike)

# tuple unpacking
 
bike1,bike2,bike3 = (bike)
print(bike1)

# list inside tuple
fav = (1,2,['mihir','verma'])
fav[2].pop()
print(fav)
fav[2].append("yo")
print(fav)

# functions
# min, max, sum