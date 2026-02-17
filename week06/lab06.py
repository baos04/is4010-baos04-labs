"""
Lab 06: Object-Oriented Programming

This module demonstrates fundamental OOP concepts including classes, inheritance,
and method overriding using real-world examples of books and e-books.
"""


class Book:
    """A class to represent a physical book."""

    def __init__(self, title, author, year):
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Return a string representation of the book.

        Returns:
            str: A formatted string with book information
        """
        return f'"{self.title}" by {self.author} ({self.year})'

    def get_age(self):
        """
        Calculate the age of the book.

        Returns:
            int: The age of the book in years (2025 - publication year)
        """
        return 2025 - self.year


class EBook(Book):
    """A class to represent a digital e-book, inheriting from Book."""

    def __init__(self, title, author, year, file_size):
        """
        Initialize an EBook object.

        Args:
            title (str): The title of the e-book
            author (str): The author of the e-book
            year (int): The publication year of the e-book
            file_size (int): The size of the file in megabytes
        """
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """
        Return a string representation of the e-book.

        Returns:
            str: The parent's string representation plus file size information
        """
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"


if __name__ == "__main__":
    # Test the Book class
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(book)
    print(f"Age: {book.get_age()} years\n")

    # Test the EBook class
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    print(ebook)
    print(f"Age: {ebook.get_age()} years")
