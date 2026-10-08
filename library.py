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
    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "status": "Available"
    }
    books.append(book)
    save_books(books)
    print(f"Book '{title}' added successfully!")

def view_books(books):
    if not books:
        print("No books in library.")
        return
    print("\n--- Book List ---")
    for book in books:
        print(f"ID: {book['id']} | {book['title']} by {book['author']} | {book['status']}")
    print("-----------------\n")

def main():
    books = load_books()
    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()