from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://quotes.toscrape.com/js/")

quotes = driver.find_elements(By.CSS_SELECTOR,'div.quote')
print(f'find {len(quotes)}quotes')

for quote in quotes:
    text = quote.find_element(By.CSS_SELECTOR,'span.text').text
    author = quote.find_element(By.CSS_SELECTOR,'small.author').text
    print(text,'-',author)

driver.quit()
