from bs4 import BeautifulSoup
import requests
import csv

all_quotes=[]
for page in range(1,11):
    url=f"https://quotes.toscrape.com/page/{page}/"

    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text,'html.parser')

    print(r.status_code)
    print(soup.title.text)

    quotes = soup.find_all("div", class_ = 'quote')
    print(f'found {len(quotes)} quotes')
    for quote in quotes:
        text = quote.find('span' , class_ = 'text').text
        author = quote.find('small', class_ = 'author').text
        all_quotes.append([text,author])

with open('quotes.csv','w',newline= "",encoding = 'utf-8')as f:
    writer = csv.writer(f)
    writer.writerow(["Text","Author"])
    writer.writerows(all_quotes)

print(f"saved{len(all_quotes)} quotes to quotes.csv")
