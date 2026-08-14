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
coordinates = (21.5451, 74.4716)
print("Shahada Coordinates :", coordinates)

print("\n--- Accessing Elements ---")
print("Latitude  :", coordinates[0])
print("Longitude :", coordinates[1])

print("\n--- Tuple Unpacking ---")
(lat, lon) = coordinates
print("Unpacked Lat :", lat)
print("Unpacked Lon :", lon)

print("\n--- Tuple Concatenation ---")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Tuple 1    :", tuple1)
print("Tuple 2    :", tuple2)
print("Combined   :", combined)

print("\n--- Built-in Tuple Methods ---")
sample = (10, 20, 30, 20, 40, 20)
print("Sample Tuple   :", sample)
print("Count of 20    :", sample.count(20))
print("Index of 30    :", sample.index(30))


"""
===========================
Expected Output:
===========================
=== Tuple and its Operations ===
Shahada Coordinates : (21.5451, 74.4716)

--- Accessing Elements ---
Latitude  : 21.5451
Longitude : 74.4716

--- Tuple Unpacking ---
Unpacked Lat : 21.5451
Unpacked Lon : 74.4716

--- Tuple Concatenation ---
Tuple 1    : (1, 2, 3)
Tuple 2    : (4, 5, 6)
Combined   : (1, 2, 3, 4, 5, 6)

--- Built-in Tuple Methods ---
Sample Tuple   : (10, 20, 30, 20, 40, 20)
Count of 20    : 3
Index of 30    : 2
===========================
"""
