"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 2 - Basic of Python Programming
Program Name : 03_tuple_operations.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates Python Tuple operations: immutability,
               concatenation, repetition, membership, iteration, and methods.
===================================================================
"""

# Creating a tuple (using fruit names as requested in previous practicals)
fruits = ("Mango", "Apple", "Banana", "Apple", "Orange")
print("Fruits Tuple :", fruits)

# Tuple Immutability
print("\n--- Tuple Immutability ---")
print("Tuples cannot be modified once created. Attempting to change an element will cause an error.")
print("Example: fruits[0] = 'Cherry' (This raises TypeError)")

# Tuple Operations
print("\n--- Tuple Operations ---")
t1 = (1, 2)
t2 = (3, 4)

# Concatenation
t3 = t1 + t2
print("Concatenation (t1 + t2) :", t3)

# Repetition
print("Repetition (t1 * 3)     :", t1 * 3)

# Membership
print("Is 'Mango' in fruits?   :", "Mango" in fruits)
print("Is 'Grapes' in fruits?  :", "Grapes" in fruits)

# Iteration / Traversing
print("\n--- Traversing Tuple using Loop ---")
for fruit in fruits:
    print("Fruit Name :", fruit)

# Tuple Methods
print("\n--- Tuple Methods ---")
# count()
print("Count of 'Apple' :", fruits.count("Apple"))

# index()
print("Index of 'Banana':", fruits.index("Banana"))


"""
===========================
Expected Output:
===========================
Fruits Tuple : ('Mango', 'Apple', 'Banana', 'Apple', 'Orange')

--- Tuple Immutability ---
Tuples cannot be modified once created. Attempting to change an element will cause an error.
Example: fruits[0] = 'Cherry' (This raises TypeError)

--- Tuple Operations ---
Concatenation (t1 + t2) : (1, 2, 3, 4)
Repetition (t1 * 3)     : (1, 2, 1, 2, 1, 2)
Is 'Mango' in fruits?   : True
Is 'Grapes' in fruits?  : False

--- Traversing Tuple using Loop ---
Fruit Name : Mango
Fruit Name : Apple
Fruit Name : Banana
Fruit Name : Apple
Fruit Name : Orange

--- Tuple Methods ---
Count of 'Apple' : 2
Index of 'Banana': 2
===========================
"""
