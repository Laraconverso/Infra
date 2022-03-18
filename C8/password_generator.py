import random

print(' Welcome to yout Password Generator! ')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-{}|":><?.,'

number = int(input('Amoutn of passwords to generate:  '))
length = int(input('Length of the passwords: '))

print('\nhere are your passwords: ')

for psw in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)