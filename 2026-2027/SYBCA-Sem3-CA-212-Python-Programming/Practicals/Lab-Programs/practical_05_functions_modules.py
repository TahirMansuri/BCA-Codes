"""
===================================================================
Practical No : Practical 05
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a Program related to Functions & Modules.
===================================================================
"""

# Importing a built-in module
import math

print("=== Functions and Modules Demonstration ===\n")

# 1. Defining a user-defined function
def calculate_circle_area(radius):
    """This function calculates the area of a circle given its radius."""
    # Using the 'math' module to get the value of pi
    area = math.pi * (radius ** 2)
    return area

# 2. Function with default arguments
def greet_user(name, course="BCA"):
    """Greets the user. Default course is BCA."""
    print(f"Welcome {name}! We hope you enjoy the {course} course.")

# 3. Calling the functions
print("--- Using User-Defined Functions ---")
greet_user("Amit")                  # Uses default course
greet_user("Priya", "MCA")          # Overrides default course

print("\n--- Using Functions with Modules ---")
r = 5.0
circle_area = calculate_circle_area(r)
print(f"The area of a circle with radius {r} is {circle_area:.2f}")

# 4. Using more functions from the 'math' module
print("\n--- Exploring 'math' Module ---")
number = 16
print(f"Square root of {number} is: {math.sqrt(number)}")
print(f"Factorial of 5 is: {math.factorial(5)}")
