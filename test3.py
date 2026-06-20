from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.flipkart.com/sa-sa-le-le-laptops-at-store?PARAM=8762&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhcHRvcHMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19")
time.sleep(3)

laptops = driver.find_elements(By.CSS_SELECTOR,"div._1AtVbE")
print(f"found {len(laptops)} laptops")

for laptop in laptops:
    try:
        title = laptop.find_element(By.CSS_SELECTOR,"div._4rR01T").text
        price = laptop.find_element(By.CSS_SELECTOR,'div._30jeq3._1_WHN1').text
        print(title,'-',price)
    except:
        pass

driver.quit()
