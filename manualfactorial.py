# Add up everything from 1 to your input integer

print("Yo, enter in a integer and we'll add up the numbers between your integer and 1.")

myinteger = int(input("Yo! Enter an integer: "))

result = 0 

for x in range(0, myinteger+1):

	result += x

print("Yo! Your integer added up is %s." %(result))