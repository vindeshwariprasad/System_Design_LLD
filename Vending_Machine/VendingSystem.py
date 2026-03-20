from Enum import VendingState


class VendingSystem:
    def __init__(self, id, racks=None, size=20):
        self.id = id
        self.racks = racks or {}       # {rack_id: Rack}
        self.size = size
        self._state = VendingState.Idle
        self._money_inserted = 0
        self._selected_rack_id = None



    def add_rack(self, rack):
        if len(self.racks) < self.size:
            self.racks[rack.id] = rack
            print(f"Rack {rack.id} added")
        else:
            print("Not enough space to add rack")

    def remove_rack(self, rack_id):
        if rack_id in self.racks:
            del self.racks[rack_id]
            print(f"Rack {rack_id} removed")
        else:
            print("Rack not present")



    # Step 1: User inserts money
    def insert_money(self, amount):
        if self._state not in (VendingState.Idle, VendingState.MoneyInserted):
            print("Machine is busy, please wait")
            return

        self._money_inserted += amount
        self._state = VendingState.MoneyInserted
        print(f"Inserted: {amount} | Total: {self._money_inserted}")

    # Step 2: User selects product (by rack_id)
    def select_product(self, rack_id):
        if self._state != VendingState.MoneyInserted:
            print("Please insert money first")
            return

        # check rack exists
        if rack_id not in self.racks:
            print(f"Rack {rack_id} does not exist")
            self._refund()
            return

        rack = self.racks[rack_id]

        # check product available
        if not rack.is_available():
            print("Product not available in this rack")
            self._refund()
            return

        self._selected_rack_id = rack_id
        self._state = VendingState.ProductSelected

        # Step 3: Check price vs money
        price = rack.get_price()
        if self._money_inserted < price:
            shortfall = price - self._money_inserted
            print(f"Insufficient money. Price: {price}, Inserted: {self._money_inserted}, Need: {shortfall} more")
            self._refund()
            return

        # Step 4: Dispense
        self._dispense(rack, price)

    # Step 4: Dispense product + return change
    def _dispense(self, rack, price):
        self._state = VendingState.Dispensing

        success = rack.remove_product(1)
        if not success:
            print("Dispensing failed")
            self._refund()
            return

        change = self._money_inserted - price
        print(f"SUCCESS: Dispensed '{rack.product.name}'")
        if change > 0:
            print(f"Returning change: {change}")

        self._reset()

    def _refund(self):
        if self._money_inserted > 0:
            print(f"Refunding: {self._money_inserted}")
        self._reset()

    def _reset(self):
        self._state = VendingState.Idle
        self._money_inserted = 0
        self._selected_rack_id = None
