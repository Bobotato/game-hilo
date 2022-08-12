class UsernameTakenException(Exception):
    def __str__(self):
        return "The username has already been taken."


class UserDoesNotExistException(Exception):
    def __str__(self):
        return "The user cannot be found."
