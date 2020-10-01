def pallindrome(a):
    b = a[::-1]
    if a == b:
        print('word is a pallindrome in nature')
    else:
        print('word is a not pallindrome in nature')
word = input('enter a word : ')
pallindrome(word)