print("Welcome to the application for Xavier's School for Gifted Youngsters. To begin, follow the prompts below.")

GPA = float(input("What is your Grade Point Average? "))
SATscore = int(input("What is your total SAT score? "))

if GPA < 1.80: 
	print("Sorry, your Grade Point Average is too low to attend Xavier's School for Gifted Youngsters. Please re-apply when your Grade Point Average is a 1.8 or above.")

elif SATscore < 900:

	print("Sorry, your SAT score is too low to attend Xavier's School for Gifted Youngsters. Please re-apply when your SAT score is a 900 or above.")

elif GPA >= 1.8 and SATscore >= 900:
	print("Congratulations! You're admitted to Xavier's School for Gifted Youngsters. Please report to either the telepath or the dude with laser eyes.")