import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://books.toscrape.com"
r = requests.get(url)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

timestamp = datetime.now().strftime("%Y-%M-%D  %H:%M:%S")

rows = []
for book in books:
    title = book.h3.a["title"]
    price = book.find ('p', class_="price_color").text
    rows.append([timestamp,title,price])

with open("price_history.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"logged {len(rows)} prices at {timestamp}")