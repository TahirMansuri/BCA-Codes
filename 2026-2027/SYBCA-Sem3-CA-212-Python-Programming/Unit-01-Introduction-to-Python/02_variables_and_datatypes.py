"""
===================================================================
Program Name : 02_variables_and_datatypes.py
Subject      : Python Programming (SYBCA - Sem 3)
Institution  : IMRD, Shahada
Description  : Demonstrates dynamic typing, standard data types,
               type conversion (casting), and user input.
===================================================================
"""

# 1. Standard Data Types
roll_no = 101                 # Integer
percentage = 87.50           # Float
student_name = "Amit Patil"   # String
is_regular = True             # Boolean
subject_list = ["Python", "DBMS", "Software Engg"] # List

print("--- Data Types & type() function ---")
print(f"roll_no: {roll_no}, Type: {type(roll_no)}")
print(f"percentage: {percentage}, Type: {type(percentage)}")
print(f"student_name: {student_name}, Type: {type(student_name)}")
print(f"is_regular: {is_regular}, Type: {type(is_regular)}")

# 2. Type Casting & User Input
print("\n--- Taking User Input ---")
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
total = num1 + num2
print(f"Sum of {num1} and {num2} = {total}")
