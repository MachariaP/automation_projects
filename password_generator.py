#!/usr/bin/env python3

# Import necessary libraries
import random
import string

# Prompt the user to input the desired password length
password_len = int(input("Write password length: "))

# Initialize an empty string to store the generated password
my_password = ""

# Loop to generate the password of the specified length
for i in range(password_len):
    my_password += random.choice(string.printable)

# Print the generated password
print("Your new password: ", my_password)
