import allure
from lesson_10.pages.login_page import LoginPage


@allure.title("Тест успешной авторизации")
@allure.description("Проверка входа в систему с валидными данными")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(driver):
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу логина"):
        login_page.open("https://example.com/login")

    with allure.step("Ввести валидные данные"):
        login_page.login("admin", "12345")

    with allure.step("Проверить, что вход выполнен"):
        assert login_page.is_logged_in()
