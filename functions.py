# Lesson 1 - Writing Functions

def greet(name):
    return f"Hello, {name}!"

# Example usage
print(greet("Praise"))
# Lesson 2 - Modules

# Save this file as mymodule.py
def square(x):
    return x * x

def cube(x):
    return x * x * x
# Lesson 3 - Importing Modules

# Importing custom module (assuming mymodule.py is in the same directory)
import mymodule

print("Square of 4:", mymodule.square(4))
print("Cube of 3:", mymodule.cube(3))

# Importing built-in module
import math
print("Square root of 16:", math.sqrt(16))
# Lesson 4 - Rectangle Area and Perimeter Calculator

def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

# Example usage
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print("Area:", area)
print("Perimeter:", perimeter)