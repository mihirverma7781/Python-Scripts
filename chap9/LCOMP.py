# list comprehension
# with the help of lc we can createof list in one line
# create a list of squares from 1 to 10

# simple tech

sq=[]
for i in range(1,11):
    sq.append(i**2)
print(sq)

# squ 2
squ =[i**2 for i in range(1,11)]
print(squ)

# normal
lis=[]
for i in range(1,11):
    lis.append(-i)
print(lis)

li =[-i for i in range(1,11)]
print(li)

name=['mihir','sunil','verma']
nl=[]
for i in name:
    nl.append(i[0])
print(nl)

nlc=[i[0] for i in name]
print(nlc)