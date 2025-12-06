import string
import random
print("Welcome to password generator")
length_intial=(input("Enter the required length of your password "))
if not length_intial.isdigit():
    print("Please enter a valid number!")
    exit()
length=int(length_intial)
if length<=0:
    print("length must be greater than zero")
    exit()
print("your length:",length)
characters=string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(length):
    password=password+random.choice(characters)
print("The generated password is:",password)