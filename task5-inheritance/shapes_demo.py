from shapes import Triangle
from shapes import Circle
from shapes import Rectangle

try:

    circle = Circle(5, "red")
    rectangle = Rectangle(4, 6, "blue")
    triangle = Triangle(3, 4, "green")
    
    #Circle details 
    print("\nCircle Details:")
    print(circle)
    print(f"Area: {circle.area()}")
    print(f"Perimeter: {circle.perimeter()}")

    # Rectangle details
    print("\nRectangle Details:")
    print(rectangle)
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")

    # Triangle details
    print("\nTriangle Details:")
    print(triangle)
    print(f"Area: {triangle.area()}")
    print(f"Perimeter: {triangle.perimeter()}")

except Exception as e:
    print(f"An error occurred: {e}")