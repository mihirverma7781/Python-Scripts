def is_even(num):
    return num%2==0

numbers = [1,2,6,4,9,7,5,4,8,9]
even = []

even = list(filter(lambda a : a%2==0 ,numbers))
print(even)

# with lc
new_even = [i for i in numbers if i%2==0]
print(new_even)