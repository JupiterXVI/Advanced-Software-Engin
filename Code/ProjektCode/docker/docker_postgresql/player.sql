CREATE TABLE player(
    player_id serial PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    age VARCHAR(50) NOT NULL,
    is_admin BOOLEAN NOT NULL
);

CREATE TABLE game(
    game_id serial PRIMARY KEY, 
    game VARCHAR (50) NOT NULL,
    game_description VARCHAR (255)
);

CREATE TABLE gamestats(
    fk_player_id serial,
    fk_game_id serial,
    FOREIGN KEY (fk_player_id) 
        REFERENCES player (player_id) 
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (fk_game_id) 
        REFERENCES game(game_id) 
        ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (fk_player_id, fk_game_id),
    wins INT NOT NULL,
    losses INT NOT NULL
);

INSERT INTO player(player_id, username, password, age, is_admin) 
VALUES(0, 'admin', 'admin', '99', TRUE);

INSERT INTO player(player_id, username, password, age, is_admin) 
VALUES(1, 'Anonymous1', '', '12', FALSE);

INSERT INTO player(player_id, username, password, age, is_admin) 
VALUES(2, 'Anonymous2', '', '12', FALSE);

INSERT INTO player(username, password, age, is_admin) 
VALUES('Tim', '!geiheim1', '16', FALSE);
