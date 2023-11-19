import streamlit as st

class Book:
    def __init__(self, title, available):
        self.title = title.lower()
        self.available = available

# Sample book database
books_database = [
    Book("The Catcher in the Rye", True),
    Book("To Kill a Mockingbird", True),
    Book("1984", False),
    Book("The Great Gatsby", False),
    Book("Brave New World", False),
    Book("One Hundred Years of Solitude", True),
    Book("Harry Potter and the Sorcerer's Stone", True),
    Book("The Hobbit", False),
    Book("The Lord of the Rings", True),
    Book("Pride and Prejudice", True),
]

# Sort the books_database based on lowercase titles
books_database.sort(key=lambda x: x.title)

def binary_search(data, key):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        current = data[mid].title

        if key.lower() == current:
            return mid
        elif key.lower() < current:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def search_books():
    user_input = st.text_input("Enter a keyword to search:")

    if st.button("Search"):
        index = binary_search(books_database, user_input)

        if index != -1:
            # Display the availability of the book
            if books_database[index].available:
                st.success(f"Book '{books_database[index].title}' is available to rent!")
            else:
                st.warning(f"Book '{books_database[index].title}' is currently rented.")
        else:
            st.error("We do not have the book you're looking for. How about a different book?")

# Streamlit app setup
st.title("Book Search App")

search_books()
