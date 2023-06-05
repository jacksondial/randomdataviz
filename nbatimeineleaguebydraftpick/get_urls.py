"""Get All URLs from website."""
import requests
from bs4 import BeautifulSoup

# URL of the directory page
url = "https://www.basketball-reference.com/players/"

# Send a GET request to the directory page
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, "html.parser")

ul = soup.find("ul", id="players")

# Find all the links within the ul
links = ul.find_all("a")

# Extract the URLs and store them in a list
urls = [link["href"] for link in links]

# Print the list of URLs
for url in urls:
    print(url)


