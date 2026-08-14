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

print("=== Class and Objects in Python ===")

class Student:
    college_name = "IMRD, Shahada"

    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
        print("Student Name :", self.name)
        print("Roll Number  :", self.roll_no)
        print("Course       :", self.course)
        print("College      :", Student.college_name)
        print("-" * 30)

# Creating objects of the Student class
student1 = Student("Amit Sharma", 101, "BCA")
student2 = Student("Priya Patel", 102, "BCA")

print("\nDetails of Student 1:")
student1.display_details()

print("Details of Student 2:")
student2.display_details()

# Modifying an object's property
student1.course = "MCA"
print("Updated Details of Student 1:")
student1.display_details()


"""
===========================
Expected Output:
===========================
=== Class and Objects in Python ===

Details of Student 1:
Student Name : Amit Sharma
Roll Number  : 101
Course       : BCA
College      : IMRD, Shahada
------------------------------

Details of Student 2:
Student Name : Priya Patel
Roll Number  : 102
Course       : BCA
College      : IMRD, Shahada
------------------------------

Updated Details of Student 1:
Student Name : Amit Sharma
Roll Number  : 101
Course       : MCA
College      : IMRD, Shahada
------------------------------
===========================
"""
