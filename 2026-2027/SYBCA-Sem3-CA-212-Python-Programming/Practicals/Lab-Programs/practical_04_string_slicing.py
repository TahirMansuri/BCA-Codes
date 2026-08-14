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

print("=== String Slicing Demonstration ===")

full_name = "Tahir Husen Najir Mansuri"
print("Original String :", full_name)
print("Length of String :", len(full_name))

print("\n--- Basic Slicing [start:stop] ---")
print("First Name [0:5] :", full_name[0:5])
print("Last Name  [18:] :", full_name[18:])

print("\n--- Slicing with Step [start:stop:step] ---")
print("Every 2nd char [0::2] :", full_name[0::2])

print("\n--- Negative Indexing ---")
print("Last 7 chars [-7:] :", full_name[-7:])

# Negative step reverses the string
print("\n--- Reversing a String ---")
print("Reversed [::-1] :", full_name[::-1])


"""
===========================
Expected Output:
===========================
=== String Slicing Demonstration ===
Original String : Tahir Husen Najir Mansuri
Length of String : 25

--- Basic Slicing [start:stop] ---
First Name [0:5] : Tahir
Last Name  [18:] : Mansuri

--- Slicing with Step [start:stop:step] ---
Every 2nd char [0::2] : Ti ueNjrMnui

--- Negative Indexing ---
Last 7 chars [-7:] : Mansuri

--- Reversing a String ---
Reversed [::-1] : irunsaM rjaN nesuH rihaT
===========================
"""
