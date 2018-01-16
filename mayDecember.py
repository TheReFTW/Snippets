def mayDecember():
	spouse1 = int(input("How old are you? "))
	spouse2 = int(input("How old is your partner? "))

	olderspouse = max(spouse1, spouse2)
	youngerspouse = min(spouse1, spouse2)
	acceptableAgeRange = int(((olderspouse/2)+7))

	if spouse1 == spouse2:
		return print("Dude, you and your partner are the same age. Neat.")
	elif youngerspouse >= acceptableAgeRange:
		return print("Dude, you and your partner are within a 'socially acceptable' age difference.")
	elif youngerspouse <= acceptableAgeRange:
		return print("Dude, you and your partner are hella disperate in age! Side eye beginning in 3, 2, 1...")

mayDecember()