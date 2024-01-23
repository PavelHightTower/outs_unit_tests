from typing import Dict
from src.book_shelf import BookShelf
from src.book import Book


class Library:

    def __init__(self):
        self.book_shelves: Dict[str, BookShelf] = {}

    def add_book_to_library(self, book: Book):
        if book.genre not in self.book_shelves:
            self.book_shelves[book.genre] = BookShelf()
        self.book_shelves[book.genre].add_book(book)

    def get_book_from_library(self, book: Book) -> Book:
        if self.check_book_in_library(book):
            book = self.book_shelves[book.genre].take_book(book)
            return book
        else:
            print("Sorry, No such book in our library")

    def get_books_form_library(self, books: list[Book]) -> list[Book]:
        found_books = []

        for book in books:
            if self.check_book_in_library(book):
                book = self.book_shelves[book.genre].take_book(book)
                found_books.append(book)

        return found_books

    def display_books(self):
        print("We have following books:")
        for genre, books in self.book_shelves.items():
            print(f"Genre: {genre}. Books: {books}")

    def check_book_in_library(self, book: Book) -> bool:
        return book.genre in self.book_shelves and self.book_shelves[book.genre].has_book(book)
