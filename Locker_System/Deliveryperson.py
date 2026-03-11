from User import User

class Delivertperson(User):
    def __init__(self, id, name, email, number):
        super().__init__(id, name, email, number)

    def deliver_order(self,order,otp,locker_service):
        return locker_service.deliver_package(order, otp)

    def get_return_order(self,order,otp,locker_service):
        return locker_service.pickup_package(order, otp)
