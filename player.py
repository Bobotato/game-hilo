class Player:
    '''A class to represent a player and their money'''
    def __init__(self, money=100):
        self.money = money

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money
        if self.money < 0:
            raise ValueError("Player can't have negative money.")

    def bet(self, bet):
        if self.money < bet:
            raise ValueError("Player can't bet more money than they have.")
        self.money -= bet
        return bet

    def __repr__(self):
        return f"A player with {self.money} credits."

