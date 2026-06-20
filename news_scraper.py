import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

titles = soup.find_all("span", class_="titleline")
scores = soup.find_all("span", class_="score")

all_stories = []
for title, score in zip(titles, scores):
    title_text = title.find("a").text
    score_text = score.text
    all_stories.append([title_text, score_text])

with open("stories.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Points"])
    writer.writerows(all_stories)

print(f"saved {len(all_stories)} stories to stories.csv")