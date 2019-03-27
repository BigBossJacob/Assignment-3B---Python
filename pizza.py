#Importing math functionality to the program
import math

#This is where the user chooses the size of the pizza
sizechoice = int(input("Type 1 for large or 2 for Extra Large "))
if sizechoice == 1: 
	sizeOfPizza = 6
	print ("Large Pizza Selected")
	print (" ")
elif sizechoice == 2:
	sizeOfPizza = 10
	print ("Extra Large Pizza Selected")
	print (" ")
else: 
	print ("Unreasonable Choice") 
		
#This is where the user chooses the number of toppings
notchoice = int(input("Type 1, 2, 3, or 4 for the number of toppings you want "))
if notchoice == 1:
	numberOfToppings = 1
	print ("1 Topping Selected")
	print (" ")
elif notchoice == 2:
	numberOfToppings = 1.75
	print ("2 Toppings Selected")
	print (" ")
elif notchoice == 3:
	numberOfToppings = 2.50
	print ("3 Toppings Selected")
	print (" ")
elif notchoice == 4:
	numberOfToppings = 3.35
	print ("4 Toppings Selected")
	print (" ")
else: 
	print ("Unreasonable Choice")

#These are the variables for the cost calculations
subtotal = (sizeOfPizza + numberOfToppings)
totalcost = (sizeOfPizza + numberOfToppings)*1.13

#This is where/when the program will output the final answer
print (" ")
print ("The subtotal is", subtotal)
print ("The tax is 13%")
print ("The total cost is", totalcost)




