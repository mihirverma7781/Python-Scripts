# in keyword

s={1,2,3}
print(len(s))
if 1 in s:
    print('present')
else:
    print('false')

# loop in sets

for i in s:
    print(i)

l =[1,1,2,3,3]
se=list(set(l))
print(se)

# union

ss={2,3,4,5}
union= ss | s
print(union)

# intersection
print(s&ss)