class Order:
    def __init__(self,id,user,pacakage,locker,otp):
        self.id = id
        self.user = user
        self.pacakage = pacakage
        self.locker = locker
        self.otp = otp
        self.is_delivered = False
        self.is_picked_up = False

    def mark_delivered(self):
        self.is_delivered = True

    def mark_picked_up(self):
        self.is_picked_up = True
