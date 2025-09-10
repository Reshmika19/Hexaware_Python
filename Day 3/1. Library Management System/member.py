from book import Book

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []  

    def borrow_book(self, book: Book):
        if len(self.__borrowed_books) >= 3:
            print(f"{self.name} cannot borrow more than 3 books.")
            return

        if book.is_available():
            self.__borrowed_books.append(book)
            book.set_availability(False)
            print(f"Member {self.name} borrowed '{book.title}'.")
        else:
            print(f"Book '{book.title}' is currently not available.")

    def return_book(self, book: Book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.set_availability(True)
            print(f"Member {self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

    def display_borrowed_books(self):
        print(f"{self.name}'s Borrowed Books:")
        if not self.__borrowed_books:
            print("No books borrowed.")
        else:
            for b in self.__borrowed_books:
                print(f"- {b.title}")
