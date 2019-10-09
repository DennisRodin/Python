#This code will ask the user to enter a random number. The program will then tell the user if the number is odd or even.
num = int(input("Give me a number to check: "))

#If the modulus has got a remainder, the number is odd (uneven). If the modulus has got "0" as a remainder, the number is even.
nun = int(num)
outcome = num % 2

zero = 0

if int(outcome > zero) :
    print("The number is odd.")
else :
    print("The number is even.")