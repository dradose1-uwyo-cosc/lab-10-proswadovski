# Peyton Roswadovski
# UWYO COSC 1010
# Submission Date: 11/24/24
# Lab 10
# Lab Section: 14
# Sources, people worked with, help given to: Lab TAs
#import modules you will need 

#To read a file eg. text.txt
#1. Get teh file path
#2. Create your try except block
#3. In the try block, call read_text(). And that'll give you the content of the file 

# 4. split the rockyou.txt into lines and loop by line 
# 5. For every line, hash it and check against the hash content

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

other_passwords = Path('rockyou.text')
correct_password = Path('hash')

try:
    hash = correct_password.read_text()
except:
    print(f"Can't read hash file")
    exit()
try:
    with open(other_passwords, 'r', encoding='utf-8') as f:
        passwords = f.readlines()

except:
    print(f"Can't read rockyou.txt file")
    exit()

for line in passwords:

    password = line.strip()
    other_passwords = get_hash(password)

    if other_passwords == hash:
        print(f"Password found: {password}")
        break  
else:
    print("Incorrect password")

    

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."
# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.