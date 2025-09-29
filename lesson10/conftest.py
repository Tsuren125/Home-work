import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """
    Фикстура для запуска и остановки браузера.

    Returns:
        WebDriver: Экземпляр Selenium WebDriver.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
