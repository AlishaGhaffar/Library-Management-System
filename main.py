from random import choice

books = []

# ---------------- FUNCTIONS FIRST ----------------

def add_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists!")
            return

    title = input("Enter Book Title: ")
    if title == "":
        print("Title cannot be empty!")
        return

    author = input("Enter Author: ")
    if author == "":
        print("Author cannot be empty!")
        return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book added successfully!")


def view_books():
    if len(books) == 0:
        print("No books available.")
        return

    print("\n===== ALL BOOKS =====")

    for book in books:
        print("\n-------------------")
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])

        if book["status"] == "Issued":
            print("Status: ISSUED ❌ (Not Available)")
        else:
            print("Status: AVAILABLE ✅")


def search_book():
    name = input("Enter book title to search: ")

    found = False

    for book in books:
        if name.lower() in book["title"].lower():
            print("\nBook Found:")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            found = True

    if not found:
        print("Book not found!")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book already issued!")
            return

    print("Book not found!")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book returned successfully!")
            else:
                print("Book is already available!")
            return

    print("Book not found!")


def remove_book():
    book_id = input("Enter Book ID to remove: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book removed successfully!")
            return

    print("Book not found!")


def main_menu():
    while True:
        print("\n==============================")
        print(" Library Management System")
        print("==============================")
        print("1. Add Book")
        print("2. Search Book")
        print("3. View All Books")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            view_books()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            remove_book()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

# ---------------- RUN PROGRAM LAST ----------------
main_menu()