slovo = input()

def is_palindrome():
    global slovo
    if slovo == slovo[::-1]:
        return True
    else:
        return False
print(is_palindrome())