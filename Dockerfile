# Используем официальный образ Python как базу
FROM python:3.10-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию
WORKDIR /code

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копируем весь остальной код проекта в рабочую директорию
COPY . /code/
