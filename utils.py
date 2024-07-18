from datetime import datetime

from enums import BookStatus


def get_int_input(prompt: str) -> int:
    """
    Запрашивает у пользователя ввод натурального числа.

    Args:
        prompt (str): Приглашение к вводу, отображаемое пользователю.

    Returns:
        int: Введенное пользователем натуральное число.

    Raises:
        ValueError: Если введено отрицательное число или нечисловое значение.
    """
    while True:
        try:
            numb = int(input(prompt))
            if numb <= -1:
                raise ValueError
            return numb
        except ValueError:
            print("Ошибка: Пожалуйста, введите натуральное числовое значение.")


def get_year_input(prompt: str) -> int:
    """
    Запрашивает у пользователя ввод года, не превышающего текущий.

    Args:
        prompt (str): Приглашение к вводу, отображаемое пользователю.

    Returns:
        int: Введенный пользователем год.

    Raises:
        ValueError: Если введен год, превышающий текущий, или нечисловое значение.
    """
    while True:
        try:
            year = get_int_input(prompt)
            if year > datetime.today().year:
                raise ValueError
            return year
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректный год.")


def get_book_status() -> BookStatus:
    """
    Запрашивает у пользователя ввод статуса книги.

    Returns:
        BookStatus: Введенный пользователем статус книги (AVAILABLE или BORROWED).

    Raises:
        ValueError: Если введен некорректный статус.
    """
    while True:
        status = input(f"Введите новый статус ({BookStatus.AVAILABLE.value}/{BookStatus.BORROWED.value}): ").lower()
        if status == BookStatus.AVAILABLE.value:
            return BookStatus.AVAILABLE
        elif status == BookStatus.BORROWED.value:
            return BookStatus.BORROWED
        print("Ошибка: Неверный статус. Попробуйте снова.")


def print_search_results(results):
    """
    Выводит результаты поиска книг.

    Args:
        results (List[Book]): Список найденных книг.

    Note:
        Если список пуст, выводит сообщение "Книги не найдены."
    """
    if results:
        for book in results:
            print(book)
    else:
        print("Книги не найдены.")
