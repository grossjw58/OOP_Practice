'''
ou've been tasked with writing some code for your public library, complete the Library and Book classes listed below.

Book class
__init__(self, title, author)
Set .title and .author to the values of the parameters.

Library class
Add the following methods.
__init__(self, name)
Initialize a .name member variable to the value of the name parameter. Create a .books member initialized to an empty list.

add_book(self, book)
Add book, a Book instance, to the books instance variable by appending it to the end of the list.

remove_book(self, book)
If the book's title and author match a library book's title and author, the remove_book method should remove that library book from the list.

search_books(self, search_string)
For every book in the library check if the search_string is contained in the title or author field (case insensitive). Return a list of all books that match the search string, ordered in the same order as they were added to the library.
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book:Book):
        self.books.append(book)

    def remove_book(self, book:Book):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                self.books.remove(b)

    def search_books(self, search_string:str) -> list[Book]:
        search_string_lower: str = search_string.lower()
        selected_books: list[Book] = []
        for book in self.books:
            title_lower:str = book.title.lower()
            author_lower: str = book.author.lower()
            if search_string_lower in title_lower or search_string_lower in author_lower:
                selected_books.append(book)
        return(selected_books)

