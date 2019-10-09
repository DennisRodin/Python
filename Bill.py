
# Every person that paid a total of 200,- EUR in the restaurant, you get 20% discount for your next order.
# Task: One person came into restaurant for 22 times and has always ordered a hamburger for 12,- EUR.
# How much has the person paid in total and is it enough for a 20% discount?
Hamburger = 12.00
tax = 7/100
tip = 15/100
occurred = 5

Hamburger += Hamburger*tax
total = Hamburger + Hamburger*tip

discount = int(occurred)*int(total)

if discount >= 200:
   print("Yes, the person gets a 20% discount. ")
else:
   print("No, the person wont get a 20% discount. ")
