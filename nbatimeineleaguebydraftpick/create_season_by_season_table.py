"Create season_by_season table"
import sqlite3

con = sqlite3.connect("nba.db")

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS season_by_season")
cur.execute(
    """
    CREATE TABLE season_by_season (
        Season TEXT,
        Age INTEGER,
        Tm TEXT,
        Lg TEXT,
        Pos TEXT,
        G INTEGER,
        GS INTEGER,
        MP REAL,
        FG REAL,
        FGA REAL,
        FG_percent REAL,
        `3P` REAL,
        `3PA` REAL,
        `3P_percent` REAL,
        `2P` REAL,
        `2PA` REAL,
        `2P_percent` REAL,
        eFG_percent REAL,
        FT REAL,
        FTA REAL,
        FT_percent REAL,
        ORB REAL,
        DRB REAL,
        TRB REAL,
        AST REAL,
        STL REAL,
        BLK REAL,
        TOV REAL,
        PF REAL,
        PTS REAL,
        PLAYER VARCHAR(255)
    )
    """
)
con.commit()
con.close()