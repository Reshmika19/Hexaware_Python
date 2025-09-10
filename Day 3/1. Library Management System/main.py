'''
1. Library Management System

Problem Statement:
You are tasked with designing a Library Management System for a small community library. The
system should manage books, library members, and borrowing/returning of books.
'''

from book import Book
from member import Member

book1 = Book("Python Basics", "Tom", "ISBN001")
book2 = Book("Learning OOP", "Virat", "ISBN002")
book3 = Book("Data Science 101", "Abde", "ISBN003")


print("\nLibrary Books:")
for b in [book1, book2, book3]:
    b.display()

print()

resh = Member("Resh", "M001")
nila = Member("Nilla", "M002")

resh.borrow_book(book1) 
resh.borrow_book(book2)   
resh.borrow_book(book3)   
resh.borrow_book(Book("Extra Book", "AuthorX", "ISBN004")) 
print()
nila.borrow_book(book1) 

resh.return_book(book2)
nila.borrow_book(book2)  # Now available for nilla
print()
resh.display_borrowed_books()
print()
nila.display_borrowed_books()
