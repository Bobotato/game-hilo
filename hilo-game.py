import sys


def print_menu():
    '''Prints the main menu'''
    print("[1] Play")
    print("[2] Ruleset")
    print("[3] Exit")


def start_game():
    pass


print("Welcome to Alex's Hi-lo game. "
      "It has been in development hell since 2020.")
while True:
    print_menu()
    option = input("Enter your option number: \n")
    if option == "1":
        start_game()
        break
    elif option == "2":
        print("\nThe game uses a standard 52 card deck. "
              "1 card is dealt face up, and another face down.\n"
              "You need to guess if the face down card is of a "
              "higher or lower value than the face up card.\n"
              "A right answer doubles your bet, and a wrong "
              "answer forfeits your bet. Happy playing.\n")
    elif option == "3":
        sys.exit("Thanks for playing!")
    else:
        print("Please try typing your choice again.\n")

