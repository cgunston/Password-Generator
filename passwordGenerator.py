# passwordGenerator.py

import random

def main():
    print("Welcome to Callum's Password Generator v1.0 \n")
    while True:
        length = eval(input("Enter how long you would like your password to be > "))
        if length < 8:
            print("A secure password should have a length greater than 8 please try again!")
        else:
            break
    generator(length)

    
def generator(y):
    x = True
    i=0
    charType = []
    password = []
    for i in range(0, y):
        charType.append("a")
        password.append("a")
    
    while x == True:
        for i in range(0,y):
            charType[i] = random.randrange(1,5)
        for i in range(0,y):
            if charType[i] == 1:
                randomLower = random.randrange(97,124)
                password[i] = chr(randomLower)
            elif charType[i] == 2:
                randomUpper = random.randrange(65,91)
                password[i] = chr(randomUpper)
            elif charType[i] == 3:
                randomNum = random.randrange(48,58)
                password[i] = chr(randomNum)
            elif charType[i] == 4:
                randomSpecial = random.randrange(33,48)
                password[i] = chr(randomSpecial)

        (x, y) = validator(password, y)


def validator(password, y):
    lower = 0
    upper = 0
    num = 0
    special = 0
    
    for i in range(0,y):
        if ord(password[i]) >= 97 and ord(password[i]) <= 122:
            lower += 1
        elif ord(password[i]) >= 65 and ord(password[i]) <= 90:
            upper += 1
        elif ord(password[i]) >= 48 and ord(password[i]) <= 57:
            num += 1
        elif ord(password[i]) >= 33 and ord(password[i]) <= 47:
            special += 1
            
    if lower > 0 and upper > 0 and num > 0 and special > 0:
        print("Your password has been successfully generated and validated!")
        print("Password > " + ''.join(password))
        return (False, y)

    else:
        return (True, y)
             
main()
