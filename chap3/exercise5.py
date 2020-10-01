name = input('enter your full name : ')
i= 0
temp =""
while i< len(name):
    if name[i] not in temp:
        temp = temp+name[i]
        print(f"number of letter : {name[i]} = {name.count(name[i])}")
    i= i+1