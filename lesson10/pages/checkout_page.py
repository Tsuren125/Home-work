import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """
    Страница оформления заказа (CheckoutPage).
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор страницы оформления заказа.

        Args:
            driver (WebDriver): Экземпляр Selenium WebDriver.
        """
        self.driver = driver

    @allure.step("Заполнить форму оформления заказа: {first_name} {last_name}, {postal_code}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнение формы оформления заказа.

        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            postal_code (str): Почтовый индекс.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить общую сумму заказа")
    def get_total(self) -> str:
        """
        Получение итоговой суммы заказа.

        Returns:
            str: Текстовое значение с суммой (например, 'Total: $32.39').
        """
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
