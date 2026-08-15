"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 1 - Introduction to Python
Program Name : 04_flow_control_conditionals.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates conditional control flow:
               1. Simple if statement
               2. if - else statement
               3. if - elif - else ladder (Student Grade System)
               4. Nested if statement
===================================================================
"""

print("=== Student Grade & Result System ===")

# Example trace: if user enters 80:
marks = float(input("Enter student overall marks (0 - 100): "))

# 1. Validation using Nested If
if 0 <= marks <= 100:
    print("Valid marks entered. Evaluating grade...")                 # Output (for 80): Valid marks entered. Evaluating grade...
    
    # 2. if-elif-else ladder
    if marks >= 75:
        grade = "Distinction (A+)"
    elif marks >= 60:
        grade = "First Class (A)"
    elif marks >= 50:
        grade = "Second Class (B)"
    elif marks >= 40:
        grade = "Pass Class (C)"
    else:
        grade = "Fail (F)"
        
    print("Student Result:", grade)                                    # Output (for 80): Student Result: Distinction (A+)
    
    # 3. Simple if & if-else
    if marks >= 40:
        print("Status: Eligible for Next Semester!")                  # Output (for 80): Status: Eligible for Next Semester!
    else:
        print("Status: Needs to appear for Remedial Exam.")
else:
    print("Error: Invalid marks! Please enter a value between 0 and 100.")
