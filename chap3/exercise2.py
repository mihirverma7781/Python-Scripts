user_name,age = input('enter your name and age : ').split()
age = int(age)
if user_name[0] =='a' or user_name[0] == 'A' and age >= 10:
    print('you are eligible to watch coco movie')
else:
    print('you are under aged')  