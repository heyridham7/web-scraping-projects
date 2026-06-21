from bs4 import BeautifulSoup
import requests
import csv

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
headers = {"User-Agent":"Mozilla/5.0"}

r = requests.get(url , headers=headers)
soup  = BeautifulSoup(r.text,"html.parser")

table = soup.find('table', class_="wikitable")
rows = table.find_all('tr')

all_data=[]

for row in rows:
    cells = row.find_all("td")
    if len(cells)>= 4:
        country = cells[0].text.strip()
        country = country.split("[")[0].strip() 
        imf_estimate = cells[1].text.strip()
        all_data.append([country , imf_estimate])

print(f"found{len(all_data)}countries")

with open ("gdp_by_country.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Counrty","GDP(IMF estimate,million USD)"])
    writer.writerows(all_data)

print("saved to gdp_by_country.csv")