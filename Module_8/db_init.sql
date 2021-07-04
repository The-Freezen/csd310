DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password by '1qaz2wsx!QAZ@WSX';

	GRANT ALL ON pysports.* TO'pysports_user'@'localhost';

DROP TABLE IF EXISTS player;

DROP TABLE IF EXISTS team;

CREATE TABLE team (
	team_id	INT	NOT NULL	AUTO_INCREMENT,
	team_name	VARCHAR(75)	NOT NULL,
	mascot	VARCHAR(75)	NOT NULL,
	PRIMARY KEY(team_id)
);

CREATE TABLE player (
	player_id	INT	NOT NULL	AUTO_INCREMENT,
	first_name	VARCHAR(75)	NOT NULL,
	last_name	VARCHAR(75)	NOT NULL,
	team_id	INT	NOT NULL,
	PRIMARY KEY(PLAYER_ID),
	CONSTRAINT fk_team
	FOREIGN KEY(team_id)
		REFERENCES team(team_id)
);

INSERT INTO team(team_name, mascot)
	VALUES('Team Gandalf', 'White Wizards');

INSERT INTO team(team_name, mascot)
	VALUES('Team Sauron', 'Orcs');

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Thorin', 'Oakenshield', '1');

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Bilbo', 'Baggins', '1');

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Frodo', 'Baggins', '1');

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Saruman', 'The White', '2');

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Angmar', 'Witch-king', '2');

INSERT INTO player(first_name, last_name, team_id)
	VALUES('Azog', 'The Defiler', '2');