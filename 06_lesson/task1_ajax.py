from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

# нажимаем синюю кнопку
blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()

# ждем появления зеленой плашки
message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)

print(message.text)  # Data loaded with AJAX get request.
driver.quit()
