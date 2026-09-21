class ATM:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    def deposit(self):
        amount = float(input(f"{self.name}, enter amount to deposit: "))

        if amount > 0:
            self.__balance += amount
            print(f"Rs. {amount} deposited successfully.")
        else:
            print("Amount must be greater than 0.")

    def withdraw(self):
        amount = float(input(f"{self.name}, enter amount to withdraw: "))

        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"{self.name}'s current balance: Rs. {self.__balance}")


client1 = ATM("Ali", "1001", 5000)
client2 = ATM("Ahmed", "1002", 10000)
client3 = ATM("Usman", "1003", 15000)


print("\n--- Client 1 ---")
client1.check_balance()
client1.deposit()
client1.check_balance()


print("\n--- Client 2 ---")
client2.check_balance()
client2.deposit()
client2.check_balance()


print("\n--- Client 3 ---")
client3.check_balance()
client3.deposit()
client3.check_balance()