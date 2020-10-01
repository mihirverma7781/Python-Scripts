# adv min max func

num = [1,2,3,5,6,7]
print(max(num))

# def func(item):
#     return len(item)

names = ['mit','mohit','howard','lauv']
print(max(names, key =  lambda item : len(item) ))



students={
'harshit':{'score': 74 , 'age':24},
'mohit' : {'score': 44 , 'age':21},
'mihir' : {'score': 94 , 'age':22},
}



students2=[
{'name':'harshit', 'score': 44 , 'age':21},
{'name':'mohit','score': 43, 'age':22},
{'name':'mihir','score': 71, 'age':23}
]

print(max(students2,key= lambda item : item.get('score'))['name'])

print(max(students,key = lambda item : students[item]['score']))
