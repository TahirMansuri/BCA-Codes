"""
===================================================================
Practical No : Practical 03
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to print "n" terms of Fibonacci Series 
               using Iteration.
===================================================================
"""

print("=== Fibonacci Series Generator ===")
print("The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers.")
print("Example: 0, 1, 1, 2, 3, 5, 8, 13...\n")

# Taking input for number of terms
n_terms = int(input("How many terms of the Fibonacci series do you want to print? "))

# Initializing the first two terms
n1 = 0
n2 = 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print(f"Fibonacci sequence up to {n_terms} term:")
    print(n1)
else:
    print(f"\nFibonacci sequence up to {n_terms} terms:")
    # Iteration to generate the series
    while count < n_terms:
        print(n1, end="  ")
        
        # Update values
        nth = n1 + n2
        n1 = n2
        n2 = nth
        
        count += 1

print("\n\nProgram execution completed.")
