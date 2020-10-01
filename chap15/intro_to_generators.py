# generators
# generators are iterators
# creating generator
# how to create generator
# 1) generator function
def func(f):
    for i in range(1,f+1):
        # print(i)
        yield(i)#creates generator

print(func(10))

# for nums in func(10):
#     print(nums)
number = func(10)
for n in number:
    print(n)
# 2) generator comprehension


