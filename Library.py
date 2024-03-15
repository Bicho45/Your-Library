import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def add_book():
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    while isbn.isdigit() == False:
        isbn = input("Enter a valid ISBN: ")
    books[isbn] = {'title':title, 'author':author, 'available': True}
    print(f"Book '{title}' by {author} added to the catalog with ISBN {isbn}")

def check_out():
    check_out = input("Enter ISBN to check out: ")
    if check_out in books and books[check_out]['available'] == True:
        books[check_out]['available'] = False
        print(f"Book {books[check_out]['title']} checked out successfully.")
    else:
        print("Sorry, the book is currently checked out.")

def check_in():
    check_in = input("Enter ISBN to check in: ")
    if check_in in books and books[check_in]['available'] == False:
        books[check_in]['available'] = True
        print(f"Book {books[check_in]['title']} checked in successfully.")
    else:
        print("Book not found in the catalog.")

books = {}
while True:
    print("""
--------------------------------------------------------------------------------
Menu
1- Add Book
2- Check out Book
3- Check in Book
4- List Books
5- Exit
""")
    c = int(input("Enter your choice (1-5): "))
    clear_screen()
    if c == 1:
        add_book()
        another_book = input("Do you want to add another book? (y/n): ")
        while another_book == "y":
            clear_screen()
            add_book()
            another_book = input("Do you want to add another book? (y/n): ")
    elif c == 2:
        check_out()
        another_book = input("Do you want to check out another book? (y/n): ")
        while another_book == "y":
            clear_screen()
            check_out()
            another_book = input("Do you want to check out another book? (y/n): ")
    elif c == 3:
        check_in()
        another_book = input("Do you want to check in another book? (y/n): ")
        while another_book == "y":
            clear_screen()
            check_in()
            another_book = input("Do you want to check in another book? (y/n): ")
    elif c == 4:
        print("Library Catalog:")
        for isbn, book_info in books.items():
            print(f"ISBN: {isbn}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['available']}")
        input("Do you want to go back to the main menu? (y/n): ")
    elif c == 5:
        print("Exiting the program....")
        break
    else:
        print("Invalid Choice")
