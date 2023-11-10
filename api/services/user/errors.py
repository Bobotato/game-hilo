class JWTEnvNotFoundException(Exception):
    def __str__(self):
        return "The JWT init variables have not been found."


class TokenMismatchException(Exception):
    def __str__(self):
        return "The tokens provided do not match."
