import string
import random
#we can randomly genrate a password everytime 
#code
def password():
    len = random.randint(8, 33)
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for i in range(len))
    return password

print(password())