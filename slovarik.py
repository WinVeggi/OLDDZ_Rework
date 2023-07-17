def is_palindrome(slovo):
    return slovo == slovo[::-1]

while True:
    slovo = input('Введите слово для проверки: ')
    print(is_palindrome(slovo))
