from datetime import datetime

from enums import BookStatus


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


def get_book_status() -> BookStatus:
    while True:
        status = input(f"Введите новый статус ({BookStatus.AVAILABLE.value}/{BookStatus.BORROWED.value}): ").lower()
        if status == BookStatus.AVAILABLE.value:
            return BookStatus.AVAILABLE
        elif status == BookStatus.BORROWED.value:
            return BookStatus.BORROWED
        print("Ошибка: Неверный статус. Попробуйте снова.")


def print_search_results(results):
    if results:
        for book in results:
            print(book)
    else:
        print("Книги не найдены.")
