import time
from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_calculator_sum():
    driver = webdriver.Chrome()
    calc_page = CalculatorPage(driver)

    try:
        calc_page.open()
        calc_page.set_delay(45)

        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

        assert calc_page.get_result(), "Результат не равен 15"
    finally:
        driver.quit()
