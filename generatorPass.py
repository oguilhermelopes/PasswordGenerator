import random

#Character List
uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = uppercaseLetters.lower()
numbers = "0123456789"
symbols = "!@#$%&+="

#Characters that will be used
upper, lower, nums, syms = True, True, True, True

passw = ""

#Characters that will be used
if upper:
    passw += uppercaseLetters
if lower:
    passw += lowercaseLetters
if nums:
    passw += numbers
if syms:
    passw += symbols

#Number of characters
lenght = 20
#Number of passwords to be generated
amount = 2

#Generate password
for x in range(amount):
    password = "".join(random.sample(passw, lenght))
    print('Your password is: ' + password)
