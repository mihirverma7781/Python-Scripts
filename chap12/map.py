num =[1,2,3,4]
# def square(n):
#     return n**2

sq=list(map(lambda a:a**2 ,num))
print(sq)

# with list comprhension

sqa=[i**2 for i in num]
print(sqa)

# without any of these
new=[]
for h in num:
    new.append(h**2)
print(new)