from bs4 import BeautifulSoup
import requests
import csv

all_jobs=[]
url=f"https://realpython.github.io/fake-jobs/"

r = requests.get(url)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text,'html.parser')

print(r.status_code)
print(soup.title.text)

jobs = soup.find_all("div", class_ = 'card-content')
print(f'found {len(jobs)} jobs')
for job in jobs:
        try:
            title = job.find('h2' , class_ = 'title').text
            company = job.find('h3', class_ = 'subtitle').text
            location = job.find('p', class_='location').text.strip().replace('\n', '').replace('  ', '')
            all_jobs.append([title,company,location])
        except:
            pass

with open('jobs.csv','w',newline= "",encoding = 'utf-8')as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["Title","Comapny","Location"])
    writer.writerows(all_jobs)

print(f"saved{len(all_jobs)} jobs to jobs.csv")
