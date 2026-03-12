from User import User
from Enum import AccountStatus


class Librarian(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)

    def reset_password(self):
        print(f"Password reset for librarian {self.name}.")

    def add_book(self, catalog, book):
        catalog.add_book(book)
        print(f"Book '{book.title}' added to catalog.")

    def block_member(self, member):
        if member.status == AccountStatus.ACTIVE:
            member.status = AccountStatus.BLOCKED
            print(f"{member.name} blocked.")
        else:
            print(f"{member.name} already blocked.")

    def unblock_member(self, member):
        if member.status == AccountStatus.BLOCKED:
            member.status = AccountStatus.ACTIVE
            print(f"{member.name} unblocked.")
        else:
            print(f"{member.name} not blocked.")
