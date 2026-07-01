from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://timesofindia.indiatimes.com")
time.sleep(6)

headlines = driver.find_elements(By.CSS_SELECTOR, "a[href*='/articleshow/']")
print(f"found {len(headlines)} headlines")

all_headlines = []
for headline in headlines:
    text = headline.text.strip()
    link = headline.get_attribute("href")
    if text:  # skip empty ones
        all_headlines.append([text, link])

with open("toi_headlines.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Headline", "Link"])
    writer.writerows(all_headlines)

print(f"saved {len(all_headlines)} headlines to toi_headlines.csv")

driver.quit()