nums =[1,2,3,4,5,6,7,8,9,10]
no =[i*2 if (i%2 ==0) else -i for i in nums]
print(no)
new_list =[]
for i in nums:
    if i%2 != 0:
        new_list.append(-i)
    else:
        new_list.append(i*2)
print(new_list)



