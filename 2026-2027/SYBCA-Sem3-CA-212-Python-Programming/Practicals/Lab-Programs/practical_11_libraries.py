"""
===================================================================
Practical No : Practical 11
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to demonstrate the working of 
               libraries.
===================================================================
"""

import random
import datetime
import math

print("=== Working with Python Libraries ===")

print("\n--- 1. random Library ---")
random_num = random.randint(1, 100)
print("Random number between 1 to 100 :", random_num)

students = ["Amit", "Priya", "Rahul", "Sneha"]
lucky_student = random.choice(students)
print("Randomly selected student      :", lucky_student)

print("\n--- 2. datetime Library ---")
current = datetime.datetime.now()
print("Current Date and Time :", current)

formatted = current.strftime("%A, %d %B %Y")
print("Formatted Date        :", formatted)

print("\n--- 3. math Library ---")
print("Square root of 25 :", math.sqrt(25))
print("Value of Pi       :", math.pi)
print("2 to the power 3  :", math.pow(2, 3))
print("Factorial of 5    :", math.factorial(5))


"""
===========================
Expected Output:
===========================
=== Working with Python Libraries ===

--- 1. random Library ---
Random number between 1 to 100 : 47
Randomly selected student      : Rahul

--- 2. datetime Library ---
Current Date and Time : 2026-08-15 01:30:00.123456
Formatted Date        : Saturday, 15 August 2026

--- 3. math Library ---
Square root of 25 : 5.0
Value of Pi       : 3.141592653589793
2 to the power 3  : 8.0
Factorial of 5    : 120
===========================
Note: random output will vary on every run.
"""
