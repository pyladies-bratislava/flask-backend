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


PYLADIES_URL="https://pyladies.com/about/"
PYLADIES_ABOUT_FILE_NAME = "pyladies_about_text.txt"


def get_pyladies_about_scraping(url=PYLADIES_URL):
    """ scrapes official pyladies website;
    returns pyladies_about_info str variable
    with info about pyladies;
    if the structure of the scraped website is changed,
    assigns url address as str instead """

    page = requests.get(PYLADIES_URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # getting the desired paragraph from scraped html page
    div_class_page = soup.find("div", {"class": "page"})
    pyladies_about_scraped = div_class_page.find("p")

    if pyladies_about_scraped:
        pyladies_about_scraped = pyladies_about_scraped.text.strip()

    # in case the pyladies international website's structure is changed
    else:
        pyladies_about_scraped = "Something went wrong :(. Please visit " + PYLADIES_URL + " for the info from the international Pyladies website"

    return pyladies_about_scraped




def get_pyladies_about_text():
    """Get paragraph1 & paragraph2 from the pyladies_about.txt file;
    paragraph1 - till [Pyladies_snake]
    paragraph2 - between [Pyladies_snake] & [Pyladies.com_text]
    paragraph3 - from scraping
    paragraph4 - from [Pyladies.com_text] 
    """

    from flask_main import BASE_DIR
    text_file = os.path.join(BASE_DIR, "resources", PYLADIES_ABOUT_FILE_NAME)

    paragraph1 = ""
    paragraph2 = ""
    paragraph3 = ""
    paragraph4 = ""

    with open(text_file, encoding = 'utf-8') as file_:

        for line in file_:                  # starts at the beginning
            line = line.strip()
            
            if line == "[Pyladies_snake]":

                for line in file_:          # starts at line below [Pyladies_snake]
                    
                    line = line.strip()
    
                    if line == "[Pyladies.com_text]":

                        for line in file_:  # starts at line below [Pyladies.com_text]
                            line = line.strip()
                            paragraph4 = paragraph4 + line
                    
                    else:
                        paragraph2 = paragraph2 + line
            else:
                paragraph1 = paragraph1 + line
        
    paragraph3 = get_pyladies_about_scraping()

    if paragraph1 == "":
        paragraph1 = "paragraph1"
        
    if paragraph2 == "":
        paragraph2 = "paragraph2"

    if paragraph4 == "":
        paragraph4 = "paragraph4"

    return paragraph1, paragraph2, paragraph3, paragraph4

