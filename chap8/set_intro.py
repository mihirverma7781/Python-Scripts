# .unordered collection of unique items
# we cant store list tuple and dictionary

s={1,2,3,4,5,6,5}
print(s)

# remove dupliate
l= [1,1,2,3,3,4,4,5,6,4,3,4,6,4,4,5,4,4,3,2,4]
print(l)
se = list(set(l))
print(se)

# methods of sets
# adding elements
sw= {1,2}
sw.add(5)
# print(sw)
# sw.remove(2)
# print(sw)
# sw.discard(3)
print(sw)
# sw.clear()
s1 =sw.copy()
print(s1)