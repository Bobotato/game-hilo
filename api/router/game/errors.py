class NoRoundInfoException(Exception):
    def __str__(self):
        return "No round info can be found."
