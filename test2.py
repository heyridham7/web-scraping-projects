import requests
from bs4 import BeautifulSoup
import csv

all_books = []
for page in range (1,6):
    url =f"https://books.toscrape.com/catalogue/page-{page}.html"
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text ,'html.parser')

    print(r.status_code)
    print(soup.title.text)

    books = soup.find_all('article', class_ = 'product_pod')
    print(f'page {page} :found{len(books)} books')
    for book in books :
        title = book.h3.a['title']
        price = book.find('p',class_ = 'price_color').text
        all_books.append([title , price])

with open('book.csv','w', newline ="" , encoding = 'utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Title","Price"])
    writer.writerows(all_books)

print(f"saved {len(all_books)}Books to books.csv")


  