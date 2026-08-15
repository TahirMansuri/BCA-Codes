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
print("a =", a, ", b =", b)                                          # Output: a = 15 , b = 4
print("Addition (a + b)        :", a + b)                             # Output: Addition (a + b)        : 19
print("Subtraction (a - b)     :", a - b)                             # Output: Subtraction (a - b)     : 11
print("Multiplication (a * b)  :", a * b)                             # Output: Multiplication (a * b)  : 60
print("Division (a / b)        :", a / b)                             # Output: Division (a / b)        : 3.75
print("Floor Division (a // b) :", a // b, " (integer quotient)")     # Output: Floor Division (a // b) : 3  (integer quotient)
print("Modulus / Remainder (%) :", a % b)                             # Output: Modulus / Remainder (%) : 3
print("Exponent / Power (a ** b):", a ** b)                           # Output: Exponent / Power (a ** b): 50625

print("\n--- 2. Comparison / Relational Operators ---")
print("a == b :", a == b)                                             # Output: a == b : False
print("a != b :", a != b)                                             # Output: a != b : True
print("a > b  :", a > b)                                              # Output: a > b  : True
print("a < b  :", a < b)                                              # Output: a < b  : False

print("\n--- 3. Logical Operators ---")
x = True
y = False
print("x and y :", x and y)                                           # Output: x and y : False
print("x or y  :", x or y)                                            # Output: x or y  : True
print("not x   :", not x)                                             # Output: not x   : False

print("\n--- 4. Membership Operators ---")
languages = ["Python", "PHP", "C++", "Java"]
print("'Python' in languages    :", "Python" in languages)            # Output: 'Python' in languages    : True
print("'Ruby' not in languages  :", "Ruby" not in languages)          # Output: 'Ruby' not in languages  : True

print("\n--- 5. Identity Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 == list2 (Same values?)  :", list1 == list2)             # Output: list1 == list2 (Same values?)  : True
print("list1 is list2 (Same memory?)  :", list1 is list2)             # Output: list1 is list2 (Same memory?)  : False
print("list1 is list3 (Same object?)  :", list1 is list3)             # Output: list1 is list3 (Same object?)  : True

print("\n--- 6. Operator Precedence ---")
calc_result = 10 + 5 * 2 ** 3 - (4 / 2)
print("Expression: 10 + 5 * 2 ** 3 - (4 / 2)")
print("Evaluated Result:", calc_result)                               # Output: Evaluated Result: 48.0
