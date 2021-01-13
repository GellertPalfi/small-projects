from requests import get
from bs4 import BeautifulSoup

from page_scraper.urban_dictionary_scraper import get_links
from objects.definitions import Definition


def definition_maker():
    """
    function scraping and creating definition objects
    """
    all_definitions = []
    definitions = get_links()
    print("parsing definitions...")
    for index in range(len(definitions)):
        soup = BeautifulSoup(get(definitions[index]).text, 'html.parser')
        name = soup.find('a', class_='word').text
        text = soup.find('div', class_='meaning').text
        example = soup.find('div', class_='example').text
        likes = soup.find('a', class_='up').text
        dislikes = soup.find('a', class_='down').text
        all_definitions.append(Definition(name, text, example, likes, dislikes))

    return all_definitions
