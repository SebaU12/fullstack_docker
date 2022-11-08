import random, string
from werkzeug.security import generate_password_hash

SECRET_KEY = "chocolateros"

def generate_user_account(nombre,apellido,dni):
    number_of_digits = 3
    number_of_punctuation_characters = 2
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password_length = 8 
    password = ""

    for digits_index in range(number_of_digits):
        password = password + random.choice(string.digits)

    for punctuation_index in range(number_of_punctuation_characters):
        password = password + random.choice(string.punctuation)

    for index in range(password_length - number_of_digits - number_of_punctuation_characters):
        password = password + random.choice(string.ascii_letters)

    username = apellido[0]+"_" + nombre+"_" + dni[1:4]
    hashpassw = generate_password_hash(password+SECRET_KEY)
    return username, hashpassw, password 

print(generate_user_account("Mauro", "Tonto", "20192930"))


