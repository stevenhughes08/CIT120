# This is only for an exercuise this is not intended for production or validation.
#

import sys

password = input("Please enter a super secret password: ")
attempt_count = 1
while password != 'mysecretpassword':
    if attempt_count > 3:
        sys.exit(" Too many invalid password attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to secret town")
