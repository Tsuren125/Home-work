from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """
    Базовый класс для всех страниц.

    Attributes:
        driver (WebDriver): Экземпляр Selenium WebDriver.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор страницы.

        Args:
            driver (WebDriver): Экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Открыть страницу по URL.

        Args:
            url (str): Ссылка на страницу.

        Returns:
            None
        """
        self.driver.get(url)
