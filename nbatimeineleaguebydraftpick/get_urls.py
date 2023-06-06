"""Get All URLs from website."""
import requests
from bs4 import BeautifulSoup
import string
 
# url = 'https://www.geeksforgeeks.org/'
url = "https://www.basketball-reference.com/players/a/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))
    # print(link.get('href'))

only_players = [ext for ext in urls if 'players/a' in ext]
print(only_players)