import sys
from websitescraper import WebsiteProcess

class Main():
    def __init__(self):
        self.login= False

    def mainMenuDisplay():
        print("\n\n\tWelcome to MealPlanning\n\tSelect option\n1- Add Recipe\n2- View recipes\n3- Create a meal plan\n4. Quit")
        menuinput=input("Enter selection: ")
        if menuinput=="1":
            Main._addRecipe()
        elif menuinput=="2":
            Main._viewRecipe()
        elif menuinput=="3":
            Main._createMealPlan()
        elif menuinput=="4":
            sys.exit("Program terminated")
        else:
            print("Please enter either 1, 2 or 3\n")

    def _addRecipe():
        print("\nRecipes can either be uploaded from the bbc good food website or entered directly\n1- Enter from website\n2- Enter directly")
        recipeinputtype=input("Enter selection: ")

        if recipeinputtype=="1":
            websiteURL=input("Enter the website URL: ")
            #check for the correct URL, other websites or indepth error checking will be added here
            #moved try except loop to class function
            sitecheck=WebsiteProcess.request(websiteURL)
            if sitecheck!="":
                print(sitecheck)
                pass

            #Very rough system for now, check off which data the user would like saved
            print("Which data would you like to be included in the save? Please select Y/N\nThe input is not case sensitive")
            for item in len(WebsiteProcess.optionaldata):
                userrequest=(WebsiteProcess.optionaldata[item]+"?")
                if userrequest.lower()=="y":
                    WebsiteProcess.datarequest[item]=True
                elif userrequest.lower()=="n":
                    WebsiteProcess.datarequest[item]=False
                else:
                    print("Please re-enter your answer using either 'y' or 'n'")
                    item=-1
            print(WebsiteProcess.datarequest)

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