import random
import string

pass_len = 10
charvalues = string.digits 
password = ""

for i in range(pass_len):
    password += random.choice(charvalues)

print("Your random password is:", password)
