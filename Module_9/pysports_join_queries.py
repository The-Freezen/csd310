import mysql.connector
from mysql.connector import connect, errorcode
from mysql.connector.cursor import MySQLCursor
config = {
    "user": "pysports_user",
    "password": "1qaz2wsx!QAZ@WSX",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()

sql = "SELECT player_id, first_name, last_name, team_name\
    FROM player \
    INNER JOIN team\
        ON player.team_id = team.team_id;"
cursor.execute(sql)
players = cursor.fetchall()
print("--Displaying Player Records--")
for player in players:
    print("Player Id: {}".format(player[0]));
    print("First Name: {}".format(player[1]));
    print("Last Name: {}".format(player[2]));
    print("Team Name: {}".format(player[3]));
    print(" ")
print("\n\n")
input("Press Enter to continue...")