import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.nzdirectory.co.nz/automotives.html"

response = requests.get(BASE_URL)
#print(response.content)

soup = BeautifulSoup(response.text,"html.parser")

itemlist = soup.findAll("li", {"class":"premium"})

for i in itemlist:
    print(i)