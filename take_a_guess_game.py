import random


print('hello there. What is your name?')
userName = input()

secretNumber = random.randint(1, 20)

print("Well " + userName + " i am thinking of a number between 1-20. Can you guess it?")

totalTries = 7
tries = 0

while tries <= totalTries:

    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good Job ' + userName + ' You guessed my number!')
else:
    print('You failed :(')