#Encapsulation
#Activity 3: BankAccount class

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = ""
        self.__balance = 0.0
        self.set_account_number(account_number)
        self.set_balance(balance)

    # Public setter for account number
    def set_account_number(self, account_number):
        if str(account_number).strip():
            self.__account_number = str(account_number)
        else:
            print("Warning: Account number cannot be empty. Value ignored.")

    # Public setter for balance
    def set_balance(self, balance):
        try:
            amount = float(balance)
        except (TypeError, ValueError):
            print("Warning: Balance must be a number. Value ignored.")
            return

        if amount < 0:
            print("Warning: Balance cannot be negative. Value ignored.")
            return

        self.__balance = amount

    # Public getter for account number using @property
    @property
    def account_number(self):
        return self.__account_number

    # Public getter for balance using @property
    @property
    def balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("CA-2026-001", 12500.50)

    print("Object of class BankAccount")
    print("Account Number:", account.account_number)
    print("Balance: PHP {:,.2f}".format(account.balance))

    print("\nUpdating account details...")
    account.set_account_number("CA-2026-002")
    account.set_balance(18000)
    print("Account Number:", account.account_number)
    print("Balance: PHP {:,.2f}".format(account.balance))

    print("\nTrying to set a negative balance...")
    account.set_balance(-500)
    print("Balance after invalid update: PHP {:,.2f}".format(account.balance))
