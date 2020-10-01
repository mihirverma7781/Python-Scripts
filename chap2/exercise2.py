num1,num2,num3 = input("enter number 1,2 & 3 =").split(",")
average = ((int(num1)+int(num2)+int(num3))/3)
print("average = "+ str(average))
# into string formatting
print(f"Average of three numbers : {((int(num1)+int(num2)+int(num3))/3)}")