fruit=['grapes','mango','apple']
fruit.sort()
print(fruit)

fruits=('grapes','mango','apple')
t=sorted(fruits)
print(t)



students2=[
{'name':'harshit', 'score': 44 , 'age':71},
{'name':'mohit','score': 43, 'age':44},
{'name':'mihir','score': 71, 'age':23}
]


m=sorted(students2 , key= lambda item : item.get('age'),reverse=True)
print(m)