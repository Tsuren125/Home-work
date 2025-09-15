from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

# вводим текст
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# нажимаем синюю кнопку
blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()

# получаем текст кнопки
print(blue_button.text)  # SkyPro
driver.quit()
