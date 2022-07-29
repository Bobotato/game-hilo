import sys

from database.loginpage import DatabaseConnection as DBC
from hilo.game import Game, Prediction
from hilo.models.roundinfo import RoundInfo
from hilo.models.roundresult import RoundResult


def end_game():
    sys.exit("Thanks for playing!")


def get_bet(game: Game) -> int:
    while True:
        print(
            f"\nYou have {game.player.credits} credits.\n"
            "How much would you like to bet?\n"
        )

        try:
            bet = int(input("> "))
        except ValueError:
            print("Please only input whole numbers.\n")
            continue

        if bet > game.player.credits:
            print("You cannot bet more credits than you have.\n")

        elif bet <= 0:
            print("You cannot bet 0 or negative amounts.\n")

        else:
            return bet


def get_name() -> str:
    while True:
        print("Please type in your username:")
        name = str(input("> "))

        if name:
            print(f"Hello {name}.\n")
            return name

        print("No entry was detected, please try again.\n")


def get_password() -> str:
    while True:
        print("Please type in your password:")
        password = str(input("> "))

        if password:
            print("Logging you in...\n")
            return password

        print("No entry was detected, please try again.\n")


def get_new_account_password() -> str:
    while True:
        print("Please type in a strong password for the account:")
        password = str(input("> "))

        if password:
            return password

        print("Your password cannot be blank!\n")


def get_prediction(round_info: RoundInfo) -> Prediction:
    while True:
        print(
            f"\nThe current card is {round_info.current_card}.\n"
            "Will the drawn card be higher or lower?\n"
            "[1] Higher\n"
            "[2] Lower\n"
        )
        prediction = input("> ")

        try:
            return Prediction(int(prediction))
        except ValueError:
            print("Please only use 1 for higher or 2 for lower.")


def is_continuing() -> bool:
    while True:
        print("Would you like to continue?\n[1] Yes\n[2] No\n")
        continuing = input("> ")

        if continuing == "1":
            return True

        elif continuing == "2":
            return False

        else:
            print("Please only input either 1 or 2.")


def is_creating_account(username) -> bool:
    while True:
        print(
            f"Would you like to make an account with username: {username}?\n"
            "[1] Yes\n"
            "[2] No\n"
        )
        creating = input("> ")

        if creating == "1":
            return True

        elif creating == "2":
            return False

        else:
            print(
                "Please only input either 1 to create an account or 2 to exit."
            )


def is_game_over(round_result: RoundResult) -> bool:
    return round_result.is_player_bankrupt or round_result.is_deck_empty


def is_playing() -> bool:
    while True:
        print("[1] Play\n[2] Ruleset\n[3] Exit\n")
        print("Enter your option number:")
        option = input("> ")

        if option == "1":
            return True

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
            return False

        else:
            print(
                "\nYour input was not recognised, please try again. "
                "Try typing 1, 2 or 3.\n"
            )


def is_restarting() -> bool:
    while True:
        print(
            "Would you like to try again with 100 credits?\n"
            "[1] Yes\n"
            "[2] No\n"
        )
        restart = input("> ")

        if restart == "1":
            print("Credits will reset to 100, and the deck will be populated.")
            return True

        elif restart == "2":
            return False

        else:
            print("Please only input 1 to restart or 2 to quit.")


def is_retrying_password() -> bool:
    while True:
        print("Would you like to try again or quit?\n[1] Yes\n[2] Quit")
        retrying = input("> ")

        if retrying == "1":
            return True

        elif retrying == "2":
            return False

        else:
            print("Please only input 1 to try again, or 2 to quit.")


def print_bankrupt():
    print("You've reached zero credits, you're bankrupt!")


def print_empty_deck():
    print("The deck has been emptied!")


def print_result(round_result: RoundResult):
    if round_result.win:
        print(
            f"\nThe next card was {round_result.drawn_card}. You won!\n"
            f"You now have {game.player.credits} credits."
        )
    else:
        print(
            f"\nThe next card was {round_result.drawn_card}. You lost!\n"
            f"You now have {game.player.credits} credits."
        )

    if round_result.is_player_bankrupt:
        print_bankrupt()

    elif round_result.is_deck_empty:
        print_empty_deck()


def print_wrong_password():
    print("Your password is incorrect.")


if __name__ == "__main__":
    print(
        "\nWelcome to Alex's Hi-lo game.\n"
        "It has been in development hell since 2020.\n"
    )

    name = get_name()

    conn = DBC()

    if not conn.is_returning_player(name):
        if not is_creating_account(name):
            end_game()

        conn.add_new_player(name, get_new_account_password())

    while not conn.is_password_correct(name, get_password()):
        print_wrong_password()

        if not is_retrying_password():
            end_game()

    if not is_playing():
        end_game()

    game = Game(name)

    while True:
        round_info = game.start_round()

        round_result = game.compute_round_result(
            prediction=get_prediction(round_info), bet=get_bet(game)
        )

        print_result(round_result)

        if is_game_over(round_result):
            if not is_restarting():
                break
            game = Game(name)

        elif not is_continuing():
            break

    end_game()
