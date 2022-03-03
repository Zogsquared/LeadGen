import requests
from bs4 import BeautifulSoup

global nlp
info_list=[]
nlp=[]

BASE_URL = "https://www.nzdirectory.co.nz/automotives.html"

def scrape_info(BASE_URL):
    response = requests.get(BASE_URL)
    #print(response.content)

    soup = BeautifulSoup(response.text,"html.parser")

    itemlist = soup.findAll("div", {"class":"listing_content"})
    print("Number of listings = " + str(len(itemlist)))

    for item in itemlist:
        address = item.find("p", class_="address")
        try:
            if address is not None:
                info_list.append([address.text])

                details = address.text

                i, a_phone = details.split('+', 1)
                a_name, a_location = i.split(', ', 1)

                nlp.append([a_name, a_location, a_phone])
        except:
            pass
    print(nlp)
    #print(address)

catgory = input("Enter Category name: ")

pageNum=["","-1","-2","-3","-4","-5","-6","-7","-8","-9","-10","-11","-12"] #List of pages in accommodation catagory

#Iterates over the pageNum list and sets the url to be sent to the scraper functions

for i in pageNum:
    scrape_info("https://www.nzdirectory.co.nz/accommodation"+str(i)+".html")