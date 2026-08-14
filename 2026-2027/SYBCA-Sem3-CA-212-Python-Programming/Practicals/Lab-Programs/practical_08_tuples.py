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

print("=== Tuple and its Operations ===\n")

# Daily Example: Storing geographic coordinates (Latitude, Longitude) 
# Tuples are immutable (cannot be changed after creation), perfect for fixed data
shahada_coordinates = (21.5451, 74.4716)
print(f"Shahada Coordinates (Tuple): {shahada_coordinates}")

print("\n--- 1. Accessing Tuple Elements ---")
latitude = shahada_coordinates[0]
longitude = shahada_coordinates[1]
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

print("\n--- 2. Tuple Unpacking ---")
# We can assign tuple values directly to variables
(lat, lon) = shahada_coordinates
print(f"Unpacked Lat: {lat}, Lon: {lon}")

print("\n--- 3. Tuple Concatenation ---")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Concatenated Tuple: {combined_tuple}")

print("\n--- 4. Built-in Tuple Methods ---")
sample_tuple = (10, 20, 30, 20, 40, 20)
print(f"Sample Tuple: {sample_tuple}")

# count() returns the number of times a value appears in the tuple
print(f"Number of times '20' appears: {sample_tuple.count(20)}")

# index() finds the first occurrence of a specified value
print(f"Index of '30' is: {sample_tuple.index(30)}")

print("\nNote: Tuples do not have methods like append(), remove() because they are immutable.")
