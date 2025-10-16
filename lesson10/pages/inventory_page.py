import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """
    Страница оформления заказа (CheckoutPage).
    """

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Заполнить форму оформления заказа: {first_name} {last_name}, {postal_code}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа.
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    @allure.step("Получить общую сумму заказа")
    def get_total(self) -> str:
        """
        Возвращает общую сумму заказа.
        """
        return self.driver.find_element(*self.TOTAL_LABEL).text
