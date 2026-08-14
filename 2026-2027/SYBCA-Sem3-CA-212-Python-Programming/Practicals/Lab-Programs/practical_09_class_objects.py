"""
===================================================================
Practical No : Practical 09
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to demonstrate the working of Class 
               and Objects.
===================================================================
"""

print("=== Class and Objects in Python ===\n")

# 1. Defining a Class
class Student:
    # Class Attribute (shared by all objects)
    college_name = "IMRD, Shahada"

    # Constructor method to initialize attributes when an object is created
    def __init__(self, name, roll_no, course):
        # Instance Attributes (unique to each object)
        self.name = name
        self.roll_no = roll_no
        self.course = course

    # Instance Method
    def display_details(self):
        print(f"Student Name : {self.name}")
        print(f"Roll Number  : {self.roll_no}")
        print(f"Course       : {self.course}")
        print(f"College      : {Student.college_name}")
        print("-" * 30)

# 2. Creating Objects (Instances) of the Class
print("Creating objects for 2 students...\n")

student1 = Student("Amit Sharma", 101, "BCA")
student2 = Student("Priya Patel", 102, "BCA")

# 3. Accessing methods through objects
print("Details of Student 1:")
student1.display_details()

print("Details of Student 2:")
student2.display_details()

# 4. Modifying object properties
print("Updating Amit's course to MCA...\n")
student1.course = "MCA"

print("Updated Details of Student 1:")
student1.display_details()
