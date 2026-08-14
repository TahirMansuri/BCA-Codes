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

# Taking range input from the user
start_range = int(input("Enter the starting number of the range: "))
end_range = int(input("Enter the ending number of the range: "))

print(f"\nPrime numbers between {start_range} and {end_range} are:")

# Loop through the given range
for num in range(start_range, end_range + 1):
    # A prime number is always greater than 1
    if num > 1:
        is_prime = True
        
        # Check for factors from 2 up to num-1
        # (Optimization: checking up to num // 2 or int(num**0.5) is better)
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break # Not a prime number, break the loop
                
        # If no factors found, it is prime
        if is_prime:
            print(num, end="  ")

print("\n\nProgram execution completed.")
