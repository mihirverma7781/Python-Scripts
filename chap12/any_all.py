numbers1=[2,4,6,8,10]
numbers2=[1,3,5,7,9,2]
evens=[]
for i in numbers1:
    evens.append(i%2==0)
print(evens)

n=all([True, True, True, True, True])
print(n)

# lc + all

m = all([num%2==0 for num in numbers2])
print(m)

k = any([num%2==0 for num in numbers2])
print(k)