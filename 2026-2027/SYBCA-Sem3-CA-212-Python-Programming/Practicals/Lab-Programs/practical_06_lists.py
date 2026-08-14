"""
===================================================================
Practical No : Practical 06
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to demonstrate the use of list & 
               related functions.
===================================================================
"""

print("=== List and Related Functions ===")

subjects = ["Python", "Data Structures", "Accounting"]
print("Initial List :", subjects)

print("\n--- Adding Elements ---")
subjects.append("Ethical Hacking")
print("After append :", subjects)

subjects.insert(1, "Web Technologies")
print("After insert :", subjects)

print("\n--- Removing Elements ---")
subjects.remove("Accounting")
print("After remove :", subjects)

removed = subjects.pop()
print("Removed item :", removed)
print("After pop    :", subjects)

print("\n--- List Information ---")
print("Total subjects :", len(subjects))
print("Index of Python:", subjects.index("Python"))

print("\n--- Sorting and Reversing ---")
subjects.sort()
print("After sort    :", subjects)

subjects.reverse()
print("After reverse :", subjects)


"""
===========================
Expected Output:
===========================
=== List and Related Functions ===
Initial List : ['Python', 'Data Structures', 'Accounting']

--- Adding Elements ---
After append : ['Python', 'Data Structures', 'Accounting', 'Ethical Hacking']
After insert : ['Python', 'Web Technologies', 'Data Structures', 'Accounting', 'Ethical Hacking']

--- Removing Elements ---
After remove : ['Python', 'Web Technologies', 'Data Structures', 'Ethical Hacking']
Removed item : Ethical Hacking
After pop    : ['Python', 'Web Technologies', 'Data Structures']

--- List Information ---
Total subjects : 3
Index of Python: 0

--- Sorting and Reversing ---
After sort    : ['Data Structures', 'Python', 'Web Technologies']
After reverse : ['Web Technologies', 'Python', 'Data Structures']
===========================
"""
