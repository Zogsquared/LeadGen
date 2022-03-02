import requests
from bs4 import BeautifulSoup

global nlp
info_list=[]
nlp=[]

BASE_URL = "https://www.nzdirectory.co.nz/automotives.html"

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

category = input("Enter Category name")

print(len(itemlist))
