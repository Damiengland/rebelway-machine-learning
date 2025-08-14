from library.book import Book
from library.lib import Library

def test_add_book():
    lib = Library()
    book = Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother.")
    lib.add_book(book)
    assert book.id in lib.books["books"]

def test_get_all_books():
    lib = Library()
    book1 = Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother.")
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, genre="Fiction", summary="A novel about the serious issues of rape and racial inequality.")
    lib.add_books([book1, book2])
    all_books = lib.get_all_books()
    compare_titles = [book1.title, book2.title]
    results = [book_data['title'] for book_id, book_data in all_books["books"].items()]
    assert results == compare_titles

def test_search_books():
    lib = Library()
    book = Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother.")
    lib.add_book(book)
    results = lib.search_books("1984")
    assert len(results) == 1
    assert results[0].id == book.id

def test_remove_books_by_query():
    lib = Library()
    book1 = Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother.")
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, genre="Fiction", summary="A novel about the serious issues of rape and racial inequality.")
    lib.add_books([book1, book2])
    lib.remove_books_by_query("1984")
    all_books = lib.get_all_books()
    assert len(all_books["books"]) == 1
    assert book2.id in all_books["books"]

def test_clear_library():
    lib = Library()
    book1 = Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother.")
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, genre="Fiction", summary="A novel about the serious issues of rape and racial inequality.")
    lib.add_books([book1, book2])
    lib.clear_library()
    all_books = lib.get_all_books()
    assert len(all_books["books"]) == 0

def test_get_total_books():
    lib = Library()
    book1 = Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother.")
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, genre="Fiction", summary="A novel about the serious issues of rape and racial inequality.")
    lib.add_books([book1, book2])
    total_books = lib.get_total_books()
    assert total_books == 2