class BankAccount:
    def __init__(self, customer_name, account_number, date_of_opening, balance=0):
        self.customer_name = customer_name
        self.account_number = account_number
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return (
            f"Customer: {self.customer_name}\n"
            f"Account Number: {self.account_number}\n"
            f"Opening Date: {self.date_of_opening}\n"
            f"Balance: {self.balance}"
        )


account = BankAccount(
    "Salah Ali Rashad",
    "ACC1001",
    "2014-07-15",
    1_000_000
)

account.deposit(500)
account.withdraw(3000)

print(account.display_account_info())
