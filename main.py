from banking import Savings, Checking

ba1 = Savings("Ariel Vera", 100, 25, 22135099, 606047593, 0.5)
ba1.print_customer_information()
ba1.apply_interest()
ba1.print_customer_information()

ba2 = Checking("Travis Marshall", 2500, 500, 41096590, 693011257, 500)
ba2.print_customer_information()
ba2.apply_transfer(ba1, 350)
ba2.print_customer_information()

ba1.print_customer_information()