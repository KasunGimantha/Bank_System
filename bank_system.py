class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance+amount
        print(f"Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance = self.__balance-amount
            print(f"Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def __str__(self) -> str:
        return f"Current balance {self.__balance}"

    def __add__(self, combine_vale):
        sum = self.__balance + combine_vale.__balance
        return BankAccount(sum)


class ATM:
    def check_balance(self, account):
        print(f"Balance: {account.get_balance()}")

    def withdraw_funds(self, account, amount):
        account.withdraw(amount)

    def deposit_funds(self, account, amount):
        account.deposit(amount)


acc1 = BankAccount(4000)
acc2 = BankAccount(3000)

obj = ATM()

obj.deposit_funds(acc1, 5000)
obj.withdraw_funds(acc1, 1000)
print()
obj.deposit_funds(acc2, 7000)
obj.withdraw_funds(acc2, 2000)
print()

account_sum = acc1+acc2
print(f"Sum of two accounts:{account_sum._BankAccount__balance}")
