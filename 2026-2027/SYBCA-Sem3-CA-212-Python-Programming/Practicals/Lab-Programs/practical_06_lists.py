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

print("=== List and Related Functions ===\n")

# Daily Example: Managing a list of subjects for a student
subjects = ["Python", "Data Structures", "Accounting"]
print(f"Initial List of Subjects: {subjects}")

print("\n--- 1. Adding Elements ---")
# append() adds an item to the end of the list
subjects.append("Ethical Hacking")
print(f"After append('Ethical Hacking') : {subjects}")

# insert() adds an item at a specific index
subjects.insert(1, "Web Technologies")
print(f"After insert(1, 'Web Tech')   : {subjects}")

print("\n--- 2. Removing Elements ---")
# remove() removes the first matching value
subjects.remove("Accounting")
print(f"After remove('Accounting')    : {subjects}")

# pop() removes and returns the item at the given index (or last item if no index)
last_subject = subjects.pop()
print(f"After pop() [Removed '{last_subject}'] : {subjects}")

print("\n--- 3. List Information ---")
# len() gives the number of items
print(f"Total number of subjects: {len(subjects)}")

# index() finds the position of an item
print(f"Index of 'Python': {subjects.index('Python')}")

print("\n--- 4. Sorting and Reversing ---")
# sort() sorts the list alphabetically or numerically
subjects.sort()
print(f"Alphabetically Sorted List: {subjects}")

# reverse() reverses the order of the list
subjects.reverse()
print(f"Reversed List: {subjects}")
