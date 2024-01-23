import unittest
from src.book import Book


class TestBook(unittest.TestCase):

    def test_book_creation(self):
        book = Book("Harry Potter and goblet of fire", "J. K. Rowling", "fantasy")
        self.assertEqual(book.title, "Harry Potter and goblet of fire")
        self.assertEqual(book.author, "J. K. Rowling")
        self.assertEqual(book.genre, "fantasy")

    def test_book_srt(self):
        book = Book("Harry Potter and goblet of fire", "J. K. Rowling", "fantasy")
        expected_str = 'Harry Potter and goblet of fire by J. K. Rowling. Genre: fantasy'
        self.assertEqual(str(book), expected_str)
