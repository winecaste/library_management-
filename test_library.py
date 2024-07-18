import unittest
from unittest.mock import patch, mock_open

from book import Book
from enums import BookStatus
from library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library('test_data.json')

    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    def test_load_books_empty(self, mock_file):
        books = self.library.load_books()
        self.assertEqual(len(books), 0)

    @patch('builtins.open', new_callable=mock_open,
           read_data='[{"id": 1, "title": "Test Book", "author": "Test Author", "year": 2021, "status": "в наличии"}]')
    def test_load_books_with_data(self, mock_file):
        books = self.library.load_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")

    @patch('library.Library.save_books')
    def test_add_book(self, mock_save):
        self.library.add_book("Python – к вершинам мастерства", "Лусиану Рамальо", 2022)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Python – к вершинам мастерства")

    @patch('library.Library.save_books')
    def test_remove_book(self, mock_save):
        self.library.books = [Book(1, "Высоконагруженные приложения", "Клеппман М.", 2018)]
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_find_book_by_id(self):
        self.library.books = [Book(1, "Test Book", "Test Author", 2021)]
        book = self.library.find_book_by_id(1)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Test Book")

    def test_search_books(self):
        self.library.books = [
            Book(1, "Python – к вершинам мастерства", "Лусиану Рамальо", 2021),
            Book(2, "Высоконагруженные приложения", "Клеппман М.", 2022)
        ]
        results = self.library.search_books("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Python – к вершинам мастерства")

    @patch('library.Library.save_books')
    def test_update_book_status(self, mock_save):
        self.library.books = [Book(1, "Test Book", "Test Author", 2021)]
        self.library.update_book_status(1, BookStatus.BORROWED)
        self.assertEqual(self.library.books[0].status, BookStatus.BORROWED.value)


if __name__ == '__main__':
    unittest.main()


