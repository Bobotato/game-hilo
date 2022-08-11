from database.connection import DatabaseConnection


class UserRepository:
    def __init__(self):
        self.dbc = DatabaseConnection()

    def add_new_entry(self, username: str, password: str) -> None:
        """
        Adds a new entry to the database

        :param username: The new player's username.
        :type username: str
        :param password: The new player's password.
        :type password: str
        """
        self.dbc.cursor.execute(
            "INSERT INTO users(username, password) VALUES (%s, %s);",
            (username, password),
        )

    def commit_update(self) -> None:
        self.dbc.connection.commit()

    def retrieve_all_entries(self):
        self.dbc.cursor.execute("SELECT * FROM users;")
        return self.dbc.cursor.fetchall()

    def retrieve_last_entry(self) -> tuple | None:
        self.dbc.cursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
        return self.dbc.cursor.fetchone()

    def retrieve_password_hash(self, username: str) -> tuple | None:
        self.dbc.cursor.execute(
            "SELECT password FROM users WHERE username = (%s);", (username,)
        )

        return self.dbc.cursor.fetchone()[0]

    def retrieve_user(self, username: str) -> tuple | None:
        self.dbc.cursor.execute(
            "SELECT username FROM users WHERE username = (%s);", (username,)
        )
        return self.dbc.cursor.fetchone()
