# methods to add data in lists

fruits = ['mango','apple']
print(fruits)
fruits.insert(0,'grapes')
print(fruits)

fruits2 = ['papaya','melon'] #concating list
fruit = fruits+fruits2
print(fruit)

fruits3 = ['orange','litchi']

fruit.extend(fruits3)
print(fruit)

#list inside list
fruit.append(fruits3)
print(fruit)

