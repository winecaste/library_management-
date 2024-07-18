import json
from typing import Optional

from book import Book
from enums import BookStatus



class Library:
    """
    Класс, представляющий библиотеку.

    Attributes:
        data_file (str): Путь к файлу для хранения данных о книгах.
        books (List[Book]): Список книг в библиотеке.
    """
    def __init__(self, data_file: str):
        """
        Инициализирует библиотеку.

        Args:
            data_file (str): Путь к файлу для хранения данных о книгах.
        """
        self.data_file = data_file
        self.books: list[Book] = self.load_books()

    def load_books(self) -> list[Book]:
        """
        Загружает книги из файла.

        Returns:
            List[Book]: Список загруженных книг.
        """
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except FileNotFoundError:
            return []

    def save_books(self) -> None:
        """Сохраняет книги в файл."""
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в библиотеку.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        book_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {book_id}")

    def remove_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по ID.

        Args:
            book_id (int): ID книги для удаления.
        """
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        """
        Находит книгу по ID.

        Args:
            book_id (int): ID книги для поиска.

        Returns:
            Optional[Book]: Найденная книга или None, если книга не найдена.
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, keyword: str) -> list[Book]:
        """
        Ищет книги по ключевому слову.

        Args:
            keyword (str): Ключевое слово для поиска.

        Returns:
            List[Book]: Список найденных книг.
        """
        return [book for book in self.books if keyword.lower() in book.title.lower() or
                keyword.lower() in book.author.lower() or keyword.lower() == str(book.year)]

    def list_books(self) -> None:
        """Выводит список всех книг в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(book)

    def update_book_status(self, book_id: int, new_status: BookStatus) -> None:
        """
        Обновляет статус книги.

        Args:
            book_id (int): ID книги для обновления.
            new_status (Union[str, BookStatus]): Новый статус книги.
        """
        book = self.find_book_by_id(book_id)
        if book:
            book.status = new_status.value
            self.save_books()
            print(f"Статус книги с ID {book_id} обновлен на '{new_status.value}'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

