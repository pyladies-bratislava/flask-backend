# This file scrapes the official pyladies 
# website 'https://pyladies.com/about/'
# and assigns about info text to 
# str type variable 'pyladies_about_scraped'
# which can be further used in our website

# in case the structure is of official pyladies
# website is changed in future, link to the website
# as str is assigned to 'pyladies_about_scraped' variable

import os
import requests
from bs4 import BeautifulSoup   # for web scraping

pyladies_url="https://pyladies.com/about/"

paragraph1 = ""
paragraph2 = ""
paragraph3 = ""
paragraph4 = ""

def get_pyladies_about_scraping(url=pyladies_url):
    """ scrapes official pyladies website;
    returns pyladies_about_info str variable
    with info about pyladies;
    if the structure of the scraped website is changed,
    assigns url address as str instead """

    page = requests.get(pyladies_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # getting the desired text from scraped html page
    div_class_page = soup.find("div", {"class": "page"})
    pyladies_about_scraped = div_class_page.find("p")

    if pyladies_about_scraped:
        pyladies_about_scraped = pyladies_about_scraped.text.strip()
    # in case the website's structure is changed
    else:
        pyladies_about_scraped= "Something went wrong :(. Please visit " + pyladies_url + " for the info from the international Pyladies website"

    return pyladies_about_scraped


dirname = os.path.dirname(__file__)
text_file = os.path.join(dirname, "pyladies_about_text")

def get_pyladies_about_text(paragraph1=paragraph1, paragraph2=paragraph2, paragraph3=paragraph3, paragraph4=paragraph4):
    """Get paragraph1 & paragraph2 from the pyladies_about.txt file;
    paragraph1 - till [Pyladies_snake]
    paragraph2 - between [Pyladies_snake] & [Pyladies.com_text]
    paragraph3 - from scraping
    paragraph4 - from [Pyladies.com_text] 
    """

    with open(text_file, encoding = 'utf-8') as file_:

        for line in file_:        
            line = line.strip()
            
            if line == "[Pyladies_snake]":

                for line in file_:
                    line = line.strip()
    
                    if line == "[Pyladies.com_text]":

                        for line in file_:
                            line = line.strip()
                            paragraph4 = paragraph4 + line
                    
                    else:
                        paragraph2 = paragraph2 + line
            else:
                paragraph1 = paragraph1 + line
        
    paragraph3 = get_pyladies_about_scraping()

    return paragraph1, paragraph2, paragraph3, paragraph4



if __name__ == "__main__":
    paragraph1, paragraph2, paragraph3, paragraph4 = get_pyladies_about_text()

    print(
        "PAR 1\n" + paragraph1 + "\n\n" +
        "PAR 2\n" + paragraph2 + "\n\n" +
        "PAR 3\n" + paragraph3 + "\n\n" +
        "PAR 4\n" + paragraph4
    )
    pass