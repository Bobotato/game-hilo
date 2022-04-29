class Player:
    '''A class to represent a player and his wallet'''
    def __init__(self, wallet_bal=100):
        self.wallet_bal = wallet_bal

    @property
    def wallet_bal(self):
        return self._wallet_bal

    @wallet_bal.setter
    def wallet_bal(self, wallet_bal):
        self._wallet_bal = wallet_bal
        if self.wallet_bal < 0:
            raise ValueError("Player can't have negative wallet balance.")

    def bet(self, bet):
        if self.wallet_bal < bet:
            raise ValueError("Player can't bet more than the wallet balance.")
        self.wallet_bal -= bet
        return bet

    def __repr__(self):
        return f"A player with {self.wallet_bal} credits."

