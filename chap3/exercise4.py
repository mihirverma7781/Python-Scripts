no = input('enter a number : ')
length = len(no)
sum = 0
i=0
while i<length:
    sum += int(no[i])
    i = i+1
print(sum)