class User:
    def __init__(self,id,name,email,number):
        self.id = id
        self.name = name
        self.email = email
        self.number = number

    def request_locker(self,pacakage,lockerrrom,locker_service):
        return locker_service.assign_locker(self, pacakage, lockerrrom)

    def pickup_item(self,order,otp,locker_service):
        return locker_service.pickup_package(order, otp)
