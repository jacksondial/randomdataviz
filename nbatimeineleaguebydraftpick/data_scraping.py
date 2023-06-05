import requests
from bs4 import BeautifulSoup
import csv

# URL = "https://www.basketball-reference.com/players/a/"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id="wrap")
# print(results.type)
# content = results.find("div", class_ = "content")
# print(content.type)
# table_wrapper = content.find("div", class_ = "table_wrapper")
# table_containter_is_setup = table_wrapper.find("div", class_ = "table_container is_setup")
# stats_table = table_containter_is_setup.find("div", class_ = "sortable stats_table now_sortable")

# print(stats_table.prettify())

# Starting now from a single page of one player
# this is going to loop through all of the a's


# root = "https://www.basketball-reference.com"
# website = f'{root}/players/a'
# result = requests.get(website)
# content = result.text
# soup = BeautifulSoup(content, "html.parser")

# box = soup.find(id = "wrap")
# box.find_all("a", href = True)

# for link in box.find_all("a", href = True):
#     link['href']

# links = [link['href'] for link in box.find_all("a", href = True)]
# print(links)


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

