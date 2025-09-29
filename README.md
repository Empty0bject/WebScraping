# WebScraping
Following the Medium introduction to building a webscraper (https://medium.com/@joerosborne/intro-to-web-scraping-build-your-first-scraper-in-5-minutes-1c36b5c4b110)

The domain used is example.com because as stated in the article, many high trafic websites can have bot detection that can be hard to bypass  
In the future Id like to create a price comparison tool to help me in my day to day shopping, or when looking to shop online and find the best deal in a certain reveiw space, eg yarn less than £10 with more than 4 stars on amazon  
I have no prior knowledge of how webscrapers work so this is also a big learning opertunity for me, I thought this would also be a good first step in learning how to create an API  

Following a text tutorial while also trying to demonstrate my learning can be difficult, as such Ill use most of the code directly from the article while commenting accordingly based on what i learn  


# Meal Prepping app

With how easy it was to create the webscraper, Id like to create a simple project to create a shopping list off the ingredients on a recipie site  
Any plans will be attached in post  

Website used in testing will be https://www.bbcgoodfood.com/recipes/chipotle-sweet-potato-black-bean-stew-cheddar-dumplings  
As this is a personal project i see it as less important to have cross site functionality, and i like to use good food

### Programming log
Theres quite a big jump in difficulty on the good food website since theres naturally a lot more data in a much different format, I did however find a similar github repo to the project Im trying to create at (https://github.com/cameronjoejones/bbc-good-food-webscraper) so Ill do the same as earlier and adapt the code to this project, commenting along the way  
- Unfortunately this didnt work  
I am now attempting to convert to an lxml.etree object in order to use xpath data
- I think i may be a fool and was just looking at the wrong data when looking for the class i required, going back to using only bs4

- <img width="1292" height="691" alt="image" src="https://github.com/user-attachments/assets/0df9c3c5-c7cc-44db-8517-bcb2ff5c3b40" />
