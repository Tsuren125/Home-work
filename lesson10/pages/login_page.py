from .base_page import BasePage
import allure


class LoginPage(BasePage):
    """
    Страница авторизации.
    """

    username_field = "input#username"
    password_field = "input#password"
    login_button = "button#login"

    @allure.step("Ввести логин '{username}' и пароль")
    def login(self, username: str, password: str) -> None:
        """
        Авторизация пользователя.

        Args:
            username (str): Логин пользователя.
            password (str): Пароль пользователя.

        Returns:
            None
        """
        self.driver.find_element("css selector", self.username_field).send_keys(username)
        self.driver.find_element("css selector", self.password_field).send_keys(password)
        self.driver.find_element("css selector", self.login_button).click()

    @allure.step("Проверка, что пользователь авторизован")
    def is_logged_in(self) -> bool:
        """
        Проверка успешной авторизации.

        Returns:
            bool: True, если авторизация успешна, иначе False.
        """
        return "dashboard" in self.driver.current_url
