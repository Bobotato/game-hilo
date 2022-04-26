import sys
from random import shuffle


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

values = ['A', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    """Deck consisting of playing cards, starts with 52 playing cards"""
    def __init__(self):
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def restore(self):
        self.cards = [Card(value, suit) for suit in suits for value in values]
        return self.cards

    def deal(self, face):
        if self.count() == 0:
            raise ValueError("The deck's empty, no cards can "
                             "be dealt until restored.")
        else:
            if face == "up":
                faceup_card = self.cards.pop()
                print(f"The face-up card is {faceup_card}")
                return faceup_card
            elif face == "down":
                facedown_card = self.cards.pop()
                print("The face-down card has been dealt.")
                return facedown_card

    def shuffle(self):
        shuffle(self.cards)
        return self.cards


class Card:
    """Standard Playing Card Class"""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return (f"{self.value} of {self.suit}")


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
        print("\nYour input was not recognised, please try again. "
              "Try typing 1, 2 or 3.\n")
