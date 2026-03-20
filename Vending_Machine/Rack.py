class Rack:
    def __init__(self, id, product=None, size=10, product_count=0):
        self._id = id
        self._product = product      # what Product this rack holds
        self._size = size             # max capacity
        self._product_count = product_count

    @property
    def id(self):
        return self._id

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product

    @property
    def product_count(self):
        return self._product_count

    def is_available(self):
        return self._product is not None and self._product_count > 0

    def get_price(self):
        if self._product:
            return self._product.price
        return 0

    def add_product(self, product, quantity):
        self._product = product
        if quantity + self._product_count <= self._size:
            self._product_count += quantity
            print(f"Added {quantity} '{product.name}' to rack {self._id}")
        else:
            print("Not enough space to add items")

    def remove_product(self, quantity=1):
        if quantity <= self._product_count:
            self._product_count -= quantity
            print(f"Dispensed {quantity} '{self._product.name}' from rack {self._id}")
            return True
        else:
            print("Not enough items in rack")
            return False
