import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
from get_urls import get_ext_list

# Currently I am facing the issue that the stats tables from each of the
# players are not the same size and have the same columns... is pretty
# frustrating but I have got to figure out a way to either only take the
# standardized tables (not ideal) or to have a table with all possible
# columns and check if certain statistics are reported....

player_extensions = get_ext_list("https://www.basketball-reference.com/players/a/")
# url = "https://www.basketball-reference.com/players/a/abdelal01.html"
root_url = "https://www.basketball-reference.com"

con = sqlite3.connect("nba.db")
cur = con.cursor()

for player_ext in player_extensions:
    # Send a GET request to the website
    player_url = root_url + player_ext
    response = requests.get(player_url)

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

    with open("player_stats.txt", "r") as file:
        lines = file.readlines()

    # Find the index of the blank line
    blank_line_index = next(
        (index for index, line in enumerate(lines) if line.strip() == ""), None
    )

    if blank_line_index is None:
        print("Blank line not found in the file.")
    else:
        # Split the lines into two lists
        season_stats = lines[:blank_line_index]
        team_summary = lines[blank_line_index + 1 :]

        # Write season_stats to season_by_season_stats.txt
        with open("season_by_season_stats.txt", "w") as file:
            file.writelines(season_stats)

        # Write team_summary to team_summary.txt
        with open("team_summary.txt", "w") as file:
            file.writelines(team_summary)

    # get the name of the current player
    player_name_element = soup.find("h1").find("span")
    player_name = player_name_element.text.strip()

    with open("season_by_season_stats.txt", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.strip().split("\t")
            data.append(player_name)
            cur.execute(
                """
                INSERT INTO season_by_season VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                data,
            )


# query = cur.execute("SELECT * FROM season_by_season")
# for row in query:
#     print(row)
