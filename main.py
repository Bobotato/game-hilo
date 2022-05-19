from game import Game
import sys
from game import Prediction


def end_game():
    """
    Ends the game and closes the program.
    """
    sys.exit("Thanks for playing!")


def get_name():
    """
    Gets an input from a user to set their name.
    """
    while True:
        name = str(input("What is your name?\n"))
        if name:
            print(f"Hello {name}.")
            return name
        else:
            print("You cannot have an empty name, try again.")


def get_bet():
    """
    Prints the player's credit balance, asks for a bet
    from the user, returns bet.

    :return: The player's bet for the round.
    :rtype: int
    """
    while True:
        try:
            print(f"You have {game.player.credits} credits.")
            bet = int(input("How much would you like to bet?\n"))
        except ValueError:
            print("Please only input integers.\n")
        else:
            if bet > game.player.credits:
                print("You cannot bet more credits than you have.\n")
            elif bet <= 0:
                print("You cannot bet 0 or negative amounts.\n")
            else:
                return bet


def is_continuing():
    """
    Gets an input from the player to choose if they want to play another
    round.

    :return: True/False based on the player's answer.
    :rtype: bool
    """
    while True:
        continuing = input("Would you like to continue?\n" "[1] Yes\n" "[2] No\n")
        if continuing == "1":
            return True
        elif continuing == "2":
            return False
        else:
            print("Please only input either 1 or 2.")


def get_prediction():
    """
    Gets an input from the player to predict if the drawn card will be
    higher or lower.
    """
    while True:
        print(f"The current card is {round_info.current_card}.")
        prediction = input(
            "Will the drawn card be higher or lower?\n" "[1] Higher\n" "[2] Lower\n"
        )
        try:
            return Prediction(int(prediction))
        except ValueError:
            print("Please only use 1 for higher or 2 for lower.")


def get_restart():
    """
    Gets an input from the user to choose if they want to restart
    the whole game with 100 credits. (Applies to gameover conditions)
    """
    while True:
        restart = input(
            "Would you like to try again with 100 credits?\n" "[1] Yes\n" "[2] No\n"
        )
        if restart == "1":
            return True
        elif restart == "2":
            return False
        else:
            print("Please only input 1 to restart or 2 to quit.")


def print_bankrupt():
    """
    Prints the bankruptcy message.
    """
    print("You've reached zero credits, you're bankrupt!")


def print_empty_deck():
    """
    Prints the empty deck message.
    """
    print("The deck has been emptied! Good job!")


def print_menu():
    """
    Prints the main menu
    """
    print("[1] Play")
    print("[2] Ruleset")
    print("[3] Exit")


def print_result():
    """
    Prints the result of the most recently played round.
    """
    if round_result.win:
        print(
            f"The next card was {round_result.drawn_card}. You won!\n"
            f"You now have {game.player.credits} credits."
        )
    else:
        print(
            f"The next card was {round_result.drawn_card}. You lost!\n"
            f"You now have {game.player.credits} credits."
        )


def start_game():
    """
    Creates an instance of a Game with the user's name.

    :param name: A string representing the user's name.

    :return: An instance of a Game
    """
    return Game(name)


print("Welcome to Alex's Hi-lo game. " "It has been in development hell since 2020.")
name = get_name()
while True:
    print_menu()
    option = input("Enter your option number: \n")
    if option == "1":
        start_game()
        break
    elif option == "2":
        print(
            "\nThe game uses a standard 52 card deck. "
            "1 card is dealt face up, and another face down.\n"
            "You need to guess if the face down card is of a "
            "higher or lower value than the face up card.\n"
            "A right answer doubles your bet, and a wrong "
            "answer forfeits your bet. Happy playing.\n"
        )
    elif option == "3":
        sys.exit("Thanks for playing!")
    else:
        print(
            "\nYour input was not recognised, please try again. "
            "Try typing 1, 2 or 3.\n"
        )

game = start_game()
round_info = game.start_round()
replay = True
while replay:
    prediction = get_prediction()
    bet = get_bet()
    round_result = game.compute_round_result(bet, prediction)
    print_result()

    if game.player.is_bankrupt():
        print_bankrupt()
        if get_restart():
            game = start_game()
            round_info = game.start_round()
            print("Your credits have been reset and the deck rebuilt!")
            continue
        else:
            end_game()

    if game.deck.is_empty():
        print_empty_deck()
        if get_restart():
            game = start_game()
            round_info = game.start_round()
            print("Your credits have been reset and the deck rebuilt!")
            continue
        else:
            end_game()

    if is_continuing():
        round_info.current_card = round_result.drawn_card
    else:
        end_game()
