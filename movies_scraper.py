from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.scrapethissite.com/pages/ajax-javascript/#2015")
time.sleep(3)

movies = driver.find_elements(By.CSS_SELECTOR,'tr.film')
print(f'find {len(movies)}movies')

for movie in movies:

    title = movie.find_element(By.CSS_SELECTOR,'td.film-title').text
    nominations = movie.find_element(By.CSS_SELECTOR, 'td.film-nominations').text
    awards = movie.find_element(By.CSS_SELECTOR,'td.film-awards').text
    print(title,'-',nominations,'-',awards)

driver.quit()    
