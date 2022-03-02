import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.nzdirectory.co.nz/automotives.html"

response = requests.get(BASE_URL)
#print(response.content)

soup = BeautifulSoup(response.text,"html.parser")

itemlist = soup.findAll("div", {"class":"listing_content"})
print("Number of listings = " + str(len(itemlist)))

for item in itemlist:
    address = item.find("p", {"class":"address"})
    print(address)

print(len(itemlist))
