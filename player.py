class Player:
    '''A class to represent a player and his wallet'''
    def __init__(self, wallet_bal = 100):
        self.wallet_bal = wallet_bal

    @property
    def wallet_bal(self):
        return self._wallet_bal

    @wallet_bal.setter
    def wallet_bal(self,wallet_bal):
        if self.wallet_bal < 0:
            raise ValueError("A player can't have negative wallet balance.")
        self._wallet_bal = wallet_bal

    def bet(self, bet):
        if self.wallet_bal > bet:
            raise ValueError("A player can't bet more than the wallet balance.")
        return bet

    def __repr__(self):
        return f"A player with {self.wallet_bal} credits."
