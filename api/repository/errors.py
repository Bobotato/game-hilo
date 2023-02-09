class GenericException(Exception):
    def __str__(self):
        return "Query produced no results."

class NoGameException(Exception):
    def __str__(self):
        return "No game object can be found."


class NoRoundInfoException(Exception):
    def __str__(self):
        return "No round info can be found."


class UsernameTakenException(Exception):
    def __str__(self):
        return "The username has already been taken."


class NoSuchUserException(Exception):
    def __str__(self):
        return "The user cannot be found."
