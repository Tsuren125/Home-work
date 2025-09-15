class StringUtils:
    """
    Утилита для работы со строками.
    """

    def capitalize(self, string: str) -> str:
        """
        Делает первую букву строки заглавной.
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Убирает пробелы в начале и в конце строки.
        """
        return string.strip()

    def to_list(self, string: str, delimiter: str = ",") -> list:
        """
        Разбивает строку по разделителю на список.
        """
        if string == "":
            return []
        return string.split(delimiter)

    def contains(self, string: str, substring: str) -> bool:
        """
        Проверяет, содержится ли подстрока в строке.
        """
        return substring in string

