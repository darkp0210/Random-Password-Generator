import string
import random

length = int(input("Enter desired password length: "))

character_list = list(string.printable)

password = []

for i in range(length):
    # Picking a random character from character list
    random_char = random.choice(character_list)

    # appending a random character to password
    password.append(random_char)

# printing password as a string
print("".join(password))

