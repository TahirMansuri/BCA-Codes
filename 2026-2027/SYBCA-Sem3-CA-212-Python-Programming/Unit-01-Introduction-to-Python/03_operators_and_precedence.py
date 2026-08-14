"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 1 - Introduction to Python
Program Name : 03_operators_and_precedence.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates all categories of Python operators:
               1. Arithmetic (+, -, *, /, //, %, **)
               2. Comparison / Relational (==, !=, >, <, >=, <=)
               3. Logical (and, or, not)
               4. Assignment (=, +=, -=, etc.)
               5. Membership (in, not in)
               6. Identity (is, is not)
               7. Operator Precedence demonstration
===================================================================
"""

a = 15
b = 4

print("--- 1. Arithmetic Operators ---")
print("a =", a, ", b =", b)
print("Addition (a + b)        :", a + b)
print("Subtraction (a - b)     :", a - b)
print("Multiplication (a * b)  :", a * b)
print("Division (a / b)        :", a / b)
print("Floor Division (a // b) :", a // b, " (integer quotient)")
print("Modulus / Remainder (%) :", a % b)
print("Exponent / Power (a ** b):", a ** b)

print("\n--- 2. Comparison / Relational Operators ---")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)

print("\n--- 3. Logical Operators ---")
x = True
y = False
print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)

print("\n--- 4. Membership Operators ---")
languages = ["Python", "PHP", "C++", "Java"]
print("'Python' in languages    :", "Python" in languages)
print("'Ruby' not in languages  :", "Ruby" not in languages)

print("\n--- 5. Identity Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 == list2 (Same values?)  :", list1 == list2)
print("list1 is list2 (Same memory?)  :", list1 is list2)
print("list1 is list3 (Same object?)  :", list1 is list3)

print("\n--- 6. Operator Precedence ---")
calc_result = 10 + 5 * 2 ** 3 - (4 / 2)
print("Expression: 10 + 5 * 2 ** 3 - (4 / 2)")
print("Evaluated Result:", calc_result)
