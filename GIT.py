from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://github.com/trending")
time.sleep(3)
all_repos = []

repos = driver.find_elements(By.CSS_SELECTOR, "article.Box-row")

print(f"Found {len(repos)} repos")

for repo in repos:

    name = repo.find_element(
        By.CSS_SELECTOR,
        "h2 a"
    ).text.replace("\n", "").strip()

    try:
        language = repo.find_element(
            By.CSS_SELECTOR,
            '[itemprop="programmingLanguage"]'
        ).text.strip()
    except:
        language = ""

    try:
        description = repo.find_element(
            By.CSS_SELECTOR,
            "p"
        ).text.strip()
    except:
        description = ""

    all_repos.append([name, language, description])

with open("repos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name", "Language", "Description"])
    writer.writerows(all_repos)

print(f"Saved {len(all_repos)} repos to repos.csv")

driver.quit()