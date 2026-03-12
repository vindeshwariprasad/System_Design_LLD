from Book import Book
from Book_item import BookItem
from Member import Member
from Librarian import Librarian
from Library import Library

# Singleton
library = Library.get_instance("City Library")
assert library is Library.get_instance()

# Setup
librarian = Librarian("L1", "Alice", "alice@lib.com")
book1 = Book("B1", "Clean Code", "Robert Martin", ["Programming"])
book2 = Book("B2", "Design Patterns", "GoF", ["Programming"])
librarian.add_book(library.catalog, book1)
librarian.add_book(library.catalog, book2)

item1 = BookItem("BI1", book1, "Rack-1")
item2 = BookItem("BI2", book2, "Rack-2")
book1.add_book_item(item1)
book2.add_book_item(item2)

member = Member("M1", "Bob", "bob@email.com")
library.add_member(member)

# Search
print("\n--- Search ---")
print(library.catalog.search_by_title("Clean Code"))
print(library.catalog.search_by_category("Programming"))

# Checkout, Renew, Return
print("\n--- Checkout ---")
member.checkout_book(item1)
member.checkout_book(item2)

print("\n--- Renew ---")
member.renew_book(item1)

print("\n--- Return ---")
member.return_book(item1)
member.return_book(item2)

# Reserve
print("\n--- Reserve ---")
member.reserve_book(item1)

# Block/Unblock
print("\n--- Block ---")
librarian.block_member(member)
member.checkout_book(item2)
librarian.unblock_member(member)
member.checkout_book(item2)

print(f"\n{library}")
print(member)
