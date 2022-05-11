#Random Number Guessing Game

import random

x = random.randint(1, 100)   #Assign random integer to x
#print(x)  #take away "#" and it will reveal what the random number is before guess

guess = int(input("Pick a number between 1 and 100: ")) #player picks a number between 1 and 100

while True:   #loops the game around again until the correct number is guessed
    if (guess < x):  
        print("Your number is too small.")    
        guess = int(input("Guess again: "))    
    
    elif (guess > x):
        print("Your number is too big.")
        guess = int(input("Guess again: "))
    else:
        print(" Congrats, you guessed the number, it was", guess)
        break 

