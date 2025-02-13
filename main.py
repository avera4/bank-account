class BankAccount:
    title = "Harvest & Trustee"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        new_balance = self.current_balance - amount
        if new_balance < self.minimum_balance:
            print(f"ERROR: {self.customer_name} cannot withdraw ${amount} due to their minimum balance threshold!\n")
        else:
            self.current_balance = new_balance

    def print_customer_information(self):
        print(f"Title of Bank: {self.title}\n"
              f"Customer Name: {self.customer_name}\n"
              f"Current Balance: {self.current_balance}\n"
              f"Minimum Balance: {self.minimum_balance}\n")

class Savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)

class Checking(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)

ba1 = BankAccount("Ariel Vera", 100, 25)
ba1.print_customer_information()
ba1.deposit(100)
ba1.withdraw(200)
ba1.deposit(200)
ba1.withdraw(100)
ba1.print_customer_information()

ba2 = BankAccount("Travis Marshall", 2500, 500)
ba2.print_customer_information()
ba2.deposit(500)
ba2.withdraw(1000)
ba2.deposit(1000)
ba2.withdraw(3000)
ba2.print_customer_information()
