from requests import get
from bs4 import BeautifulSoup


url = 'https://www.urbandictionary.com'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')


def get_links():
    """
    method returning all 30 top definitions
    """
    all_quotes = soup.findAll('a', class_='trending-link')
    return ['https://www.urbandictionary.com' + link['href'] for link in all_quotes]
