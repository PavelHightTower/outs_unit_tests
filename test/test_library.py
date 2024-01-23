from src.library import Library
from src.book import Book
import unittest
from unittest.mock import Mock, patch


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book = Book("Harry Potter and goblet of fire", "J. K. Rowling", "fantasy")
        # self.library = Library()
        # self.library.check_book_in_library = Mock(return_value=True)

    # def test_has_book(self):
    #     self.assertTrue(self.library.check_book_in_library(self.book))

    def test_has_book_2(self):
        with patch.object(Library, 'check_book_in_library', return_value=False):
            library = Library()
            self.assertTrue(library.check_book_in_library(self.book))

