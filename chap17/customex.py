

class nameTooShortError(ValueError):
    pass
def validate(name):
    if len(name)<7:
        raise nameTooShortError('name too short')


username = input('enter name --> ')
validate(username)
print(f"hello {username}")