from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://books.toscrape.com/")

books= driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
print(f"found {len(books)} books")

for book in books:
    title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
    price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
    print(title, '-' ,price)



driver.quit()