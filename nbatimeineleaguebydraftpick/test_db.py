import sqlite3

con = sqlite3.connect("nba.db")

cur = con.cursor()

sbys = cur.execute("""
            SELECT * FROM season_by_season
            """)

for line in sbys:
    print(line)