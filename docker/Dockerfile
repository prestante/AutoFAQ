FROM --platform=arm64 python:3.12.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Установка Playwright и браузеров
RUN playwright install --with-deps

# Make port 80 available to the world outside this container
EXPOSE 80

# Запуск тестов
ENTRYPOINT ["pytest"]