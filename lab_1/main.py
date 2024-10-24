import argparse
import os
import re


def name_file() -> str:
    """
    Ввод названия файла
    :return: строка с именем файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('namefile', type=str, help='Имя файла')
    args = parser.parse_args()
    return args.namefile


def open_file(filename: str) -> str:
    """
    Считывание данных из файла
    :param filename: имя файла
    :return: данные в виде строки
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Указанный файл '{filename}' не найден.")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except OSError as err:
        raise RuntimeError(f"Ошибка при открытии файла '{filename}': {err}")
    

def split_forms(text: str) -> list[str]:
    """
    Разделение данных по анкетам
    :param text: данные в виде строки
    :return: список из каждой анкеты по отдельности
    """
    pattern=r'\d{1,2}\)'
    container=re.split(pattern, text)
    return container


def search_forms(container: list) -> list[str]:
    """
    Поиск анкет, в которых номер телефона имеет код города 927.
    :param container: список всех анкет по отдельности
    :return: список анкет, для которых выполняется условие задачи
    """
    return [i for i in container if re.search(r'\+7 927',i)]


def print_forms(container: list):
    """
    Вывод анкет
    :param container: список из каждой анкеты по отдельности
    """
    c=0
    for i in container:
        c += 1
        print(str(c) + ')')
        print(i.strip())


def main():
    """
    Основная функция
    """
    try:
        filename = name_file()
        text = open_file(filename)
        container = split_forms(text)
        container = search_forms(container)
        print_forms(container)
    except Exception as err:
        print(f"Произошла ошибка: {err}")


if __name__ == "__main__":
    main()
