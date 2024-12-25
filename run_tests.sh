#!/bin/bash

# 1. Удаляем старые отчеты (опционально)
rm -rf ./allure-reports ./allure-results

# 2. Запускаем контейнер и ждем завершения
docker-compose up --build

# 3. Открываем отчет в браузере
open http://localhost:5050

# 4. Останавливаем контейнер
docker-compose down