class NoGameException(Exception):
    def __str__(self):
        return "No game object can be found."


class NoRoundInfoException(Exception):
    def __str__(self):
        return "No round info can be found."
