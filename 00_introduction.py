passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
# print('Enter your password: ', end='')
# typedPassword = input()
typedPassword = input('Enter your password: ')
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('The password is one that and idiot puts on their luggage.')
else:
    print('Access denied')
