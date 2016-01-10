-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE IF EXISTS Matches CASCADE;
DROP TABLE IF EXISTS Players CASCADE;
DROP VIEW IF EXISTS Player_Standings;

CREATE TABLE Players (id SERIAL PRIMARY KEY,
  name text NOT NULL
);

CREATE TABLE Matches (match_id SERIAL PRIMARY KEY,
  winner int NOT NULL,
  loser int NOT NULL,
  FOREIGN KEY(winner) REFERENCES Players(id),
  FOREIGN KEY(loser) REFERENCES Players(id)
);

CREATE VIEW Match_Count AS
SELECT Players.id as player_id, COUNT(Matches.winner) as matches
FROM Players LEFT JOIN Matches
ON Players.id = Matches.winner
OR Players.id = Matches.loser
GROUP BY Players.id;

CREATE VIEW Win_Count AS
SELECT Players.id as player_id, COUNT(Matches.winner) as wins
FROM Players LEFT JOIN Matches
ON Players.id = Matches.winner
GROUP BY Players.id;

CREATE VIEW Player_Standings AS
SELECT Players.id, Players.name, Win_Count.wins, Match_Count.matches
FROM Players
INNER JOIN Win_Count ON Players.id = Win_Count.player_id
INNER JOIN Match_Count ON Win_Count.player_id = Match_Count.player_id
GROUP BY Win_Count.wins, Players.id, Match_Count.matches
ORDER BY Win_Count.wins desc;

SELECT a.id, a.name, b.id, b.name
FROM Player_Standings AS a, Player_Standings AS b
WHERE a.wins = b.wins
AND a.id > b.id;


