from LockerStatus import LockerSize
from Locker import Locker
from Lockerroom import Lockerrrom
from Pacakage import Pacakage
from User import User
from Deliveryperson import Delivertperson
from LockerService import LockerService

# ---------- Setup ----------
# create lockers of different sizes
l1 = Locker(1, LockerSize.SMALL)
l2 = Locker(2, LockerSize.MEDIUM)
l3 = Locker(3, LockerSize.LARGE)
l4 = Locker(4, LockerSize.XLARGE)

# create locker room
room = Lockerrrom(1, [l1, l2, l3, l4])

# singleton locker service — get_instance() creates once, returns same object every time
service = LockerService.get_instance()
service2 = LockerService.get_instance()
print(f"Same instance? {service is service2}")  # True — proves singleton

# ---------- Flow 1: User requests locker, delivery person delivers ----------
print("=" * 50)
print("FLOW 1: User requests locker -> Delivery person delivers -> User picks up")
print("=" * 50)

user = User(1, "Alice", "alice@mail.com", "1234567890")
pkg = Pacakage(101, LockerSize.MEDIUM, "2026-03-11")

# Step 1: user requests a locker (AVAILABLE -> BOOKED)
print("\n--- Step 1: User requests locker ---")
order = user.request_locker(pkg, room, service)

# Step 2: delivery person delivers using OTP (BOOKED -> FILLED)
print("\n--- Step 2: Delivery person delivers package ---")
dp = Delivertperson(2, "Bob", "bob@mail.com", "9876543210")
dp.deliver_order(order, order.otp, service)

# Step 3: user picks up using OTP (FILLED -> AVAILABLE)
print("\n--- Step 3: User picks up package ---")
user.pickup_item(order, order.otp, service)

# ---------- Flow 2: Wrong OTP rejected ----------
print("\n" + "=" * 50)
print("FLOW 2: Wrong OTP gets rejected")
print("=" * 50)

pkg2 = Pacakage(102, LockerSize.SMALL, "2026-03-11")
order2 = user.request_locker(pkg2, room, service)

print("\n--- Delivery with wrong OTP ---")
dp.deliver_order(order2, "0000", service)

print("\n--- Delivery with correct OTP ---")
dp.deliver_order(order2, order2.otp, service)

# ---------- Flow 3: No locker available ----------
print("\n" + "=" * 50)
print("FLOW 3: No locker available for oversized package")
print("=" * 50)

# fill up all lockers first
pkg3 = Pacakage(103, LockerSize.SMALL, "2026-03-11")
pkg4 = Pacakage(104, LockerSize.LARGE, "2026-03-11")
pkg5 = Pacakage(105, LockerSize.XLARGE, "2026-03-11")
o3 = user.request_locker(pkg3, room, service)
if o3: dp.deliver_order(o3, o3.otp, service)
o4 = user.request_locker(pkg4, room, service)
if o4: dp.deliver_order(o4, o4.otp, service)
o5 = user.request_locker(pkg5, room, service)
if o5: dp.deliver_order(o5, o5.otp, service)

# now try to request another locker — all full
print("\n--- All lockers full, requesting another ---")
pkg6 = Pacakage(106, LockerSize.SMALL, "2026-03-11")
user.request_locker(pkg6, room, service)
