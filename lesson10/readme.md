# Lesson 10 – Allure + Документация

## 🚀 Как запустить тесты с Allure

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
Запустите тесты с генерацией отчёта:

bash
Копировать код
pytest --alluredir=allure_results
Просмотрите отчёт:

bash
Копировать код
allure serve allure_results
⚠️ Папки allure_results и allure_report пушить в репозиторий не нужно.

yaml
Копировать код

---

👉 Теперь твои шаги:
1. Создаёшь ветку `lesson10`.  
2. Копируешь туда эти файлы.  
3. `git add . && git commit -m "Lesson 10 with Allure and docs"`  
4. `git push origin lesson10`  
5. Создаёшь Pull Request.  

---

Хочешь, я сразу сделаю тебе **версию с разметкой PEP8 (flake8-чистую)**, чтобы не пришлось потом исправлять ошибки стиля?






