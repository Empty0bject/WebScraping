#Main file

import requests #requests the HTML from websites
from bs4 import BeautifulSoup #makes the parsing and searching of the HTML (or XML) more intuative


def scrape():
    url = 'https://www.example.com' #any given url, to the desired page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup) outputs the page with its HTML formatting
    search(soup)

def search(soup):
    title = soup.select_one('h1').text #selects the HTML in the specified formatting, in this case h1 is the header
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href') #'href' meaning the page that any links point towards

    print(title)
    print(text)
    print(link)



if __name__ == '__main__':
    scrape()