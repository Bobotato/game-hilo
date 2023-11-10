from dataclasses import dataclass


@dataclass
class Credentials:
    """This class contains a user's attempted login credentials"""

    username: str
    password: str
