"""Get All URLs from website."""
import requests
from bs4 import BeautifulSoup
import string
 

url = "https://www.basketball-reference.com/players/a/"


def get_ext_list(url: str) -> list:
    """
    Function to pull all individual players' URLs associated with a specific 
    letter in the alphabet from the basketball reference website used.
    """
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
        # print(link.get('href'))
    
    only_player_urls = [ext for ext in urls if 'players/a' in ext]
    return(only_player_urls)


# print(get_ext_list(url))