from pyfiglet import Figlet
from getpass import getpass
import sqlite3

f = Figlet(font='slant')
print(f.renderText('Wallet'))

print('''
1-create account
2-login
3-my wallet
4-send balance
5-exit
''')

login_ = False
username_ = ''

while True:

    option = input('Choose from the options: ')

    match option:
        case '1':
            print('fullname:')
            fullname = input('|')
            print('Username:')
            username = input('|')
            print('Password:')
            password = getpass('|')
            print('Confirm Password:')
            password_confirm = getpass('|')
        case '2':
            print('Username:')
            username = input('|')
            print('Password:')
            password = getpass('|')
        case '3':
            if login_ == False:
                print('Please login first')
        case '4':
            if login_ == False:
                print('Please login first')
        case '5':
            exit()
        case _:
            print("Please select by number or select from the given numbers")