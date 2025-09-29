from websitescraper import WebsiteProcess

class Main():
    def __init__(self):
        self.login= False

    def mainMenuDisplay():
        print("\n\n\tWelcome to MealPlanning\n\tSelect option\n1- Add Recipe\n2- View recipes\n3- Create a meal plan")
        menuinput=input("Enter selection: ")
        if menuinput=="1":
            Main._addRecipe()
        elif menuinput=="2":
            Main._viewRecipe()
        elif menuinput=="3":
            Main._createMealPlan()
        else:
            print("Please enter either 1, 2 or 3\n")

    def _addRecipe():
        print("\nRecipes can either be uploaded from the bbc good food website or entered directly\n1- Enter from website\n2- Enter directly")
        recipeinputtype=input("Enter selection: ")
        if recipeinputtype=="1":
            websiteURL=input("Enter the website URL: ")
            try:
                websitedata=WebsiteProcess.request(websiteURL)
                print("data obtained correctly")
            except:
                print("Please enter a valid URL or check your internet connection")
                #need to add in error catching for each type of error

        elif recipeinputtype=="2":
            pass
        else:
            print("Please enter either 1 or 2")

    def _viewRecipe():
        print("view recipe")

    def _createMealPlan():
        print("create meal plan")


while __name__ == '__main__':
    Main.mainMenuDisplay()