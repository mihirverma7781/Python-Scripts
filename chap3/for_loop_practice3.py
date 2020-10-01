name = input('enter your name : ')
i=0
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        temp = temp+ name[i] 
        print(f"number of {name[i]} in string = {name.count(name[i])}")
    else:
        pass
    i= i+1