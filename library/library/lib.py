from dataclasses import dataclass, field
from library.book import Book
from library.rand_num_utils import RandomUtils
from typing import Dict, List

@dataclass
class Library:
    books: Dict[str, Dict] = field(default_factory=lambda: {"books": {}})
    isEmpty: bool = field(default=True)
    id: str = field(default_factory=lambda: RandomUtils.generate_random_id())

    def get_all_books(self, verbose=0) -> dict:
        """
        Returns all books in the library.

        Args:
            verbose (int, optional): If set to 1, will print the books. Defaults to 0.

        Returns:
            dict: A dictionary of all books in the library.
        """ 

        if len(self.books) > 0:
            self.isEmpty = False
        try:   
            if verbose == 1:
                print(self.books)
                return self.books
            else:
                return self.books
        except:
            raise ValueError("The value for the verbose has to be 0 or 1")
            
 
    def add_book(self, book: Book) -> Book:
        """
        Adds a book to the library.

        Returns:
            Book: The added book.
        """
        data = self.get_all_books()

        data["books"][book.id] = {
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "genre": book.genre,
            "summary": book.summary
        }

        self.isEmpty = False
        
        return book
    
    def add_books(self, books: List[Book]) -> list[Book]:
        """
        Adds multiple books to the library.

        Returns: 
            list[Book]: The list of added books.
        """
        added_books = []
        for book in books:
            added_books.append(self.add_book(book))
        return added_books
    
    def search_books(self, query) -> List[Book]:
        """
        Searches for books in the library that match the given query.

        Returns:
            List[Book]: A list of books that match the query.
        """
        results = []
        data = self.get_all_books(verbose=0)
        for book_id, book_data in data['books'].items():
            book = Book(
                title=book_data["title"],
                author=book_data["author"],
                year=book_data["year"],
                genre=book_data["genre"],
                summary=book_data.get("summary", ""),
                id=book_id
            )
            if query.lower() in book.search_string.lower():
                results.append(book)

        if len(results) == 0:
            print("No books found matching the query.")
        else:
            print(f"Found {len(results)} matching books:")

        return results

    def remove_books_by_query(self, query: str):
        """
        Remove books from the library by the given query.
        """
        books_to_remove = self.search_books(query)

        for book in books_to_remove:
            del self.books["books"][book.id]
            print(f"Removed book: {book.title} by {book.author}")
        if len(self.books) == 0:
            self.isEmpty = True

    def clear_library(self):
        """
        Clears the library by removing all books.
        """
        self.books = {"books": {}}
        self.isEmpty = True

    def get_total_books(self, verbose=0) -> int:
        """
        Returns the total number of books in the library.

        Args:
            verbose (int): if 1, prints the total number of books.

        Returns:
            int: The total number of books in the library.
        """
        total_books = self.get_all_books()
        if verbose == 1:
            print(f"Total books in library: {len(total_books.get('books', {}))}")
        return len(total_books.get('books', {}))

lib = Library()
lib.add_book(Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother."))
lib.add_books([
    Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, genre="Fiction", summary="A novel about the serious issues of rape and racial inequality."),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925, genre="Fiction", summary="A story about the American dream and the disillusionment that comes with it.")
]) 
