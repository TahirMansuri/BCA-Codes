"""
===================================================================
Practical No : Practical 02
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to find all prime numbers within a 
               given range.
===================================================================
"""

print("=== Prime Number Finder ===")

start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))

print("Prime numbers between", start_range, "and", end_range, "are:")

for num in range(start_range, end_range + 1):
    if num > 1:
        is_prime = True
        # Check if num has any factor other than 1 and itself
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end="  ")

print("\nDone.")


"""
===========================
Expected Output:
===========================
=== Prime Number Finder ===
Enter the starting number: 1
Enter the ending number: 30
Prime numbers between 1 and 30 are:
2  3  5  7  11  13  17  19  23  29  
Done.
===========================
"""
