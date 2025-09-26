#Main file

import requests #requests the HTML from websites
from bs4 import BeautifulSoup #makes the parsing and searching of the HTML (or XML) more intuative


def scrape():
    url = 'https://www.bbcgoodfood.com/recipes/chipotle-sweet-potato-black-bean-stew-cheddar-dumplings'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search(soup)

def search(soup):
    ingredients = soup.find('ul', {'class': 'ingredients-list list'}).text
    print(ingredients)


if __name__ == '__main__':
    scrape()