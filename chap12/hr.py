# ans=[[x,y,z] for x in range(0,3) for y in range(0,2) for z in range(0,2) if (x+y+z!=n) ]
# print(ans)
l=[]    
for i in range(5):
    l.append([])
print(l)

for j in l:
    name = input('enter name')
    score = float(input('enter score'))
    j.append(name)
    j.append(score)
m=max(l)
print(m)
# m=max(l)
# l.remove(max(l))
# while m in l:
#     l.remove(max(l))
# k=max(l)
# while k in l:
#     g=max(l)
#     print(g[0])
#     l.remove(max(l))
#     s=l.copy()
#     print
res=[[x for x,y in m],[y for x,y in m]]
print(res)



# l=[[] for i in range n]

            
            
            
            


            
        

