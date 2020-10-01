# list comp. with if

num = list(range(1,11))
nums=[]
for i in num:
    if i%2== 0:
        nums.append(i)
    else:
        pass
print(nums)

even_num=[i for i in num if i%2==0]
print(even_num)