#Guess Game defined as a function

#import libraries
import random

x = random.randint(1, 100)  

#define function

def guessing_game(guess):
    while True:   #loops the game around again until the correct number is guessed
    if (guess < x):  
        return("Your number is too small. Guess again: ")    
    
    elif (guess > x):
        return("Your number is too big. Guess again: ")
        
    else:
        return("Congrats, you guessed the number, it was", number)
        break 
    
#the code

guess = int(input("Pick a number between 1 and 100: ")) #player picks a number between 1 and 100

for guess:
    print(guessing_game)