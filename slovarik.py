

def is_palindrome():
    print('Введите слово:')
    slovo = input()
    if slovo == slovo[::-1]:
        print('True')
    else:
        print('False')
is_palindrome()
