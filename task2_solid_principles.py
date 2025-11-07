from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Abstract Library
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book:Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


# Abstract Library according to Interface Segregation Principle
class AddBookInterface(ABC):
    @abstractmethod
    def add_book(self, book:Book):
        pass

class RemoveBookInterface(ABC):
    @abstractmethod
    def remove_book(self, title: str):
        pass

class ShowBookInterface(ABC):
    @abstractmethod
    def show_books(self):
        pass 

class ReadBookInterface(ABC):
    @abstractmethod
    def read_book(self, title):
        pass

# Concrete Library. Close for changes, open for extension (Implements a library)
# Library
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

class OnlineLibrary(ShowBookInterface, ReadBookInterface):
    def __init__(self):
        self.books = []

    def show_books(self):
        for book in self.books:
            print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

    def read_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f'Reading the book "{title}"')

# Extension of Library (Extends behavior)
class LibraryManagement():
    def __init__(self, library: Library):
        self.library = library

    def add_book(self):
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        year = input("Enter book year: ").strip()
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self):
        title = input("Enter book title to remove: ").strip()
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManagement(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()
        
        match command:
            case "add":
                manager.add_book()
            case "remove":
                manager.remove_book()
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

