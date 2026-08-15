"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 1 - Introduction to Python
Program Name : 06_break_continue_pass.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates loop control statements:
               1. break    - Terminates the loop immediately
               2. continue - Skips current iteration & moves to next
               3. pass     - Null statement / placeholder
===================================================================
"""

print("--- 1. 'break' Statement Demo ---")
print("Searching for number 5 in range 1 to 10:")
for i in range(1, 11):
    if i == 5:
        print("Target", i, "found! Breaking out of loop.")            # Output: Target 5 found! Breaking out of loop.
        break
    print("Checking:", i)
# Output of Loop:
# Checking: 1
# Checking: 2
# Checking: 3
# Checking: 4

print("\n--- 2. 'continue' Statement Demo ---")
print("Printing numbers from 1 to 10 except multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        continue # Skip printing for multiples of 3
    print(i, end=" ")                                                 # Output: 1 2 4 5 7 8 10 
print()

print("\n--- 3. 'pass' Statement Demo ---")
for i in range(1, 6):
    if i == 3:
        pass  # Syntactic placeholder
        print("Encountered", i, "- passed without alteration.")       # Output: Encountered 3 - passed without alteration.
    else:
        print("Processing item", i)
# Output of Loop:
# Processing item 1
# Processing item 2
# Processing item 4
# Processing item 5
