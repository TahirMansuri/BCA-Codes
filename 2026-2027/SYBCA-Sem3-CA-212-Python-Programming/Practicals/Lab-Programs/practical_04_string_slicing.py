"""
===================================================================
Practical No : Practical 04
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to demonstrate the use of slicing 
               in string.
===================================================================
"""

print("=== String Slicing Demonstration ===\n")

# Daily Example: Processing a full name and extracting parts
full_name = "Tahir Husen Najir Mansuri"
print(f"Original String: '{full_name}'")
print(f"Length of String: {len(full_name)} characters\n")

print("--- 1. Basic Slicing [start:stop] ---")
# Extracting the first name (from index 0 to 4)
first_name = full_name[0:5] 
print(f"First Name [0:5] : {first_name}")

# Extracting the last name (from index 18 to the end)
last_name = full_name[18:] 
print(f"Last Name [18:]  : {last_name}")

print("\n--- 2. Slicing with Step [start:stop:step] ---")
# Skipping characters (step = 2)
skip_chars = full_name[0::2]
print(f"Every 2nd char [0::2] : {skip_chars}")

print("\n--- 3. Negative Indexing and Slicing ---")
# Extracting the last 7 characters
negative_slice = full_name[-7:]
print(f"Last 7 chars [-7:] : {negative_slice}")

print("\n--- 4. Reversing a String ---")
# Using a negative step to reverse the string
reversed_string = full_name[::-1]
print(f"Reversed String [::-1] : {reversed_string}")
