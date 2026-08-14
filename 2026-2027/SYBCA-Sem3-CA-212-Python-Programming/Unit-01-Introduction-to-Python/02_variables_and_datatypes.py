"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 1 - Introduction to Python
Program Name : 02_variables_and_datatypes.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates dynamic typing, standard data types,
               type conversion and user input.
===================================================================
"""

roll_no = 101
percentage = 87.50
student_name = "Amit Patil"
is_regular = True

print("--- Data Types & type() function ---")
print("roll_no:", roll_no, "  Type:", type(roll_no))
print("percentage:", percentage, "  Type:", type(percentage))
print("student_name:", student_name, "  Type:", type(student_name))
print("is_regular:", is_regular, "  Type:", type(is_regular))

print("\n--- Taking User Input ---")
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
total = num1 + num2
print("Sum of", num1, "and", num2, "=", total)
