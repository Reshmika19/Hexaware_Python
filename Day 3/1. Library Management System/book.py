class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True   

    def is_available(self):
        return self.__available

    def set_availability(self, status: bool):
        self.__available = status

    def display(self):
        status = "Available" if self.__available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}")
