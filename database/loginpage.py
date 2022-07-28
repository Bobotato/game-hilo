import psycopg2


def add_new_player(cursor, username, password) -> None:
    cursor.execute(
        "INSERT INTO users(username, password) VALUES (%s, %s);",
        (username, password),
    )
    print(f"Added {username} as a new player!")


def is_returning_player(cursor, username) -> bool:
    cursor.execute("SELECT * FROM users WHERE username = (%s);", (username,))

    if not cursor.fetchone():
        print("It looks like you're new.")
        return False

    print(f"Welcome back {username}.")
    return True


def connect_db():
    connection = psycopg2.connect(
        user="alex",
        password="alexvm",
        host="localhost",
        port="5432",
        database="hilo",
    )
    return connection


def create_cursor(connection):
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "\n")
    return cursor


def is_password_correct(cursor, username, password):
    cursor.execute(
        "SELECT password FROM users WHERE username = (%s);", (username,)
    )

    if password != cursor.fetchone()[0]:
        return False

    return True
