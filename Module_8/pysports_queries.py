import mysql.connector
from mysql.connector import connect, errorcode
config = {
    "user": "pysports_user",
    "password": "1qaz2wsx!QAZ@WSX",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()

for team in teams:
    print("Team ID: {}".format(team[1]));
    print("Team Name: {}".format(team[1]));
    print("Mascot: {}".format(team[1]));

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()
for player in players:
    print("Player ID: {}".format(player[2]));
    print("First Name: {}".format(player[2]));
    print("Last Name: {}".format(player[2]));
    print("Team ID: {}".format(player[2]))