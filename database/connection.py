import psycopg2


class DatabaseConnection:
    def __init__(self):
        self.connection = self.connect_db()
        self.cursor = self.create_cursor()

    def add_new_player(self, username: str, password: str) -> None:
        self.cursor.execute(
            "INSERT INTO users(username, password) VALUES (%s, %s);",
            (username, password),
        )
        self.connection.commit()
        print(f"Added {username} as a new player!")

    def is_returning_player(self, username: str) -> bool:
        self.cursor.execute(
            "SELECT * FROM users WHERE username = (%s);", (username,)
        )

        if not self.cursor.fetchone():
            print("It looks like you're new.")
            return False

        print(f"Welcome back {username}.")
        return True

    def connect_db(self):
        connection = psycopg2.connect(
            user="hilo",
            password="hilo",
            host="localhost",
            port="5432",
            database="hilo",
        )
        return connection

    def create_cursor(self):
        cursor = self.connection.cursor()
        print(self.connection.get_dsn_parameters(), "\n")
        return cursor

    def is_password_correct(self, username, password) -> bool:
        self.cursor.execute(
            "SELECT password FROM users WHERE username = (%s);", (username,)
        )

        if password != self.cursor.fetchone()[0]:
            return False

        return True
