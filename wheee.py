import random


def get_difficulty():
    diff = input("Enter Difficulty Level(E,M or H):").upper()
    if diff == "E":
        return 5,25

    elif diff == "M":
        return 7,50

    elif diff == "H":
        return 10,100

    else:
        print("Enter valid input!!")
        get_difficulty()


def new_game():
    attempts,rangee = get_difficulty()
    player_choice = player_choice()
    computer_choice = comp_choice()
    
    if computer_choice == player_choice:
        print("Hurray! You Won!")

    else:
        print("You Lost!!")


def play_again():
    jawab = input("Do you want to play again?(y/n)").lower()
    if jawab == "y":
        return True
    elif jawab == "n":
        return False
    else:
        print("Enter valid input!")
        play_again()

def comp_choice():
    comp = random.randint(rangee)
    return comp

def player_choice():
    print(f"Guess a number between 1 and {rangee}.")
    print(f"Guesses left:{attempts}.")


new_game()

while play_again():
    new_game()