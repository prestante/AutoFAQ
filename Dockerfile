FROM python:3.12.8-slim

# Установка рабочего каталога
WORKDIR /app

# Копируем проект внутрь контейнера
COPY . /app

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Установка Playwright и необходимых браузеров
RUN playwright install --with-deps

# Команда для запуска тестов
ENTRYPOINT ["pytest", "--alluredir=allure-results"]