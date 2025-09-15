import pytest
from string_utils import StringUtils


class TestStringUtils:

    # --- Тесты для capitalize ---
    @pytest.mark.parametrize("input_str, expected", [
        ("тест", "Тест"),
        ("Test", "Test"),
        ("123abc", "123abc"),
        ("", ""),
        (" ", " "),
    ])
    def test_capitalize(self, input_str, expected):
        utils = StringUtils()
        assert utils.capitalize(input_str) == expected

    def test_capitalize_none(self):
        utils = StringUtils()
        with pytest.raises(AttributeError):  # .capitalize() не работает с None
            utils.capitalize(None)

    # --- Тесты для trim ---
    @pytest.mark.parametrize("input_str, expected", [
        ("  тест  ", "тест"),
        ("тест", "тест"),
        ("  ", ""),
    ])
    def test_trim(self, input_str, expected):
        utils = StringUtils()
        assert utils.trim(input_str) == expected

    def test_trim_none(self):
        utils = StringUtils()
        with pytest.raises(AttributeError):
            utils.trim(None)

    # --- Тесты для to_list ---
    @pytest.mark.parametrize("input_str, delimiter, expected", [
        ("a,b,c", ",", ["a", "b", "c"]),
        ("a;b;c", ";", ["a", "b", "c"]),
        ("", ",", []),
    ])
    def test_to_list(self, input_str, delimiter, expected):
        utils = StringUtils()
        assert utils.to_list(input_str, delimiter) == expected

    def test_to_list_none(self):
        utils = StringUtils()
        with pytest.raises(AttributeError):
            utils.to_list(None, ",")

    # --- Тесты для contains ---
    @pytest.mark.parametrize("input_str, substring, expected", [
        ("hello world", "world", True),
        ("hello world", "python", False),
        ("", "a", False),
    ])
    def test_contains(self, input_str, substring, expected):
        utils = StringUtils()
        assert utils.contains(input_str, substring) == expected

    def test_contains_none(self):
        utils = StringUtils()
        with pytest.raises(TypeError):
            utils.contains(None, "test")
