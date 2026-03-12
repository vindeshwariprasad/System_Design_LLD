from abc import ABC, abstractmethod


class Search(ABC):
    @abstractmethod
    def search_by_title(self, title):
        pass

    @abstractmethod
    def search_by_author(self, author):
        pass

    @abstractmethod
    def search_by_category(self, category):
        pass
