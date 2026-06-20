from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://webscraper.io/test-sites/e-commerce/scroll/computers")
time.sleep(3)
for i in range (10):
    driver.execute_script(f'window.scrollTo(0, {i * 500});')
    time.sleep(1)

computers = driver.find_elements(By.CSS_SELECTOR,'div.thumbnail')
print(f'find {len(computers)}computers')

for computer in computers:
    name = computer.find_element(By.CSS_SELECTOR,'a.title').text
    price = computer.find_element(By.CSS_SELECTOR,'span').text
    print(name,'-',price)
driver.quit()
