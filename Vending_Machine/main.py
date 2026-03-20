from Product import Product
from Rack import Rack
from Enum import ProductType
from VendingSystem import VendingSystem

# --- Setup products ---
coke = Product(1, "Coke", 25, ProductType.Sweet)
chips = Product(2, "Lays Chips", 20, ProductType.Salty)
oreo = Product(3, "Oreo", 15, ProductType.Sweet)

# --- Setup racks with products ---
rack1 = Rack(id="R1")
rack1.add_product(coke, 5)

rack2 = Rack(id="R2")
rack2.add_product(chips, 3)

rack3 = Rack(id="R3")
rack3.add_product(oreo, 0)   # empty rack on purpose

# --- Create vending machine ---
vm = VendingSystem(id="VM-001")
vm.add_rack(rack1)
vm.add_rack(rack2)
vm.add_rack(rack3)

# --- Test Case 1: Success + return change ---
print("\n===== TEST 1: Buy Coke (price=25), insert 30 =====")
vm.insert_money(30)
vm.select_product("R1")       # SUCCESS, change = 5

# --- Test Case 2: Insufficient money ---
print("\n===== TEST 2: Buy Chips (price=20), insert 10 =====")
vm.insert_money(10)
vm.select_product("R2")       # FAIL: need 10 more, refund

# --- Test Case 3: Product not available ---
print("\n===== TEST 3: Buy Oreo (empty rack) =====")
vm.insert_money(20)
vm.select_product("R3")       # FAIL: not available, refund

# --- Test Case 4: Rack doesn't exist ---
print("\n===== TEST 4: Invalid rack =====")
vm.insert_money(20)
vm.select_product("R99")      # FAIL: rack not found

# --- Test Case 5: No money inserted ---
print("\n===== TEST 5: Select without inserting money =====")
vm.select_product("R1")       # FAIL: insert money first

# --- Test Case 6: Exact money ---
print("\n===== TEST 6: Exact money (price=20), insert 20 =====")
vm.insert_money(20)
vm.select_product("R2")       # SUCCESS, no change
