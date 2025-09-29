from main import Main
import requests #requests the HTML from websites
from bs4 import BeautifulSoup #makes the parsing and searching of the HTML (or XML) more intuative

class WebsiteProcess():
    def __init__(self):
        self.dataoutput=[[[]]]
        __soup=[[]]
        __datarequest=[[]]


    def request(websiteURL):
        pass
        #response = requests.get(websiteURL)
        #soup = BeautifulSoup(response.text, 'html.parser')
        #return soup

    def parse(requestedData):
        pass
        #ingredients = requestedData.find('ul', {'class': 'ingredients-list list'}).text
        #print(ingredients)

class RecipeDataProcess():
    def __init__(self):
        pass

    def saveRecipe():
        pass

    def saveMealPlan():
        pass