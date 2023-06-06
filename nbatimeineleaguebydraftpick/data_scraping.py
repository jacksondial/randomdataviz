import requests
from bs4 import BeautifulSoup
import csv
import sqlite3

url = "https://www.basketball-reference.com/players/a/abdelal01.html"

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table with class "stats_table" on the page
table = soup.find("table", class_="stats_table")

# Open a text file for writing
with open("player_stats.txt", "w") as file:
    # Iterate over each row in the table
    for row in table.find_all("tr"):
        # Iterate over each cell in the row
        for cell in row.find_all(["th", "td"]):
            # Write the cell's text content to the file
            file.write(cell.get_text().strip() + "\t")
        file.write("\n")

with open('player_stats.txt', 'r') as file:
    lines = file.readlines()

# Find the index of the blank line
blank_line_index = next((index for index, line in enumerate(lines) if line.strip() == ''), None)

if blank_line_index is None:
    print("Blank line not found in the file.")
else:
    # Split the lines into two lists
    season_stats = lines[:blank_line_index]
    team_summary = lines[blank_line_index + 1:]

    # Write season_stats to season_by_season_stats.txt
    with open('season_by_season_stats.txt', 'w') as file:
        file.writelines(season_stats)

    # Write team_summary to team_summary.txt
    with open('team_summary.txt', 'w') as file:
        file.writelines(team_summary)

# get the name of the current player

url = 'https://www.basketball-reference.com/players/a/abdelal01.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
player_name_element = soup.find("h1").find("span")
player_name = player_name_element.text.strip()
print(player_name)
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

with open('season_by_season_stats.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split('\t')
        data.append(player_name)
        cur.execute('''
            INSERT INTO season_by_season VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)


query = cur.execute("SELECT * FROM season_by_season")
for row in query:
    print(row)