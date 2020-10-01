# we use enumrate function with for loop to track position of our item in iteration




# how can we do it without enumerate function
l=['abc','def','mihir']
# pos=0
# for i in l:
    
#     print(f"{pos} --> {i}")
#     pos+=1

# with enumrate function

# for posi,name in enumerate(l):
#     print(f"{posi} --> {name}")


# practice

def fu(li,target):
    for pos,name in enumerate(li):
        if name == target:
            return pos
    return -1
print(fu(l,'abcd'))