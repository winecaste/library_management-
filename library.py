from book import Book


class Library:
    def __init__(self):
        self.books = []

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
