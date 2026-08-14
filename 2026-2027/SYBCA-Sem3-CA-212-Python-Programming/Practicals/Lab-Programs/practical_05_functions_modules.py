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

import math

print("=== Functions and Modules ===")

# User-defined function
def calculate_circle_area(radius):
    area = math.pi * radius * radius
    return area

def greet_user(name, course = "BCA"):
    print("Welcome", name, "! You are enrolled in", course, "course.")

print("\n--- User-Defined Functions ---")
greet_user("Amit")
greet_user("Priya", "MCA")

print("\n--- Function with math Module ---")
r = 5
area = calculate_circle_area(r)
print("Radius       :", r)
print("Circle Area  :", area)

print("\n--- More math Module Functions ---")
print("Square root of 16 :", math.sqrt(16))
print("Factorial of 5    :", math.factorial(5))
print("Value of Pi       :", math.pi)


"""
===========================
Expected Output:
===========================
=== Functions and Modules ===

--- User-Defined Functions ---
Welcome Amit ! You are enrolled in BCA course.
Welcome Priya ! You are enrolled in MCA course.

--- Function with math Module ---
Radius       : 5
Circle Area  : 78.53981633974483

--- More math Module Functions ---
Square root of 16 : 4.0
Factorial of 5    : 120
Value of Pi       : 3.141592653589793
===========================
"""
