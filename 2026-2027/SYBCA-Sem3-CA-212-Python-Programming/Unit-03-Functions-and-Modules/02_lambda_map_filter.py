"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 3 - Python Functions and Modules
Program Name : 02_lambda_map_filter.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates Lambda (anonymous) functions, and built-in
               higher-order functions map() and filter().
===================================================================
"""

print("--- 1. Lambda Functions ---")
# Lambda function to calculate square of a number
square = lambda x: x * x
print("Square of 5 is :", square(5))          # Output: Square of 5 is : 25

# Lambda function to add two numbers
add = lambda a, b: a + b
print("Sum of 10 & 20 :", add(10, 20))        # Output: Sum of 10 & 20 : 30

print("\n--- 2. map() Function ---")
# Double all numbers in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda val: val * 2, numbers))
print("Original List  :", numbers)            # Output: Original List  : [1, 2, 3, 4, 5]
print("Doubled List   :", doubled)            # Output: Doubled List   : [2, 4, 6, 8, 10]

print("\n--- 3. filter() Function ---")
# Filter out only even numbers from a list
original_list = [10, 15, 20, 25, 30, 35]
even_numbers = list(filter(lambda num: num % 2 == 0, original_list))
print("Original List  :", original_list)       # Output: Original List  : [10, 15, 20, 25, 30, 35]
print("Even Numbers   :", even_numbers)        # Output: Even Numbers   : [10, 20, 30]


"""
===========================
Expected Output:
===========================
--- 1. Lambda Functions ---
Square of 5 is : 25
Sum of 10 & 20 : 30

--- 2. map() Function ---
Original List  : [1, 2, 3, 4, 5]
Doubled List   : [2, 4, 6, 8, 10]

--- 3. filter() Function ---
Original List  : [10, 15, 20, 25, 30, 35]
Even Numbers   : [10, 20, 30]
===========================
"""
