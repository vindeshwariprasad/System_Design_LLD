import random
from Order import Order
from Notification import Notification

class LockerService:
    _instance = None

    def __init__(self):
        if LockerService._instance is not None:
            raise Exception("LockerService is a singleton! Use get_instance()")
        self.orders = {}        # order_id -> Order
        self.otp_map = {}       # (otp, locker_id) -> Order
        self.notification = Notification()
        self._order_counter = 0
        LockerService._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def _generate_otp(self):
        return str(random.randint(1000, 9999))

    def assign_locker(self,user,pacakage,lockerrrom):
        locker = lockerrrom.find_available_locker(pacakage.size)
        if locker is None:
            print(f"No available locker for package {pacakage.id}")
            return None

        locker.book()
        otp = self._generate_otp()
        self._order_counter += 1
        order = Order(self._order_counter, user, pacakage, locker, otp)
        self.orders[order.id] = order
        self.otp_map[(otp, locker.id)] = order

        self.notification.send_otp(user, otp, locker)
        print(f"Locker {locker.id} assigned to user {user.name} | status: {locker.status.value}")
        return order

    def deliver_package(self,order,otp):
        if not self.verify_otp(otp, order.locker.id):
            print("Invalid OTP! Cannot deliver.")
            return False

        order.locker.place_item(order.pacakage)
        order.mark_delivered()
        print(f"Package {order.pacakage.id} placed in locker {order.locker.id} | status: {order.locker.status.value}")
        return True

    def pickup_package(self,order,otp):
        if not self.verify_otp(otp, order.locker.id):
            print("Invalid OTP! Cannot pick up.")
            return None

        item = order.locker.release()
        order.mark_picked_up()
        del self.otp_map[(otp, order.locker.id)]
        print(f"Package {order.pacakage.id} picked up from locker {order.locker.id} | status: {order.locker.status.value}")
        return item

    def verify_otp(self,otp,locker_id):
        return (otp, locker_id) in self.otp_map
