from random import randint

print('welcome To state cmd!')
print(40 * '_')

id_user = randint(1, 10)

user = {}
state = {} 

start_ = False

while True:
    

    if start_ == False:

        questions = input('Order:')

        if questions == 'start':
            start_ = True

            user['id'] = id_user

            print('1-my data')
            print('2-show all values')

            options = input('Options:')

            if options == '1':
                name = input('yorname:')
                user['name'] = name

                if id_user == user['id']:
                    lastname = input('your lastname:')
                    user['lastname'] = lastname
                    
                    if id_user == user['id']:
                        age = input('your age:')
                        user['age'] = age

            
            elif options == '2':

                print('your id:', user['id'])
                print('your name:', user['name'])
                print('your lastname:', user['lastname'])
                print('your age:', user['age'])
    else:
        options = input('Options:')

        if options == '1':
            name = input('yorname:')
            user['name'] = name

            if id_user == user['id']:
                lastname = input('your lastname:')
                user['lastname'] = lastname
                
                if id_user == user['id']:
                    age = input('your age:')
                    user['age'] = age
        
        elif options == '2':

            print('your id:', user['id'])
            print('your name:', user['name'])
            print('your lastname:', user['lastname'])
            print('your age:', user['age'])