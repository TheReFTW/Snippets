# Calculate geometric area of four shapes: triangles, squares, rectangles, and circles. 
# Present a menu of shapes to the user and then depending on their selection, prompt them for the values necessary to calculate the area of the shape. Display the area once it's complete. 

import math

def triangle_area():
	global area 
	base = float(input("How long is the base of your triangle? "))
	height = float(input("How tall is your triangle? "))
	area = (base*height*0.5)
	return area

def square_area():
	global area 
	side = float(input("How long are the sides of your square? "))
	area = (side**2)
	return area

def rectangle_area():
	global area 
	width = float(input("How wide is your rectangle? "))
	height = float(input("How tall is your rectangle? "))
	area = (width*height)
	return area

def circle_area():
	global area
	radius = float(input("What is the radius of your circle? "))
	area = ((radius**2)*(math.pi))
	return area

def select_geometry():
	print("Welcome to the Shape Area Calculator!")

	unit = input("Are you working in inches or centimeters? ")
	if unit == "inches":
		unit_of_measurement = "inches"
	else:
		unit_of_measurement = "centimeters"

	shape = input("Do you want to calculate the area of a triangle, square, rectangle or circle? ")
	
	if shape == "triangle":
		triangle_area()
	elif shape == "square":
		square_area()
	elif shape == "rectangle":
		rectangle_area()
	elif shape == "circle":
		circle_area()

	return print("The area of your %s is %s square %s." %(shape, area, unit_of_measurement))

select_geometry()




