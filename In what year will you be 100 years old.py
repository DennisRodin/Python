#This program will ask for the users name, his age and then the program will tell the user in what year he will become one hundred years old.
name = input("Give me your name: ")
print("Ok, so your name is " + str(name) + ".")


year_of_birth = input("What year were you born? ")
print("Aight you were born in " + str(year_of_birth) )

year_onehundred = int(year_of_birth) + 100

print("By the year " + str(year_onehundred) + " you will be one hundred years old.")