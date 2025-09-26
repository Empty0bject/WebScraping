#Main file

import requests #requests the HTML from websites
from bs4 import BeautifulSoup #makes the parsing and searching of the HTML (or XML) more intuative
from lxml import etree


def scrape():
    url = 'https://www.bbcgoodfood.com/recipes/chipotle-sweet-potato-black-bean-stew-cheddar-dumplings'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    dom = etree.HTML(str(soup))
    search(dom)

def search(dom):
    text = dom.xpath('/html/body/div[1]/div[5]/main/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/section/section')[0].text
    print(text)


if __name__ == '__main__':
    scrape()