class Book:
    def __init__(self, id, title, author, categories):
        self.id = id
        self.title = title
        self.author = author
        self.categories = categories
        self.book_items = []

    def add_book_item(self, book_item):
        self.book_items.append(book_item)

    def __str__(self):
        return f"Book('{self.title}' by {self.author})"
