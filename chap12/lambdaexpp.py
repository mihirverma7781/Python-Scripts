# # def is_even(a):
# #     return a%2==0

# # print(is_even(5))


# # eve = lambda a : a%2==0

# # print(eve(4))

# def last_char(s):
#     return s[-1]

# l = lambda m : m[-1]
# print(l('mihir'))

# lambda with if else
def func(s):
    if len(s)>5:
        return True
    return False

fun = lambda s : len(s)>5 #True if len(s)>5 else False
print(fun('mihis'))