from Catalog import Catalog


class Library:
    _instance = None

    def __init__(self, name):
        self.name = name
        self.catalog = Catalog.get_instance()
        self.members = {}
        self.librarians = {}

    @classmethod
    def get_instance(cls, name="Library"):
        if cls._instance is None:
            cls._instance = cls(name)
        return cls._instance

    def add_member(self, member):
        self.members[member.id] = member
        print(f"Member '{member.name}' added.")

    def add_librarian(self, librarian):
        self.librarians[librarian.id] = librarian

    def __str__(self):
        return f"Library('{self.name}', members={len(self.members)})"
