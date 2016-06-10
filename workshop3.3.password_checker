import string, random

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = string.punctuation
MENU = """
Please enter a valid password
Your password must be between 5 and 15 characters, and contain:
1 or more uppercase characters
1 or more lowercase characters
1 or more numbers
and 1 or more special characters:	!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|
"""
def check_password(pw, validator):
    for each in pw:
        if each in validator:
            return True
    return False

print(MENU)
password = input(">>>")

while True:
    if len(password) < 5 or len(password) > 15:
        print("Legth issue")
        password = input(">>>")
    elif not check_password(password,UPPER):
        print("Uppercase issue")
        password = input(">>>")
    elif not check_password(password,LOWER):
        print("Lowercase issue")
        password = input(">>>")
    elif not check_password(password,DIGITS):
        print("Digits issue")
        password = input(">>>")
    elif not check_password(password,SPECIAL):
        print("Special character issue")
        password = input(">>>")
    else:
        break

print("Password accepted.")
