from typing import List


class Book:

    def __init__(self, title: str, author: str):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(author, str):
            raise TypeError("author must be a string")

        self.title: str = title
        self.author: str = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):

    def __init__(self, title: str, author: str, file_size: int):
        # initialize base attributes
        super().__init__(title, author)

        if not isinstance(file_size, int):
            raise TypeError("file_size must be an int")
        if file_size < 0:
            raise ValueError("file_size must be non-negative")

        self.file_size: int = file_size

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):

    def __init__(self, title: str, author: str, page_count: int):
        # initialize base attributes
        super().__init__(title, author)

        if not isinstance(page_count, int):
            raise TypeError("page_count must be an int")
        if page_count < 0:
            raise ValueError("page_count must be non-negative")

        self.page_count: int = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Only Book instances (or subclasses) can be added to the library.")
        self.books.append(book)

    def list_books(self) -> None:
        for book in self.books:
            print(str(book))

__all__ = ["Book", "EBook", "PrintBook", "Library"]
