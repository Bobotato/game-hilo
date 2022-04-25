def open_main_menu():
'''Opens the main menu and its choices'''
    while True:
        main_menu_choice = (input("Please type an option or it's shorthand (first letter) to choose:\nPlay\nRules\nQuit\n")).lower()
        if main_menu_choice == "rules" or main_menu_choice == "r":
            print("The game is played with a standard 52 card deck. The dealer plays one card face up and one card face down. You have to guess whether the facedown card is of higher or lower value than the faceup card. Getting it right doubles your bet, losing forfeits the bet.\n")
            open_main_menu()
        elif main_menu_choice == "quit" or main_menu_choice == "q":
            print("Thanks for playing!")
            quit()
        elif main_menu_choice == "play" or main_menu_choice == "p":
            print("Let's begin!")
            game_initialise()
            break
        else:
            print("Try again, remember its \"play/p\" to play, \"rules/r\" for the rules, or \"quit/q\".\n\n")

def game_initialise():
'''Starts the game process'''
    print("Game is starting...TBC")

print("Welcome to Alex's Hi-lo game. It has been in development hell since 2020.")
open_main_menu()
