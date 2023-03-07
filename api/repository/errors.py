class GenericException(Exception):
    def __str__(self):
        return "Query produced no results."


class ExpiredTokenException(Exception):
    def __str__(self):
        return "The supplied token has expired."


class InvalidCredentialsException(Exception):
    def __str__(self):
        return "Invalid credentials were entered."


class InvalidTokenException(Exception):
    def __str__(self):
        return "The supplied token is invalid."


class NoSuchGameException(Exception):
    def __str__(self):
        return "No game object can be found."


class UsernameTakenException(Exception):
    def __str__(self):
        return "The username has already been taken."


class NoSuchUserException(Exception):
    def __str__(self):
        return "The user cannot be found."
