from User import User
from Enum import AccountStatus

MAX_BOOKS = 5
FINE_PER_DAY = 1.0


class Member(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
        self.status = AccountStatus.ACTIVE
        self.borrowed_books = []
        self.total_fine = 0.0

    def reset_password(self):
        print(f"Password reset for {self.name}.")

    def checkout_book(self, book_item):
        if self.status != AccountStatus.ACTIVE:
            print(f"{self.name} account is {self.status.name}.")
            return False
        if len(self.borrowed_books) >= MAX_BOOKS:
            print(f"{self.name} reached max limit of {MAX_BOOKS} books.")
            return False
        if self.total_fine > 0:
            print(f"{self.name} has unpaid fine of ${self.total_fine:.2f}.")
            return False
        if book_item.checkout(self.id):
            self.borrowed_books.append(book_item)
            return True
        return False

    def return_book(self, book_item):
        if book_item not in self.borrowed_books:
            print(f"{book_item.id} not borrowed by {self.name}.")
            return False
        overdue = book_item.return_book()
        if overdue is False:
            return False
        self.borrowed_books.remove(book_item)
        if overdue > 0:
            fine = overdue * FINE_PER_DAY
            self.total_fine += fine
            print(f"Overdue {overdue} days. Fine: ${fine:.2f}")
        return True

    def renew_book(self, book_item):
        if book_item not in self.borrowed_books:
            print(f"{book_item.id} not borrowed by {self.name}.")
            return False
        return book_item.renew()

    def reserve_book(self, book_item):
        if self.status != AccountStatus.ACTIVE:
            print(f"{self.name} account is {self.status.name}.")
            return False
        return book_item.reserve()

    def pay_fine(self):
        if self.total_fine <= 0:
            print("No fine to pay.")
            return False
        print(f"{self.name} paid fine of ${self.total_fine:.2f}.")
        self.total_fine = 0.0
        return True

    def __str__(self):
        return f"Member({self.name}, {self.status.name}, books={len(self.borrowed_books)})"
