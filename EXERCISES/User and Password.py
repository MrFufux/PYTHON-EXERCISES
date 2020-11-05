#-----------------------------------------------------PASSWORD EXERCISE--------------------------------------------------------------------------------
#Este ejercicio es solo funciona correctamente si se ingresa los valores adecuados, si no es asi no compila el codigo.


User = 'Andres'
password = 'UmbrellAndres'

print('Welcome to Umbrella Corp!')
print('Hello User. Identify with your user and password.')
print('Please type your User')

Username = input()
if User == 'Andres':
    print('Please type your Password')
else:
    print('Please type your User.')

Passname = input()

if password == 'UmbrellAndres':
    print('Welcome to Umbrella Corp Dr. Andres')
else:
    print('Access Denied. Please contact with a supervisor.')

#------------------------EJERCICIO DE USUARIO Y CONTRASENA---------------------------------------------------
print('///////////////////////////////////////////////////////////////////////////////')

print('Welcome to Umbrella Corp!')
print('Hello User. Identify with your user and password.')
print('Please type your User and Password to continue.')


while True:
    username = input('Enter your Username: ')
    password = input('Enter your Password: ')

    if password == 'UmbrellAndres' and username == 'Andres':
        print('Access granted. Welcome to Umbrella Corp Dr. Andres.')
        break
    else:
        print('Access denied. Try again. Your Username or Password are wrong!')


#------------------------EJERCICIO DE USUARIO Y CONTRASENA CON SOLO 3 OPOTUNIDADES----------------------------------------
print('///////////////////////////////////////////////////////////////////////////////')

print('Welcome to Umbrella Corp!')
print('Hello User. Identify with your Username and Password.')
print('Please type your Username and Password to continue.')

count = 0

while count < 3:
    username = input('Enter your Username: ')
    password = input('Enter your Password: ')

    if password == 'UmbrellAndres' and username == 'Andres':
        print('Acces granted. Welcome to Umbrella Corp Dr. Andres')
        break
    else:
        print('Access denied.')
        count += 1

if count == 3:
    print('Please send your case at the email: support@umbrellacorp.com')
    


    










