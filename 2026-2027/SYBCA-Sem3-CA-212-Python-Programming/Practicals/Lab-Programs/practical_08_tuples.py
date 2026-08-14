"""
===================================================================
Practical No : Practical 08
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to demonstrate the use of Tuple.
===================================================================
"""

print("=== Tuple and its Operations ===")

# Tuple is immutable - values cannot be changed after creation
fruits = ("Mango", "Apple", "Banana", "Orange", "Grapes")
print("Fruits Tuple :", fruits)

print("\n--- Accessing Elements ---")
print("First Fruit  :", fruits[0])
print("Last Fruit   :", fruits[-1])
print("Second Fruit :", fruits[1])

print("\n--- Slicing a Tuple ---")
print("First 3 fruits  :", fruits[0:3])
print("Last 2 fruits   :", fruits[3:])

print("\n--- Tuple Unpacking ---")
(f1, f2, f3, f4, f5) = fruits
print("Unpacked - f1 :", f1, " f2 :", f2, " f3 :", f3)

print("\n--- Tuple Concatenation ---")
more_fruits = ("Pineapple", "Papaya")
all_fruits = fruits + more_fruits
print("Original Fruits  :", fruits)
print("Added Fruits     :", more_fruits)
print("All Fruits       :", all_fruits)

print("\n--- Built-in Tuple Methods ---")
sample = ("Mango", "Apple", "Mango", "Banana", "Mango")
print("Sample Tuple      :", sample)
print("Count of Mango    :", sample.count("Mango"))
print("Index of Apple    :", sample.index("Apple"))

print("\n--- Other Tuple Operations ---")
print("Total fruits      :", len(fruits))
print("Is Mango present? :", "Mango" in fruits)
print("Is Cherry present?:", "Cherry" in fruits)


"""
===========================
Expected Output:
===========================
=== Tuple and its Operations ===
Fruits Tuple : ('Mango', 'Apple', 'Banana', 'Orange', 'Grapes')

--- Accessing Elements ---
First Fruit  : Mango
Last Fruit   : Grapes
Second Fruit : Apple

--- Slicing a Tuple ---
First 3 fruits  : ('Mango', 'Apple', 'Banana')
Last 2 fruits   : ('Orange', 'Grapes')

--- Tuple Unpacking ---
Unpacked - f1 : Mango  f2 : Apple  f3 : Banana

--- Tuple Concatenation ---
Original Fruits  : ('Mango', 'Apple', 'Banana', 'Orange', 'Grapes')
Added Fruits     : ('Pineapple', 'Papaya')
All Fruits       : ('Mango', 'Apple', 'Banana', 'Orange', 'Grapes', 'Pineapple', 'Papaya')

--- Built-in Tuple Methods ---
Sample Tuple      : ('Mango', 'Apple', 'Mango', 'Banana', 'Mango')
Count of Mango    : 3
Index of Apple    : 1

--- Other Tuple Operations ---
Total fruits      : 5
Is Mango present? : True
Is Cherry present?: False
===========================
"""
