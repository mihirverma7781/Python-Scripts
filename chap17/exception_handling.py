# exception handling
# try catch finally
while True:
    try:
        age = int(input('input your age:  '))
        
    except ValueError:
        print('invalid input')
    except:
        print('unexpected eooro...')
    else:
        print(f"user input = {age}")
        break
    finally:
        print('finally block......')


if age<18:
    print('you can\'t play this game.')
else:
    print('you can play this game ')

# errors that occur during execution