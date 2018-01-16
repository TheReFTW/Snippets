def maxCalc():
	num1 = int(input("Give me a number, yo: "))
	num2 = int(input("Give me another number, yo: "))
	num3 = int(input("Give me one, final, number!: "))
	theMax = max(num1, num2, num3)
	return print("Of the three numbers you entered, %s is the largest!" %(theMax))
	
maxCalc()