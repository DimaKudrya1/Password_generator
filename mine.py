#генерація паролюююю
from random import randint, choice

def generate_password(length_pass=8):
    password= ''
    lower_chars = ['a','s' ,'d','f','g','h','j','k','l','z',
                   'q','w','e',r't','y','u','i','o','p',]
    upper_chars = ['Q','W','E','R','T','Y','U','I','O','P',
                   'A', 'S','D', 'F','G','H','J','K','L','Z']
    special_symbols = ['!', '@', '$','#','%',"&",'*']
    d = [lower_chars, upper_chars, special_symbols, False]
    for i in range(length_pass):
        chose = choice(d)
        if chose:
            password += choice(chose)
        else:
            password += str(randint(0, 9))
    return password

#print(generate_password(16))






