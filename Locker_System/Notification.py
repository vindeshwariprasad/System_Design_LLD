class Notification:
    def send_otp(self,user,otp,locker):
        print(f"[NOTIFICATION] OTP {otp} sent to {user.name} ({user.email}) for locker {locker.id}")
