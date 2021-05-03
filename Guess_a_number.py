import random

#a function created for guessing between a particular range of numbers starting from 1
def guess(num):
    random_number = random.randint(1, num)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {num}')) #taking input
        if guess < random_number:#checking conditions to get closer to the guessed number
            print("Your guessed number is lower than what we guessed. Try again")
        elif guess > random_number :#checking conditions to get closer to the guessed number
            print("You guessed number is higher than what we guessed. Try again")
    print(f"CONGRATS! You have guessed the correct number which is {random_number}") # guess == random_number

guess(100) #the computer will guess a number from 1 to 100




