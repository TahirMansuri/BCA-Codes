"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 3 - Python Functions and Modules
Program Name : 03_modules_demo.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates importing custom modules (my_calculator.py)
               and using built-in Python standard libraries.
===================================================================
"""

# Importing custom module
import my_calculator

# Importing built-in standard modules
import math
import random
import datetime
import os
import sys

print("--- 1. Using Custom Module (my_calculator.py) ---")
sum_res = my_calculator.add(10, 5)
mul_res = my_calculator.multiply(10, 5)
print("Addition using module :", sum_res)     # Output: Addition using module : 15
print("Multiply using module :", mul_res)     # Output: Multiply using module : 50

print("\n--- 2. Built-in Math and Random Modules ---")
print("Square root of 36     :", math.sqrt(36)) # Output: Square root of 36     : 6.0
print("Value of Pi           :", math.pi)       # Output: Value of Pi           : 3.141592653589793

# Generating random integer between 1 and 10
rand_num = random.randint(1, 10)
print("Random Number (1-10)  :", rand_num)     # Output: (e.g. 7, value will vary)

print("\n--- 3. Built-in Datetime Module ---")
# Getting current local date
today = datetime.date.today()
print("Today's Date          :", today)        # Output: (e.g. 2026-08-15, value will vary)

print("\n--- 4. Built-in OS and SYS Modules ---")
# Current directory path
current_dir = os.path.basename(os.getcwd())
print("Current folder name   :", current_dir)   # Output: Current folder name   : BCA-Codes (varies by run location)

# Python runtime version
python_ver = sys.version.split()[0]
print("Python Version        :", python_ver)    # Output: (e.g. 3.13.x, varies by system)



"""
===========================
Expected Output:
===========================
--- 1. Using Custom Module (my_calculator.py) ---
Addition using module : 15
Multiply using module : 50

--- 2. Built-in Math and Random Modules ---
Square root of 36     : 6.0
Value of Pi           : 3.141592653589793
Random Number (1-10)  : 7

--- 3. Built-in Datetime Module ---
Today's Date          : 2026-08-15

--- 4. Built-in OS and SYS Modules ---
Current folder name   : BCA-Codes
Python Version        : 3.13.6
===========================
Note: Random number, date, and Python version will vary on execution.
"""
