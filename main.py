from banking import Savings, Checking

ba1 = Savings("Ariel Vera", 100, 50, 22135099, 606047593, 0.5)
ba2 = Savings("Dexter Morgan", 10000, 5000, 41096590, 693011257, 0.25)
ba3 = Checking("Travis Marshall", 2500, 500, 63251585, 617295583, 500)
ba4 = Checking("Arthur Mitchell", 5000, 1000, 16140736, 815431589, 2500)

ba1.apply_interest() # Ariel now has $150
ba3.withdraw(750) # Travis now has $1,750
ba3.apply_transfer(ba1, 250) # Travis sent $250 to Ariel. Ariel now has $400. Travis now has $1,500
ba2.apply_interest() # Dexter now has $12,500
ba4.withdraw(1500) # Arthur now has $3,500
ba4.withdraw(1000) # Arthur now has $2,500
ba2.apply_interest() # Dexter now has $15,625
ba4.apply_transfer(ba3, 3000) # Arthur couldn't transfer $3,000 due to transfer limit
ba4.apply_transfer(ba3, 2500) # Arthur couldn't transfer $2,500 due to minimum balance
ba4.apply_transfer(ba3, 1500) # Arthur sent $1,500 to Travis. Travis now has $3,000. Arthur now has $1,000

ba1.print_customer_information()
ba2.print_customer_information()
ba3.print_customer_information()
ba4.print_customer_information()