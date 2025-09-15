from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.ID, "delay")
        self.result_field = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds: int):
        field = self.driver.find_element(*self.delay_field)
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, value: str):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    def get_result(self, timeout=60):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_field, "15")
        )
