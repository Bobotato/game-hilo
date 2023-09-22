CREATE TABLE user_details (
    username VARCHAR(255) NOT NULL,
    password_hash VARCHAR,
    PRIMARY KEY (username)
);

CREATE TABLE gamestates (
    id SERIAL NOT NULL,
    game VARCHAR,
    username VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(username) REFERENCES user_details (username)
);


