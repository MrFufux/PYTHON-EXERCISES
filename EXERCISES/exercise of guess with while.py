#Este ejercicio tiene el while, try

import random

print('Hello stranger. What is your name?')
name = input()
print('Nice to meet you '+ name + '. Lets play a fun game.')
print('This game is guess the number that Im thinking in a range of 1 to 20.')
thenumber = random.randint (1, 20)
guess = ''
answer = True

while answer:
    try:
        for guessestaken in range (1,5):
            print('Take a guess')
            guess = int(input())
            

            if guess < thenumber:
                print ('Nope. It is incorrect. This number is too low.')
            elif guess > thenumber:
                print('Nope. This number is not correct. The number is too high.')
            else: 
                answer = False
                break
            if guessestaken == 4:
                answer = False
                print('You are a fool.')
    except:
        print('Please type a number you dumbass bitch')


if guess == thenumber:
    print('The number is correct ' + name + '. You guessed my number in ' + str(guessestaken) + ' guesses.' )  
else:
    print('The number I was looking for was ' + str(thenumber) +'. You should try again this game.')
        













