import re
import requests
from typing import List

from bs4 import BeautifulSoup


def extract_time(expression: str) -> List[str]:
    return re.findall(r"\b(?:[0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\b", expression)

def get_time_from_user() -> str:
    return input().strip()

def get_time_from_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл с таким названием не найден")
        return ""

def get_time_from_url(url: str) -> str:
    try:
        response = requests.get(url, timeout = 10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при запросе: {error}")
        return ""

def main():
    print("Выберите источник информации:")
    print("1) Ввод с клавиатуры")
    print("2) Веб-страница по URL")
    print("3) Загрузить файл")
    choice = input().strip()

    text = ""
    if choice == '1':
        print("Введите строку")
        text = get_time_from_user()
    elif choice == '2':
        print("Введите URL веб-страницы")
        url = input().strip()
        text = get_time_from_url(url)
    elif choice == '3':
        print("Введите путь до файла")
        file_path = input().strip()
        text = get_time_from_file(file_path)
    else:
        print("Введите цифру от 1 до 3")
        return

    if text:
        result = extract_time(text)
        if result:
            print("Найденное синтаксически корректное время:", result)
        else:
            print("Cинтаксически корректное время в формате ЧЧ:ММ:СС не найдено")
    else:
        print("Не удалось получить данные")

if __name__ == "__main__":
    main()