import json
import os

DATA_FILE = "books.json"


def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)


def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    if books:
        new_id = max(book["id"] for book in books) + 1
    else:
        new_id = 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "status": "Available"
    }
    books.append(book)
    save_books(books)
    print(f"Book '{title}' added successfully with ID {new_id}!")


def view_books(books):
    if not books:
        print("No books in library.")
        return
    print("\n--- Book List ---")
    for book in books:
        print(f"ID: {book['id']} | {book['title']} by {book['author']} | {book['status']}")
    print("-----------------\n")


def borrow_book(books):
    book_id = int(input("Enter book ID to borrow: "))
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Borrowed"
                save_books(books)
                print(f"You borrowed '{book['title']}'")
            else:
                print("Book already borrowed.")
            return
    print("Book not found.")


def return_book(books):
    book_id = int(input("Enter book ID to return: "))
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Borrowed":
                book["status"] = "Available"
                save_books(books)
                print(f"Returned '{book['title']}'")
            else:
                print("This book was not borrowed.")
            return
    print("Book not found.")


def search_book(books):
    keyword = input("Enter title keyword: ").lower()
    found = [b for b in books if keyword in b["title"].lower()]
    if found:
        print("\n--- Search Results ---")
        for book in found:
            print(f"ID: {book['id']} | {book['title']} by {book['author']} | {book['status']}")
        print("----------------------\n")
    else:
        print("No matching books found.")


def delete_book(books):
    book_id = int(input("Enter book ID to delete: "))
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)
            print(f"Book ID {book_id} deleted successfully.")
            return
    print("Book not found.")


def main():
    books = load_books()
    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Delete Book")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            search_book(books)
        elif choice == "6":
            delete_book(books)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()