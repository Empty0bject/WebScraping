import requests #requests the HTML from websites
from bs4 import BeautifulSoup #makes the parsing and searching of the HTML (or XML) more intuative

class WebsiteProcess():
    def __init__(self):
        self.dataoutput=[[]]
        self.__soup=""
        self.optionaldata=["Calories per serving","Prep time","Cook time","Servings per dish","Difficulty"]
        self.datarequest=[]

    def request(websiteURL):
        try:
            response = requests.get(websiteURL)
            soup = BeautifulSoup(response.text, 'html.parser')
            WebsiteProcess.__soup=soup
            return ""
        except:
            return "There is an issue with the URL or internet connection, please try again"
            #new private funtion could be added to check for specific errors

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