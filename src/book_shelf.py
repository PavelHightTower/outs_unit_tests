from src.book import Book


class BookShelf:

    def __init__(self):
        self._books: list[Book] = []

    def add_book(self, book: Book):
        self._books.append(book)

    def take_book(self, book: Book) -> Book | None:
        found_book = None
        book_index = self._get_book_index(book)
        if book_index is not None:
            found_book = self._books.pop(book_index)
        return found_book

    def has_book(self, book: Book) -> bool:
        return book in self._books

    def remove_book(self, books: list[Book]):
        self._books[:] = [book for book in self._books if book not in books]

    def _get_book_index(self, book: Book):
        try:
            book_index = self._books.index(book)
        except ValueError:
            book_index = None

        return book_index

    def __str__(self):
        return ", ".join(str(book) for book in self._books)

