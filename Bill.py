
"""This code lets you calculate if you are going to receive a configurable discount or not, given by the least amount for the discount.
   You could use this for example in a restaurant, where you have a meal prize, a tax and a tip percentage. 
   You also need to tell the program how often you visited the place,
   so it can calculate the all in all amount of how much you paid for the food in your lifetime. """



meal = int(input("How much did your meal cost? "))
if meal < 0:
   print("Empty") #not working. I wanted to give out a message if there's an invalid key such as the "Enter" key.
else:
  print("")

tax = int(input("What's the tax percentage? "))
if tax < 0:
   print("Empty") #not working. I wanted to give out a message if there's an invalid key such as the "Enter" key.
else:
  print("")

tip = int(input("What was the tip amount? "))
if tip < 0:
   print("Empty") #not working. I wanted to give out a message if there's an invalid key such as the "Enter" key.
else:
  print("")

occurred = int(input("How many times did you visit and eat at the restaurant? "))
if occurred < 0:
   print("Empty") #not working. I wanted to give out a message if there's an invalid key such as the "Enter" key.
else:
  print("")

meal += meal*tax

total = meal + meal*tip

discount = int(occurred)*int(total)

amount_for_discount = 1500 # Change here the restaurants' least amount for the discount.
discount_percentage = 30#%# Change the restaurants' discount percentage here.
if discount >= amount_for_discount:
   print("Yes, you get a " + str(discount_percentage) + "%" + " discount for you next order, because you have paid more than " + str(amount_for_discount) + ",-EUR. " + "The amount you have paid altogether is " + str(total) + ",-EUR. " )
else:
   print("No, you wont get a " + str(discount_percentage) + "%" + " discount, because you have paid less than " + str(amount_for_discount) + ",-EUR. " + "The amount you have paid altogether is " + str(total) + ",-EUR. " )