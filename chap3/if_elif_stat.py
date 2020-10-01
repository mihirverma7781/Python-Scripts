#we use it when we have to check multiple conditions
# show ticket pricing
#  1 to 3 (free)
#  4 to 10  (150)
#  11 to 60 (250)
#  above 60 (200)

age = input('please input your age = ')
age = int(age)
if age<=0:
    print("invalid age")
elif 0<age<=3:
    print('ticket price : free')
elif 3<age<=10 :
        print('ticket price : 150')
elif 10<age<=60:
            print('ticket price : 250')
else:
    print('ticket price : 150')