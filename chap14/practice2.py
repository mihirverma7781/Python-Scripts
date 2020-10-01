def func(*args):
    l=[]
    for pair in zip(*args):
        l.append((sum(pair)/len(pair)))
    print(l)



func([1,2,3],[4,5,6],[7,8,9])


# average = [sum(pair)/len(pair) for pair in zip(*arg) ]

# print(average)

# number1 = [2,4,6,8,10]
# l = [i%2==0 for i in number1] 
# print(l)
