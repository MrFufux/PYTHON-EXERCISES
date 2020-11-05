#Guess the number Program.
print('///////////////////////EJERCICIO 1 /////////////////////////////////////////////////////')

import random   #Como necesitamos un numero random importamos este modulo

print('Hello. What is your name?')
name = input()

print('Well, '+ name +', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)      #Esta funcion retorna integers
#el + name + es porque name regresa str por lo que se puede concatenar.

for guessesTaken in range (1, 7):
    print('Take a guess.')
    #Input retorna un string pero necesito un integer
    guess = int(input())  #Para que me de un integer de pasar por la funcion int
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break      #Esta condicion es para el guess correcto!
                   #Aqui termina el loop de manera prematura cuando adivina el numero.

if guess == secretNumber:
    print('Good Job, ' + name + '! You guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

#Se llama la funcion str al secretNumber
#hay que hacer concatenacion de strings porque secretNumber devuelve un int


print('///////////////////////////////////EJERCICIO 2/////////////////////////////////////////////////////////////')
#Ejercicio 2:

from random import randint

print('Hello Stranger. I would like to know your name')
name = input()

print('Oh! Hi, ' + name +'. You know, I am thinking right know. I need a number bettween 1 to 30.' )
numbersecret = random.randint(1, 30)

for turnos in range (1, 5):
    print('Please take a guess.')
    eleccion = int(input())

    if eleccion > numbersecret:
        print('Your guess is high')
    elif eleccion < numbersecret:
        print('Your guess is low')
    else:
        break

if eleccion == numbersecret:
    print('Congratulations ' + name +'. You guessed the number that I was thinking.')
    print('You take ' + str(turnos)+ ' guesses to know it.')
else:
    print('Sorry bro. The number I was thinking of was ' + str(numbersecret) + '!')




    








