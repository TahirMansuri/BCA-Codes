"""
===================================================================
Practical No : Practical 03
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to print "n" terms of Fibonacci 
               Series using Iteration.
===================================================================
"""

print("=== Fibonacci Series Generator ===")
print("Fibonacci: Each number is sum of the previous two numbers.")
print("Example: 0, 1, 1, 2, 3, 5, 8, 13 ...")

n_terms = int(input("\nHow many terms do you want? "))

n1 = 0
n2 = 1
count = 0

if n_terms <= 0:
    print("Please enter a positive number.")
elif n_terms == 1:
    print(n1)
else:
    print("Fibonacci Series:")
    while count < n_terms:
        print(n1, end="  ")
        # Calculate next term
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1

print("\nDone.")


"""
===========================
Expected Output:
===========================
=== Fibonacci Series Generator ===
Fibonacci: Each number is sum of the previous two numbers.
Example: 0, 1, 1, 2, 3, 5, 8, 13 ...

How many terms do you want? 8
Fibonacci Series:
0  1  1  2  3  5  8  13  
Done.
===========================
"""
