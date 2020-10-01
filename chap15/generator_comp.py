#we use this in list comprehension 

square=[i**2 for i in range(1,11)]
print(square)

# for generator comprehension we have to use paranthesis only()

squ=(i**2 for i in range(1,11))
for num in squ:
    print(num)