from src.book_shelf import BookShelf
from src.book import Book
import unittest


class TestBookShelf(unittest.TestCase):

    def setUp(self):
        self.book_shelf = BookShelf()
        self.book_one = Book("Harry Potter and goblet of fire", "J. K. Rowling", "fantasy")
        self.book_two = Book("Crime and Punishment", "F. M. Dostoevsky", "novel")

    def test_add_book(self):
        self.book_shelf.add_book(self.book_one)
        self.assertTrue(self.book_shelf.has_book(self.book_one))

    def test_take_book(self):
        self.book_shelf.add_book(self.book_one)
        self.book_shelf.take_book(self.book_one)
        self.assertFalse(self.book_shelf.has_book(self.book_one))

    def test_remove_books(self):
        self.book_shelf.add_book(self.book_one)
        self.book_shelf.add_book(self.book_two)
        self.book_shelf.remove_book(books=[self.book_one, self.book_two])
        self.assertFalse(self.book_shelf.has_book(self.book_one))
        self.assertFalse(self.book_shelf.has_book(self.book_two))

    def test_check_book(self):
        self.book_shelf.add_book(self.book_one)
        self.assertTrue(self.book_shelf.has_book(self.book_one))
        self.assertFalse(self.book_shelf.has_book(self.book_two))

