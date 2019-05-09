import math

width = input("Enter the wight: ")
height = input("Enter the height: ")
width = int(width)
height = int(height)

def rectangle_area():
    return width * height

print(f"The rectangle Area is {rectangle_area()}")