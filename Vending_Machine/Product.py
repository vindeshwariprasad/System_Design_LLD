class Product:
    def __init__(self, id, name, price, category):
        self._id = id
        self._name = name
        self._price = price
        self._category = category

    def update_price(self, new_price):
        self._price = new_price

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def category(self):
        return self._category
