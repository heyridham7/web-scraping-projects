import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent

url = 'https://books.toscrape.com/'
session = requests.Session()
 
r = requests.get(url)

#print(r.text)

with open("file.html", "w") as f:
    f.write(r.text)

#soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.title.text)  