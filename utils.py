from datetime import datetime


def get_int_input(prompt: str) -> int:
    while True:
        try:
            numb = int(input(prompt))
            if numb <= -1:
                raise ValueError
            return numb
        except ValueError:
            print("Ошибка: Пожалуйста, введите натуральное числовое значение.")


def get_year_input(prompt: str) -> int:
    while True:
        try:
            year = get_int_input(prompt)
            if year > datetime.today().year:
                raise ValueError
            return year
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректный год.")
