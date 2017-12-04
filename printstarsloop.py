print("Welcome to the star printing loop testy thing. Enter in a minimum number of stars you want to see, as well as a multiplier, when prompted.")

starnumber = int(input("How many stars do you want, minimum? "))
multiplier = int(input("What do you want those stars multiplied by? "))

print("Yo, here are your stars!")

for x in range(1, multiplier+1):
	print ("%s * %s = %s Stars" %(starnumber, x, starnumber*x))
	print("*" * (starnumber*x))

print ("That's all the stars we've got for you. Thanks for coming to the star generator.")