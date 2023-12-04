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

    def display_book_list(self):
        return Book.bookList

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

    def search_books_by_ISBN(self, isbn):
        results = [book for book in Book.bookList if str(book.get_ISBN()) == str(isbn)]
        return results

    def search_books_by_author(self, author):
        results = [book for book in Book.bookList if book.get_author().lower() == author.lower()]
        return results

    def search_books_by_title(self, title):
        results = [book for book in Book.bookList if book.get_title().lower() == title.lower()]
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
        return f"{self.ISBN},{self.author},{self.title},{self.publisher},{self.genre},{self.year_published},{self.date_purchased},{self.status}"


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

def validate_ISBN(ISBN):
        return ISBN == "" or (ISBN.isdigit() and int(ISBN) >= 0 and len(ISBN) == 13 )

def validate_year(year):
        return year == "" or (year.isdigit() and len(year) == 4)


# Read books from the file when the program starts
read_books_from_file("books_StudentID.txt")

choice = 1
book = Book(0, "", "", "", "", 0, "", "")

while 1 <= choice <= 6:
    print("\n\n1. Add new book\n2. Remove book by ISBN, author, or title\n3. Update book by ISBN, author, or title\n4. Display all the books that are currently in the system\n5. Search for book(s) by ISBN, author, or title\n6. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if choice == 1:
        ISBN = input("Enter ISBN: ")
        while not validate_ISBN(ISBN):
            print("Invalid input. ISBN must consist of 13 positive integer number.")
            ISBN = input("Enter ISBN: ")

        author = input("Enter author: ")
        title = input("Enter title: ")
        publisher = input("Enter publisher: ")
        genre = input("Enter genre: ")
        year_published = input("Enter year published: ")
        while not (validate_year(year_published) and len(year_published) == 4):
            print("Invalid input. Year must be a 4-digit integer.")
            year_published = input("Enter year published: ")

        date_purchased = input("Enter date purchased: ")
        status = input("Enter status: ")
        new_book = Book(ISBN, author, title, publisher, genre, year_published, date_purchased, status)
        new_book.add_new_book()

        print(f"\nAdd {'successful' if new_book in Book.bookList else 'failed'}. Book: {new_book}")

    elif choice == 2:
        search_choice = int(input("Search by:\n1. ISBN\n2. Author\n3. Title\nEnter your choice: "))
        if search_choice == 1:
            ISBN = input("Enter ISBN: ")
            while not validate_ISBN(ISBN):
                print("Invalid input. ISBN must consist of 13 positive integer number.")
                ISBN = input("Enter ISBN: ")
            search_results = book.search_books_by_ISBN(ISBN)
        elif search_choice == 2:
            author = input("Enter author: ")
            search_results = book.search_books_by_author(author)
        elif search_choice == 3:
            title = input("Enter title: ")
            search_results = book.search_books_by_title(title)
        else:
            print("Invalid choice. Please enter a valid option.")
            continue

        if not search_results:
            print("\nNo matching books found.")
        else:
            print("\nMatching Books:")
            for result in search_results:
                print(result)
         # Prompt for confirmation to delete
            delete_confirmation = input("Do you want to delete the matched book(s)? (yes/no): ").lower()
            if delete_confirmation == "yes":
                for result in search_results:
                    Book.bookList.remove(result)
                print("Delete successful.")
            else :
                print("Delete canceled.")        

    elif choice == 3 :
        search_choice = int(input("Search by:\n1. ISBN\n2. Author\n3. Title\nEnter your choice: "))
        if search_choice == 1:
            ISBN = input("Enter ISBN: ")
            while not validate_ISBN(ISBN):
                print("Invalid input. ISBN must consist of 13 positive integer number.")
                ISBN = input("Enter ISBN: ")
            search_results = book.search_books_by_ISBN(ISBN)
        elif search_choice == 2:
            author = input("Enter author: ")
            search_results = book.search_books_by_author(author)
        elif search_choice == 3:
            title = input("Enter title: ")
            search_results = book.search_books_by_title(title)
        else:
            print("Invalid choice. Please enter a valid option.")
            continue
        
        if not search_results:
            print("\nNo matching books found.")
        else:
            print("\nMatching Books:")
            for result in search_results:
                print(result)
    
            # Prompt for updated information
            author = input("Enter new author (leave blank to keep current): ")
            title = input("Enter new title (leave 4 to keep current): ")
            publisher = input("Enter new publisher (leave blank to keep current): ")
            genre = input("Enter new genre (leave blank to keep current): ")
            year_published = input("Enter new year published (leave blank to keep current): ")
            date_purchased = input("Enter new date purchased (leave blank to keep current): ")
            status = input("Enter new status (leave blank to keep current): ")
            
            # Update only the fields that are not left blank
            if author:
                result.set_author(author)
            if title:
                result.set_title(title)
            if publisher:
                result.set_publisher(publisher)
            if genre:
                result.set_genre(genre)
            if year_published:
                result.set_year_published(year_published)
            if date_purchased:
                result.set_date_purchased(date_purchased)
            if status:
                result.set_status(status)
                
            print("Update successful.")


    elif choice == 4:
        print("\n")
        for bk in book.display_book_list():
            print(bk)


    elif choice == 5:
        search_choice = int(input("Search by:\n1. ISBN\n2. Author\n3. Title\nEnter your choice: "))
        if search_choice == 1:
            ISBN = input("Enter ISBN: ")
            while not validate_ISBN(ISBN):
                print("Invalid input. ISBN must consist of 13 positive integer number.")
                ISBN = input("Enter ISBN: ")
            search_results = book.search_books_by_ISBN(ISBN)
        elif search_choice == 2:
            author = input("Enter author: ")
            search_results = book.search_books_by_author(author)
        elif search_choice == 3:
            title = input("Enter title: ")
            search_results = book.search_books_by_title(title)
        else:
            print("Invalid choice. Please enter a valid option.")
            continue
        
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
