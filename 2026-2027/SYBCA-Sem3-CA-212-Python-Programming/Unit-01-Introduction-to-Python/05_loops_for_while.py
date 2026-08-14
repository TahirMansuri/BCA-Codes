"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 1 - Introduction to Python
Program Name : 05_loops_for_while.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates looping mechanisms:
               1. for loop with range(start, stop, step)
               2. while loop
               3. Sum of first N natural numbers
               4. Mathematical Multiplication Table
===================================================================
"""

# 1. for loop with range()
print("--- 1. Printing Even Numbers from 2 to 20 using for loop ---")
for num in range(2, 21, 2):
    print(num, end=" ")
print()

# 2. Multiplication Table using for loop
print("\n--- 2. Multiplication Table Generator ---")
table_num = 7
print("Multiplication Table for", table_num, ":")
for i in range(1, 11):
    print(table_num, "x", i, "=", table_num * i)

# 3. while loop - Sum of Digits of a Number
print("\n--- 3. Calculate Sum of Digits using while loop ---")
number = 12345
temp = number
digit_sum = 0

while temp > 0:
    remainder = temp % 10
    digit_sum += remainder
    temp = temp // 10

print("Sum of digits in", number, "=", digit_sum)
