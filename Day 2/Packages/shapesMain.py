# 1. shapes Package (circle.py, rectangle.py)
'''
A design company builds CAD (Computer-Aided Design) software.
They frequently need to calculate the area and perimeter of shapes.
To avoid rewriting formulas everywhere, they create a shapes package.
'''

from shapes import circle_area, circle_perimeter, rectangle_area, rectangle_perimeter

# Circle
print("Circle area:", circle_area(5))
print("Circle perimeter:", circle_perimeter(5))

# Rectangle
print("Rectangle area:", rectangle_area(10, 4))
print("Rectangle perimeter:", rectangle_perimeter(10, 4))
