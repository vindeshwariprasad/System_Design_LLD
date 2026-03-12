from datetime import datetime, timedelta
from Enum import BookStatus

MAX_LENDING_DAYS = 15


class BookItem:
    def __init__(self, id, book, rack):
        self.id = id
        self.book = book
        self.rack = rack
        self.status = BookStatus.FREE
        self.borrowed_by = None
        self.due_date = None
        self.is_reference_only = False

    def checkout(self, member_id):
        if self.is_reference_only:
            print(f"BookItem {self.id} is reference only.")
            return False
        if self.status != BookStatus.FREE:
            print(f"BookItem {self.id} not available.")
            return False
        self.status = BookStatus.TAKEN
        self.borrowed_by = member_id
        self.due_date = datetime.now() + timedelta(days=MAX_LENDING_DAYS)
        print(f"BookItem {self.id} checked out. Due: {self.due_date.date()}")
        return True

    def return_book(self):
        if self.status != BookStatus.TAKEN:
            print(f"BookItem {self.id} not loaned out.")
            return False
        overdue = max(0, (datetime.now() - self.due_date).days) if datetime.now() > self.due_date else 0
        self.status = BookStatus.FREE
        self.borrowed_by = None
        self.due_date = None
        print(f"BookItem {self.id} returned.")
        return overdue

    def reserve(self):
        if self.status != BookStatus.FREE:
            print(f"BookItem {self.id} cannot be reserved.")
            return False
        self.status = BookStatus.RESERVED
        print(f"BookItem {self.id} reserved.")
        return True

    def renew(self):
        if self.status != BookStatus.TAKEN:
            print("Cannot renew, not loaned.")
            return False
        self.due_date += timedelta(days=MAX_LENDING_DAYS)
        print(f"BookItem {self.id} renewed. Due: {self.due_date.date()}")
        return True

    def __str__(self):
        return f"BookItem({self.id}, {self.status.name})"
