print("This script gives you three chances to get the pin correct.")

PINcorrect = str(1234)

PINattempt = str(input("Enter a four digit PIN: "))

if PINattempt == PINcorrect:
	print("This PIN is correct!")

else:
	for x in range (0,2):
		print("Dude, try again.")

		PINattempt = input("Enter a four digit PIN: ")

	print("Nope. You're out of tries.")


