from library.book import Book
from library.lib import Library

if __name__ == "__main__":

    # create instance
    my_library = Library()

    # add book
    my_library.add_book(Book(title="1984", author="George Orwell", year=1949, genre="Dystopian", summary="A dystopian novel set in a totalitarian society ruled by Big Brother."))
    
    # add books
    my_library.add_books([
        Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960, genre="Fiction", summary="A novel about the serious issues of rape and racial inequality."),
        Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925, genre="Fiction", summary="A story about the American dream and the disillusionment that comes with it.")
    ])
    print("------------------------")

    # search books
    my_library.search_books("1984")
    print("------------------------")

    # remove book
    my_library.remove_books_by_query("1984")
    print("------------------------")

    # get all books
    my_library.get_all_books(verbose=1)
    print("------------------------")

    # get total books
    my_library.get_total_books(verbose=1)
    print("------------------------")

    # clear library
    my_library.clear_library()

    # get total books
    my_library.get_total_books(verbose=1)
    print("------------------------")
