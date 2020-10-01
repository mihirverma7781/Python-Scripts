# dictionary comprehension
# square = {1:1, 2:4, 3:9}

square={f" square of {num} is ": num**2 for num in range(1,11)}

for key,value in square.items():
    print(f"  {key} {value}") 

string = "mihirverma"

count = {char:string.count(char) for char in string}
print(count)