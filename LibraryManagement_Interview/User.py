from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @abstractmethod
    def reset_password(self):
        pass
