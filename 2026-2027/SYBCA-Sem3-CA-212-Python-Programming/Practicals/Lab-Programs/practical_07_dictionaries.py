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

print("=== Dictionary and Related Functions ===")

student_profile = {
    "roll_no": 105,
    "name": "Rohan Gupta",
    "course": "BCA",
    "grade": "A"
}

print("Student Profile :", student_profile)

print("\n--- Accessing Values ---")
print("Student Name   :", student_profile["name"])
print("Student Course :", student_profile.get("course"))

print("\n--- Adding and Updating ---")
student_profile["city"] = "Shahada"
print("After adding city  :", student_profile)

student_profile["grade"] = "A+"
print("After updating grade:", student_profile)

print("\n--- Removing Elements ---")
student_profile.pop("city")
print("After pop city     :", student_profile)

print("\n--- Dictionary Methods ---")
print("Keys   :", student_profile.keys())
print("Values :", student_profile.values())
print("Items  :", student_profile.items())

print("\n--- Looping through Dictionary ---")
for key, value in student_profile.items():
    print(key, ":", value)


"""
===========================
Expected Output:
===========================
=== Dictionary and Related Functions ===
Student Profile : {'roll_no': 105, 'name': 'Rohan Gupta', 'course': 'BCA', 'grade': 'A'}

--- Accessing Values ---
Student Name   : Rohan Gupta
Student Course : BCA

--- Adding and Updating ---
After adding city  : {'roll_no': 105, 'name': 'Rohan Gupta', 'course': 'BCA', 'grade': 'A', 'city': 'Shahada'}
After updating grade: {'roll_no': 105, 'name': 'Rohan Gupta', 'course': 'BCA', 'grade': 'A+', 'city': 'Shahada'}

--- Removing Elements ---
After pop city     : {'roll_no': 105, 'name': 'Rohan Gupta', 'course': 'BCA', 'grade': 'A+'}

--- Dictionary Methods ---
Keys   : dict_keys(['roll_no', 'name', 'course', 'grade'])
Values : dict_values([105, 'Rohan Gupta', 'BCA', 'A+'])
Items  : dict_items([('roll_no', 105), ('name', 'Rohan Gupta'), ('course', 'BCA'), ('grade', 'A+')])

--- Looping through Dictionary ---
roll_no : 105
name : Rohan Gupta
course : BCA
grade : A+
===========================
"""
