from typing import List

class Book:
    bookList = []  # Class variable to store a list of all books

    def __init__(self, ISBN, author, title, publisher, genre, year_published, date_purchased, status):
        # Constructor to initialize a new Book object with provided attributes
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
        # Method to add a new book to the bookList
        Book.bookList.append(self)

    def display_book_list(self):
        # Method to return the list of all books
        return Book.bookList

    def search_books_by_ISBN(self, isbn):
        # Method to search books by ISBN and return a list of matching books
        results = [book for book in Book.bookList if str(book.get_ISBN()) == str(isbn)]
        return results
    
    def search_books_by_author(self, author):
        # Method to search books by author and return a list of matching books
        results = [book for book in Book.bookList if book.get_author().lower() == author.lower()]
        return results

    def search_books_by_title(self, title):
        # Method to search books by title and return a list of matching books
        results = [book for book in Book.bookList if book.get_title().lower() == title.lower()]
        return results
    
    # Getter and setter methods for ISBN
    def set_ISBN(self, ISBN):
        self.ISBN = ISBN

    def get_ISBN(self):
        return self.ISBN

    # Getter and setter methods for author
    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    # Getter and setter methods for title
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    # Getter and setter methods for publisher
    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    # Getter and setter methods for genre
    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    # Getter and setter methods for year_published
    def set_year_published(self, year_published):
        self.year_published = year_published

    def get_year_published(self):
        return self.year_published

    # Getter and setter methods for date_purchased
    def set_date_purchased(self, date_purchased):
        self.date_purchased = date_purchased

    def get_date_purchased(self):
        return self.date_purchased

    # Getter and setter methods for status
    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    # Method to provide a string representation of the book
    def __str__(self):
        return f"{self.ISBN},{self.author},{self.title},{self.publisher},{self.genre},{self.year_published},{self.date_purchased},{self.status}"

    # Getter and setter methods for various book attributes


# Function to read books from a file and populate the bookList
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

# Function to write books to a file
def write_books_to_file(filename):
    with open(filename, 'w') as file:
        for book in Book.bookList:
            file.write(f"{book.get_ISBN()},{book.get_author()},{book.get_title()},{book.get_publisher()},{book.get_genre()},{book.get_year_published()},{book.get_date_purchased()},{book.get_status()}\n")

# Functions to validate ISBN and year inputs
def validate_ISBN(ISBN):
        return ISBN == "" or (ISBN.isdigit() and int(ISBN) >= 0 and len(ISBN) == 13 )

def validate_year(year):
        return year == "" or (year.isdigit() and len(year) == 4)


# Main part of the program
# Read books from the file when the program starts
read_books_from_file("books_StudentID.txt")

# Initialize choice and a default book
choice = 1
book = Book(0, "", "", "", "", 0, "", "")

# Main program loop
while True:
    # Display menu options
    print("\n\n1. Add new book\n2. Remove book by ISBN, author, or title\n3. Update book by ISBN, author, or title\n4. Display all the books that are currently in the system\n5. Search for book(s) by ISBN, author, or title\n6. Exit\n")

    # Get user choice and handle input validation
    try:
        choice = int(input("Enter your choice: "))
        if not 1 <= choice <= 6:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    # Process user choice
    if choice == 1:
        # Option 1: Add new book
        ISBN = input("Enter ISBN(must input): ")
        while not (validate_ISBN(ISBN) and len(ISBN) == 13):
            print("Invalid input. ISBN must consist of 13 positive integer numbers.")
            ISBN = input("Enter ISBN: ")

        # Get other book details from user
        author = input("Enter author(leave blank if can't find): ")
        title = input("Enter title(leave blank if can't find): ")
        publisher = input("Enter publisher(leave blank if can't find): ")
        genre = input("Enter genre(leave blank if can't find): ")
        year_published = input("Enter year published(leave blank if can't find): ")
        while not validate_year(year_published):
            print("Invalid input. Year must be a 4-digit integer.")
            year_published = input("Enter year published(leave blank if can't find): ")

        date_purchased = input("Enter date purchased(leave blank if can't find): ")
        status = input("Enter status(leave blank if can't find): ")

        # Create a new book object and add it to the book list
        new_book = Book(ISBN, author, title, publisher, genre, year_published, date_purchased, status)
        new_book.add_new_book()

        print(f"\nAdd {'successful' if new_book in Book.bookList else 'failed'}. Book: {new_book}")

    elif choice == 2:
        # Option 2: Remove book
        search_results = []
        try:
            search_choice = int(input("Search by:\n1. ISBN\n2. Author\n3. Title\nEnter your choice: "))
        
            if search_choice == 1:
                ISBN = input("Enter ISBN: ")
                while not validate_ISBN(ISBN):
                    print("Invalid input. ISBN must consist of 13 positive integer number.(leave blank for cancel)")
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
                continue  # This will go back to the beginning of the loop

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        # You may choose to handle this differently, like asking the user to input the choice again.


        if not search_results:
            print("\nNo matching books found.")
        else:
            print("\nMatching Books:")
            for result in search_results:
                print(result)
         # Prompt for confirmation to delete
        
            while True:
                delete_confirmation = input("Do you want to delete the matched book(s)? (yes/no): ").lower()
                if delete_confirmation in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if delete_confirmation == "yes":
                for result in search_results:
                    Book.bookList.remove(result)
                print("Delete successful.")
            else:
                print("Delete canceled.")
                  

    elif choice == 3:
        # Option 3: Update book
        search_results = []      
        try:
            search_choice = int(input("Search by:\n1. ISBN\n2. Author\n3. Title\nEnter your choice: "))
        
            if search_choice == 1:
                ISBN = input("Enter ISBN: ")
                while not validate_ISBN(ISBN):
                    print("Invalid input. ISBN must consist of 13 positive integer number.(leave blank for cancel)")
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
                continue  # This will go back to the beginning of the loop

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        # You may choose to handle this differently, like asking the user to input the choice again.

        if not search_results:
            print("\nNo matching books found.")
        else:
            print("\nMatching Books:")
            for result in search_results:
                print(result)

            # Prompt for updated information based on search criteria
            if search_choice == 1:
                # If searching by ISBN, don't allow changes to ISBN
                author = input("Enter new author (leave blank to keep current): ")
                title = input("Enter new title (leave blank to keep current): ")
                publisher = input("Enter new publisher (leave blank to keep current): ")
                genre = input("Enter new genre (leave blank to keep current): ")
                year_published = input("Enter new year published (leave blank to keep current): ")
                while not (validate_year(year_published)):
                    print("Invalid input. Year must be a 4-digit integer.")
                    year_published = input("Enter year published: ")

                date_purchased = input("Enter new date purchased (leave blank to keep current): ")
                status = input("Enter new status (leave blank to keep current): ")
            elif search_choice == 2:
                # If searching by author, don't allow changes to author
                ISBN = input("Enter ISBN: ")
                while not validate_ISBN(ISBN):
                    print("Invalid input. ISBN must consist of 13 positive integer number.")
                    ISBN = input("Enter ISBN: ")

                title = input("Enter new title (leave blank to keep current): ")
                publisher = input("Enter new publisher (leave blank to keep current): ")
                genre = input("Enter new genre (leave blank to keep current): ")
                year_published = input("Enter new year published (leave blank to keep current): ")
                while not (validate_year(year_published)):
                    print("Invalid input. ISBN must consist of 13 positive integer number.")
                    year_published = input("Enter year published: ")

                date_purchased = input("Enter new date purchased (leave blank to keep current): ")
                status = input("Enter new status (leave blank to keep current): ")
            elif search_choice == 3:
                # If searching by title, don't allow changes to title
                ISBN = input("Enter ISBN: ")
                while not validate_ISBN(ISBN):
                    print("Invalid input. ISBN must be an integer.")
                    ISBN = input("Enter ISBN: ")
                    
                author = input("Enter new author (leave blank to keep current): ")
                publisher = input("Enter new publisher (leave blank to keep current): ")
                genre = input("Enter new genre (leave blank to keep current): ")
                year_published = input("Enter new year published (leave blank to keep current): ")
                while not (validate_year(year_published)):
                    print("Invalid input. Year must be a 4-digit integer.")
                    year_published = input("Enter year published: ")

                date_purchased = input("Enter new date purchased (leave blank to keep current): ")
                status = input("Enter new status (leave blank to keep current): ")

            # Update only the fields that are not left blank
            for result in search_results:
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

            # Display the updated book information
            print("\nUpdated Book Information:")
            for result in search_results:
                print(result)

            print("Update successful.")

    elif choice == 4:
        # Option 4: Display all books
        print("\n")
        for bk in book.display_book_list():
            print(bk)

    elif choice == 5:
        # Option 5: Search for books
        search_results = []
        try:
            search_choice = int(input("Search by:\n1. ISBN\n2. Author\n3. Title\nEnter your choice: "))
        
            if search_choice == 1:
                ISBN = input("Enter ISBN: ")
                while not validate_ISBN(ISBN):
                    print("Invalid input. ISBN must consist of 13 positive integer number.(leave blank for cancel)")
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
                continue  # This will go back to the beginning of the loop

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        # You may choose to handle this differently, like asking the user to input the choice again.
        
        if not search_results:
            print("\nNo matching books found.")
        else:
            print("\nMatching Books:")
            for result in search_results:
                print(result)

    elif choice == 6:
        # Option 6: Exit the program
        print("Exiting the program.")
        # Write books back to the file when the program exits
        write_books_to_file("books_StudentID.txt")
        break  # Exit the loop and end the program
