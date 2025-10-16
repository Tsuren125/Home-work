import pytest
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Оформление заказа на SauceDemo")
@allure.description("Проверка, что сумма заказа после оформления равна $58.29")
def test_shop_checkout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.add_to_cart("Sauce Labs Onesie")
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Tsyren", "Gomboev", "670000")

    total = checkout.get_total()
    assert total == "Total: $58.29", f"Ожидалось $58.29, но получили {total}"
