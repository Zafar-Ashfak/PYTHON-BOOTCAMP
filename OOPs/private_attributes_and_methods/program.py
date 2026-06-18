class Account:
    bank_name = "SBI"
    def __init__(self, acc_no, password):
        self.acc_no = acc_no
        self.__password = password # makes the password attribute private

    # Setter
    def set_password(self, new_password):
        self.__password = new_password

    # Getter
    def get_password(self):
        return self.__password

# Creating object of class Account
acc1 = Account(43138649198, "IamZafar@008")
print(f"Account Number: {acc1.acc_no}")

# AttributeError: 'Account' object has no attribute '--password'
# print(f"Password: {acc1.__password}")

acc1.set_password("IamGroot@007")
print(f"Your new password is: {acc1.get_password()}")
