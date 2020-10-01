import random
i=1
guess = random.randint(1,100)
while i <=100:
    num = int(input('Guess any number from 1 to 100 : '))
    if num==guess:
        print(f'you win!! you have taken {i} times to completed it')
        break
    else:
        if num <= guess:
            print('Low Input try again!!')
        if num >= guess:
            print('High Input try again!!')
        else:
            pass
    i = i+1