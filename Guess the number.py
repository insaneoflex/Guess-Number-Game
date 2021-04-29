# This is a guess the number game
import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')

secretnumber = random.randint(1, 20)

for guessestaken in range (1, 7):
    print ('Take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print ('Your guess is too low.')
    elif guess > secretnumber:
        print ('Your guess is too high.')
    else:
        break #This condition is for the correct guess

if guess == secretnumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessestaken) + ' tries ')
else:
    print('Nope, the number I was thinking of was ' +str(secretnumber))
          

