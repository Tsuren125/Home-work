from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

# Кликаем на синюю кнопку (динамический id → используем класс)
button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

time.sleep(2)
driver.quit()
