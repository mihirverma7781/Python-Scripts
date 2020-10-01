winning_number = 27
gussed_number = int(input('Guess the number b/w 1 to 100 : '))
if winning_number == gussed_number:
    print("congrats you win!!!")
else:
    if gussed_number < winning_number:
        print('too small')
if gussed_number > winning_number:
    print('too high')
   
