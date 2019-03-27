import math

sizechoice = int(input("Type 1 for large or 2 for Extra Large "))
if sizechoice == 1: 
	sizeOfPizza = 6
	print ("Large Pizza Selected")
elif sizechoice == 2:
	sizeOfPizza = 10
	print ("Extra Large Pizza Selected")
else: 
	print ("Unreasonable Choice") 
		

notchoice = int(input("Type 1, 2, 3, or 4 for the number of toppings you want "))
if notchoice == 1:
	numberOfToppings = 1
	print ("1 Topping Selected")
elif notchoice == 2:
	numberOfToppings = 1.75
	print ("2 Toppings Selected")
elif notchoice == 3:
	numberOfToppings = 2.50
	print ("3 Toppings Selected")
elif notchoice == 4:
	numberOfToppings = 3.35
	print ("4 Toppings Selected")
else: 
	print ("Unreasonable Choice")

subtotal = (sizeOfPizza + numberOfToppings)
totalcost = (sizeOfPizza + numberOfToppings)*1.13

print (" ")
print ("The subtotal is", subtotal)
print ("The tax is 13%")
print ("The total cost is", totalcost)




