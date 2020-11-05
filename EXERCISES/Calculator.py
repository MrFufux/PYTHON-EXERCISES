#-----------------CALCULATOR WITH PYTHON--------------------------------------------------------

print('This is a calculator. Please follow the instructions')

num1 = float(input('Enter the first number: '))
operator = input('Please, choose the operator that you wanna use: ')
num2 = float(input('Enter the second number: '))

if operator  == '+':
    print('The result is :' + str(num1 + num2))

elif operator == '-':
    print('The result is: ' + str(num1 - num2))

elif operator  == '*':
    print ('The result is: ' + str(num1 * num2))

elif operator == '/':
    print('The result is: ' + str(num1 / num2))

else:
    print('invalid operation')






