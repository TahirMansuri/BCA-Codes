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

print("=== Working with Python Libraries ===\n")
print("Note: If 'math' and 'random' are built-in, no installation is needed.")
print("For external libraries like 'numpy' or 'pandas', you need to install them using: pip install numpy pandas\n")

# 1. Demonstrating built-in library 'random'
import random

print("--- 1. Using the 'random' Library ---")
# Generating a random integer between 1 and 100
random_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_num}")

# Choosing a random item from a list
students = ["Amit", "Priya", "Rahul", "Sneha"]
lucky_student = random.choice(students)
print(f"Randomly selected student: {lucky_student}")


# 2. Demonstrating built-in library 'datetime'
import datetime

print("\n--- 2. Using the 'datetime' Library ---")
# Getting the current date and time
current_datetime = datetime.datetime.now()
print(f"Current Date and Time: {current_datetime}")

# Formatting the date
formatted_date = current_datetime.strftime("%A, %d %B %Y")
print(f"Formatted Date: {formatted_date}")


# 3. Simple demonstration of math library
import math

print("\n--- 3. Using the 'math' Library ---")
number = 25
print(f"Square root of {number}: {math.sqrt(number)}")
print(f"Value of Pi: {math.pi}")
print(f"2 to the power of 3: {math.pow(2, 3)}")

print("\n(To demonstrate external libraries like numpy/pandas, please install them via terminal first.)")
