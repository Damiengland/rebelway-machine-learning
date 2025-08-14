from library.book import Book

def test_book_get_summary():
    book = Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother.")
    assert book.get_summary == "A dystopian novel set in a totalitarian society ruled by Big Brother."
