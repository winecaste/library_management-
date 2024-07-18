import json

from book import Book


class Library:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.books = self.load_books()

    def add_book(self, title: str, author: str, year: int) -> None:
        book_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        print(f"Книга '{title}' добавлена с ID {book_id}")

    def list_books(self) -> None:
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(book)

    def remove_book(self, book_id: int) -> None:
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print(f"Книга с ID {book_id} удалена.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, keyword: str) -> list[Book]:
        return [book for book in self.books if keyword.lower() in book.title.lower() or
                keyword.lower() in book.author.lower() or keyword == str(book.year)]

    def update_book_status(self, book_id: int, new_status: str) -> None:
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                print(f"Статус книги с ID {book_id} обновлен на '{new_status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")


    def load_books(self) -> list[Book]:
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except FileNotFoundError:
            return []

    def save_books(self) -> None:
        with open(self.data_file, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)
