import random

print("Welcome to Tic tac toe.")

def game():
    userInput = int(input("Press 1 for Rock, 2 for Paper, 3 for Scissors: "))
    if userInput > 3:
        greatError = "greatError"
        return greatError

    computerInput = random.randint(1,3)

    if userInput == 1:
        if computerInput == 2:
            print("You lose.")
        if computerInput == 3:
            print("You win.")
    
    if userInput == 2:
        if computerInput == 1:
            print("You win.")
        if computerInput == 3:
            print("You lose.")

    if userInput == 3:
        if computerInput == 1:
            print("You win.")
        if computerInput == 2:
            print("You lose.")

    if userInput == computerInput:
        print("Tie")
        
while True:
    while True:
        isError = game()   
        if isError == "greaError":
            game()
        else:
            break
    
    playAgain = input("Do you want to play again. (y/n): ")
    if playAgain == "y":
        game()
    if playAgain == "n":
        print("Thank you for playing our game.")
        break
