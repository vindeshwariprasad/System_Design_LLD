from Search import Search
from collections import defaultdict


class Catalog(Search):
    _instance = None

    def __init__(self):
        self._titles = defaultdict(list)
        self._authors = defaultdict(list)
        self._categories = defaultdict(list)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def add_book(self, book):
        self._titles[book.title.lower()].append(book)
        self._authors[book.author.lower()].append(book)
        for cat in book.categories:
            self._categories[cat.lower()].append(book)

    def search_by_title(self, title):
        return self._titles.get(title.lower(), [])

    def search_by_author(self, author):
        return self._authors.get(author.lower(), [])

    def search_by_category(self, category):
        return self._categories.get(category.lower(), [])
