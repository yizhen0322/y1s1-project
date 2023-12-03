from typing import List

class Book:
    bookList = []

    def __init__(self, ISBN, author, title, publisher, genre, year_published, date_purchased, status):
        self.ISBN, self.author, self.title, self.publisher, self.genre, self.year_published, self.date_purchased, self.status = (
            ISBN,
            author,
            title,
            publisher,
            genre,
            year_published,
            date_purchased,
            status,
        )

    def add_new_book(self):
        Book.bookList.append(self)

    def get_book_list(self):
        return Book.bookList

    def get_book_by_id(self, identifier):
        for book in Book.bookList:
            if book.get_ISBN() == identifier or book.get_author().lower() == identifier.lower() or book.get_title().lower() == identifier.lower():
                return book
        return False

    def update_book_by_id(self, identifier, author, title, publisher, genre, year_published, date_purchased, status):
        for book in Book.bookList:
            if (
                book.get_ISBN() == identifier
                or book.get_author().lower() == identifier.lower()
                or book.get_title().lower() == identifier.lower()
            ):
                book.ISBN, book.author, book.title, book.publisher, book.genre, book.year_published, book.date_purchased, book.status = (
                    identifier,
                    author,
                    title,
                    publisher,
                    genre,
                    year_published,
                    date_purchased,
                    status,
                )
                return True
        return False

    def remove_book_by_id(self, identifier):
        for book in Book.bookList:
            if (
                book.get_ISBN() == identifier
                or book.get_author().lower() == identifier.lower()
                or book.get_title().lower() == identifier.lower()
            ):
                Book.bookList.remove(book)
                return True
        return False

    def search_books(self, isbn="", author="", title=""):
        results = []
        for book in Book.bookList:
            if (
                (not isbn or book.get_ISBN() == isbn)
                and (not author or book.get_author().lower() == author.lower())
                and (not title or book.get_title().lower() == title.lower())
            ):
                results.append(book)
        return results

    def set_ISBN(self, ISBN):
        self.ISBN = ISBN

    def get_ISBN(self):
        return self.ISBN

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_year_published(self, year_published):
        self.year_published = year_published

    def get_year_published(self):
        return self.year_published

    def set_date_purchased(self, date_purchased):
        self.date_purchased = date_purchased

    def get_date_purchased(self):
        return self.date_purchased

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def __str__(self):
        return f"{self.ISBN} {self.title} {self.author} {self.publisher} {self.genre} {self.year_published} {self.date_purchased} {self.status}"


def read_books_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 8:
                    ISBN, author, title, publisher, genre, year_published, date_purchased, status = data
                    new_book = Book(int(ISBN), author, title, publisher, genre, int(year_published), date_purchased, status)
                    new_book.add_new_book()
    except FileNotFoundError:
        print(f"The file {filename} does not exist. Starting with an empty book list.")

def write_books_to_file(filename):
    with open(filename, 'w') as file:
        for book in Book.bookList:
            file.write(f"{book.get_ISBN()},{book.get_author()},{book.get_title()},{book.get_publisher()},{book.get_genre()},{book.get_year_published()},{book.get_date_purchased()},{book.get_status()}\n")


# Read books from the file when the program starts
read_books_from_file("books_StudentID.txt")

choice = 1
book = Book(0, "", "", "", "", 0, "", "")

while choice >= 1 and choice <= 6:
    print("\n\n1. Add new book\n2. Remove book by ISBN, author, or title\n3. Update book by ISBN, author, or title\n4. Get all books list\n5. Search for book(s) by ISBN, author, or title\n6. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue  # This will go back to the beginning of the loop

    if choice == 1:
        ISBN = int(input("Enter ISBN: "))
        author = input("Enter author: ")
        title = input("Enter title: ")
        publisher = input("Enter publisher: ")
        genre = input("Enter genre: ")
        year_published = int(input("Enter year published: "))
        date_purchased = input("Enter date purchased: ")
        status = input("Enter status: ")
        new_book = Book(ISBN, author, title, publisher, genre, year_published, date_purchased, status)
        new_book.add_new_book()

    elif choice == 2:
        identifier = input("Enter ISBN, author, or title: ")
        bk = book.remove_book_by_id(identifier)
        if bk == False:
            print(f"\nSorry, delete failed. Book not found: {identifier}")
        else:
            print(f"Delete successful. Identifier: {identifier}")

    elif choice == 3:
        identifier = input("Enter ISBN, author, or title: ")
        author = input("Enter author: ")
        title = input("Enter title: ")
        publisher = input("Enter publisher: ")
        genre = input("Enter genre: ")
        year_published = int(input("Enter year published: "))
        date_purchased = input("Enter date purchased: ")
        status = input("Enter status: ")
        bk = book.update_book_by_id(identifier, author, title, publisher, genre, year_published, date_purchased, status)
        if bk == False:
            print(f"\nSorry, update failed. Book not found: {identifier}")
        else:
            print("Update successful.")

    elif choice == 4:
        print("\n")
        for bk in book.get_book_list():
            print(bk)

    elif choice == 5:
        ISBN = input("Enter ISBN, author, or title: ")
        author = input("Enter author (leave blank if not searching by author): ")
        title = input("Enter title (leave blank if not searching by title): ")
        search_results = book.search_books(ISBN, author, title)
        if not search_results:
            print("\nNo matching books found.")
        else:
            print("\nMatching Books:")
            for result in search_results:
                print(result)

    elif choice == 6:
        print("Exiting the program.")
        # Write books back to the file when the program exits
        write_books_to_file("books_StudentID.txt")
        break

