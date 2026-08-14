"""
===================================================================
Practical No : Practical 07
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to demonstrate the use of Dictionary 
               & related functions.
===================================================================
"""

print("=== Dictionary and Related Functions ===\n")

# Daily Example: Storing a student's profile information (Key-Value pairs)
student_profile = {
    "roll_no": 105,
    "name": "Rohan Gupta",
    "course": "BCA",
    "grade": "A"
}

print(f"Initial Dictionary: {student_profile}")

print("\n--- 1. Accessing Values ---")
# Using the key to access a value
print(f"Student Name: {student_profile['name']}")
# Using get() method (safer, returns None if key doesn't exist)
print(f"Student Course: {student_profile.get('course')}")

print("\n--- 2. Adding and Updating Elements ---")
# Adding a new key-value pair
student_profile["city"] = "Shahada"
print(f"After adding 'city'  : {student_profile}")

# Updating an existing value
student_profile["grade"] = "A+"
print(f"After updating 'grade': {student_profile}")

print("\n--- 3. Removing Elements ---")
# pop() removes the item with the specified key and returns its value
removed_city = student_profile.pop("city")
print(f"After pop('city')    : {student_profile}")

print("\n--- 4. Dictionary Methods ---")
# keys() returns a list of all keys
print(f"All Keys: {student_profile.keys()}")

# values() returns a list of all values
print(f"All Values: {student_profile.values()}")

# items() returns a list of all key-value tuple pairs
print(f"All Items: {student_profile.items()}")

print("\n--- 5. Looping through a Dictionary ---")
for key, value in student_profile.items():
    print(f"{key.capitalize()}: {value}")
