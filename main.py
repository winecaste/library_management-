from typing import Callable

from enums import MenuChoice
from library import Library
from utils import get_int_input, get_book_status, print_search_results, get_year_input


def main():
    """
    Главная функция программы.

    Инициализирует библиотеку, создает меню действий и
    запускает основной цикл взаимодействия с пользователем.
    """
    library = Library('data.json')

    menu_actions: dict[MenuChoice, Callable[[], None]] = {
        MenuChoice.ADD_BOOK: lambda: library.add_book(
            input("Введите название книги: "),
            input("Введите автора книги: "),
            get_year_input("Введите год издания книги: ")
        ),
        MenuChoice.REMOVE_BOOK: lambda: library.remove_book(
            get_int_input("Введите ID книги для удаления: ")
        ),
        MenuChoice.SEARCH_BOOK: lambda: print_search_results(
            library.search_books(input("Введите ключевое слово для поиска: "))
        ),
        MenuChoice.LIST_BOOKS: library.list_books,
        MenuChoice.UPDATE_STATUS: lambda: library.update_book_status(
            get_int_input("Введите ID книги для обновления статуса: "),
            get_book_status()
        ),
        MenuChoice.EXIT: lambda: None
    }

    while True:
        print("\nСистема управления библиотекой")
        for choice in MenuChoice:
            print(f"{choice.value}. {choice.name.replace('_', ' ').capitalize()}")

        choice = input("Выберите действие: ")

        try:
            action = menu_actions[MenuChoice(choice)]
            if choice == MenuChoice.EXIT.value:
                break
            action()
        except KeyError:
            print("Неверный выбор. Попробуйте снова.")




if __name__ == "__main__":
    main()
