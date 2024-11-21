#генерація паролюююю
from random import randint

def generate_password():
    password= 'qwerttyuui'
    for i in range(8):
        password += str(randint(8, 9))
    return password






