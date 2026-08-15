"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 3 - Python Functions and Modules
Program Name : 01_function_arguments_and_scope.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates functions, argument types (positional, default,
               keyword, *args, **kwargs), return values, and local vs global scope.
===================================================================
"""

# Global variable
college = "IMRD"

# 1. Simple function with positional and default arguments
def greet_student(name, course = "BCA"):
    print("Welcome", name, "from course", course)

# 2. Function with return value
def add_numbers(x, y):
    return x + y

# 3. Variable-length arguments (*args and **kwargs)
def print_hobbies(*args):
    print("Hobbies are :", args)

def print_student_info(**kwargs):
    print("Details :", kwargs)

# 4. Local vs Global Scope
def show_scope():
    # Local variable
    city = "Shahada"
    print("Inside function - Local city    :", city)
    print("Inside function - Global college:", college)

print("--- 1. Basic Function Call & Arguments ---")
greet_student("Amit")                          # Output: Welcome Amit from course BCA
greet_student("Priya", "MCA")                  # Output: Welcome Priya from course MCA

# Keyword arguments
greet_student(course = "BBA", name = "Rahul")  # Output: Welcome Rahul from course BBA

print("\n--- 2. Function with Return Value ---")
result = add_numbers(15, 25)
print("Result of addition :", result)          # Output: Result of addition : 40

print("\n--- 3. Variable-Length Arguments ---")
print_hobbies("Cricket", "Music", "Reading")  # Output: Hobbies are : ('Cricket', 'Music', 'Reading')
print_student_info(roll_no = 101, city = "Shahada", grade = "A")
# Output: Details : {'roll_no': 101, 'city': 'Shahada', 'grade': 'A'}

print("\n--- 4. Local vs Global Scope ---")
show_scope()
# Output of show_scope():
# Inside function - Local city    : Shahada
# Inside function - Global college: IMRD

print("Outside function - Global college:", college)  # Output: Outside function - Global college: IMRD


"""
===========================
Expected Output:
===========================
--- 1. Basic Function Call & Arguments ---
Welcome Amit from course BCA
Welcome Priya from course MCA
Welcome Rahul from course BBA

--- 2. Function with Return Value ---
Result of addition : 40

--- 3. Variable-Length Arguments ---
Hobbies are : ('Cricket', 'Music', 'Reading')
Details : {'roll_no': 101, 'city': 'Shahada', 'grade': 'A'}

--- 4. Local vs Global Scope ---
Inside function - Local city    : Shahada
Inside function - Global college: IMRD
Outside function - Global college: IMRD
===========================
"""
