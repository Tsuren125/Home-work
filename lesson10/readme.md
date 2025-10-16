# Домашнее задание №10 – Документация и Allure

## Как запустить тесты
1. Установить зависимости:
pip install -r requirements.txt

markdown
Копировать код
2. Запустить тесты с формированием отчёта:
pytest --alluredir=allure_results

markdown
Копировать код
3. Посмотреть отчёт:
allure serve allure_results

markdown
Копировать код

## Структура проекта
- `pages/` — классы страниц (Page Object)
- `tests/` — тесты
- `conftest.py` — фикстуры
- `readme.md` — инструкция по запуску

Allure-разметка добавлена для шагов и проверок.  
Проект проверен линтером flake8 и соответствует PEP8.
