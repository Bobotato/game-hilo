CREATE TABLE gamestates (
    id INTEGER NOT NULL,
    game VARCHAR(255),
    username VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(username) REFERENCES user_details (username)
);

CREATE TABLE user_details (
    username VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255),
    PRIMARY KEY (username)
);
