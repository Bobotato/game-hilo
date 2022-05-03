class Game:
    """This class includes all the methods required for the game of Hilo"""
    def draw(self, deck):
        return deck.cards.pop()

    def take_bet(self, player, bet):
        if bet <= 0:
            raise ValueError("Bets cannot be 0 or negative.")
        elif bet > player.credits:
            raise ValueError("Bets cannot exceed player's credits.")
        player.credits -= bet

    def award_bet(self, player, bet):
        player.credits += (bet*2)
        
    def check_guess(self, guess, faceup, facedown):
        if guess == "higher":
            if faceup > facedown:
                return True
            else:
                return False
        elif guess == "lower":
            if faceup < facedown:
                return True
            else:
                return False

