from player import Player
from deck import Deck
from random import shuffle


class Game:
    """This class includes all the methods required for the game of Hilo"""
    def draw(self, deck, face):
        if face == "up":
            faceup = deck.cards.pop()
            print(faceup)
            return faceup
        elif face == "down":
            facedown = deck.cards.pop()
            print(facedown)
            return facedown

    def take_bet(self, player):
        while True:
            bet = int(input("How much would you like to bet?\n"))
            if bet <= 0:
                print("Bets cannot be 0 or negative.")
                continue
            elif bet > player.credits:
                print("Bets cannot exceed player's credits.")
                continue
            else:
                break
        player.credits -= bet
        return bet

    def award_bet(self, player):
        player.credits += (bet*2)

    def check_guess(self):
        while True:
            direction = input("Is the face-down card higher or lower?\n")
            if direction == "higher":
                if faceup > facedown:
                    print("You win")
                    return True
                else:
                    print("You lose")
                    return False

            elif direction == "lower":
                if faceup < facedown:
                    print("You win")
                    return True
                else:
                    print("You lose")
                    return False

            else:
                print("Please input either higher or lower.")
                continue

