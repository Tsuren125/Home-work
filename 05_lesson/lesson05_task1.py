from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

# Кликаем на синюю кнопку по CSS-селектору
button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

time.sleep(2)  # задержка для наглядности
driver.quit()
