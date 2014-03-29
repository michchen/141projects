# CS 141 Project 1
# Proj1.py
# Michelle Chen
# mchen01@email.wm.edu, (937)423-9630

# Program to determine: the area and perimeter of a triangle given the lower
# edge and height, and to figure out the volume and surface area of a cone that
# is created by rotating the right triangle around an axis that is the height
# of the right triangle.

import math

radius = input("Please enter the triangle's radius ==> ")
# echo printing
print (radius)
radius = float(radius)

height = input("Please enter the triangle's height ==> ")
print (height)
height = float(height)

# All of the calculations for the triangle and cone
perimeter = radius + height + math.sqrt(radius ** 2 + height ** 2)
area = (radius * height) / 2

surfArea = math.pi * radius * (radius + math.sqrt (radius ** 2 + height ** 2))
volume = math.pi * radius ** 2 * height / 3

# Prints the results, with blank lines and lines of hyphens
print()
print("-" * 40)
print()
# Below, the format allows for a specified spacing
print("%30s %9.3f" % ("The triangle's radius = ", radius))
print("%30s %9.3f" % ("The triangle's height = ", height))
print("%30s %9.3f" % ("The triangle's area = ", area))
print("%30s %9.3f" % ("The triangle's perimeter = ", perimeter))
print("%30s %9.3f" % ("The cone's volume = ", volume))
print("%30s %9.3f" % ("The cone's surface area = ", surfArea))
print()
print("-" * 40)
print()
print("Thank you for using this program")