class BankAccount:
    title = "Harvest & Trustee"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = account_number
        self._routing_number = routing_number

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        new_balance = self.current_balance - amount
        if new_balance < self.minimum_balance:
            print(f"[ERROR] {self.customer_name} cannot withdraw ${amount} due to their minimum balance threshold!\n")
            return False
        else:
            self.current_balance = new_balance
        return True

    def print_customer_information(self):
        print(f"Title of Bank: {self.title}\n"
              f"Customer Name: {self.customer_name}\n"
              f"Current Balance: {self.current_balance}\n"
              f"Minimum Balance: {self.minimum_balance}")

class Savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest = interest

    def apply_interest(self):
        self.deposit(self.current_balance * self.interest)

    def print_customer_information(self):
        super().print_customer_information()
        print(f"Interest Rate: {self.interest}\n")

class Checking(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def apply_transfer(self, account, amount):
        if amount <= self.transfer_limit:
            if self.withdraw(amount):
                account.deposit(amount)
                print(f"[SUCCESS] {self.customer_name} sent ${amount} to {account.customer_name}!\n")
        else:
            print(f"[ERROR] {self.customer_name} cannot send money to {account.customer_name} as they have exceeded their transfer limit!\n")

    def print_customer_information(self):
        super().print_customer_information()
        print(f"Transfer Limit: {self.transfer_limit}\n")

ba1 = Savings("Ariel Vera", 100, 25, 22135099, 606047593, 0.5)
ba1.print_customer_information()
ba1.apply_interest()
ba1.print_customer_information()

ba2 = Checking("Travis Marshall", 2500, 500, 41096590, 693011257, 500)
ba2.print_customer_information()
ba2.apply_transfer(ba1, 350)
ba2.print_customer_information()

ba1.print_customer_information()