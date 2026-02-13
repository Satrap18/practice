from pyfiglet import Figlet
from getpass import getpass
from database import DataBase

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

main = DataBase()
main.create_table()

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

            if password == password_confirm:
                if main.cheak_user(username) == username:
                    print('This username already exists, please use another username.')
                else:
                    main.create_user(fullname=fullname, username=username, password=password)
            else:
                print('Password and password confirmation are not the same.')
        case '2':
            print('Username:')
            username = input('|')
            print('Password:')
            password = getpass('|')

            data = main.login_user(username=username, password=password)

            if data == username:
                login_ = True
                username_ = username
        case '3':
            if login_ == False:
                print('Please login first')
            elif login_ == True:
                wallet = main.wallet_user(username_)
                print(f"The wallet that needs to be paid is yours and is exclusive to you:\n{wallet}")
        case '4':
            if login_ == False:
                print('Please login first')
            elif login_ == True:
                print('1-"1 trx" 30D ')
                print('1-"2 trx" 60D ')
                print('1-"3 trx" 90D ')
                sub = input('Select Subscription:')
                match sub:
                    case '1':
                        print('active 30D')
                    case '2':
                        print('active 60D')                    
                    case '3':
                        print('active 90D')                        
        case '5':
            exit()
        case _:
            print("Please select by number or select from the given numbers")