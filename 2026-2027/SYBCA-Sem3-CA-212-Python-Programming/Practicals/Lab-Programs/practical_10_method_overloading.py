"""
===================================================================
Practical No : Practical 10
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to demonstrate the working of 
               Overloading Methods.
===================================================================
"""

print("=== Method Overloading in Python ===")
print("Python achieves method overloading using default arguments or *args.")

class MathOperations:

    # Using default arguments to simulate overloading
    def add(self, a = 0, b = 0, c = 0):
        return a + b + c

    # Using *args to accept any number of arguments
    def multiply(self, *args):
        result = 1
        if len(args) == 0:
            return 0
        for num in args:
            result = result * num
        return result

calc = MathOperations()

print("\n--- add() with different number of arguments ---")
print("add()         :", calc.add())
print("add(10)       :", calc.add(10))
print("add(10, 20)   :", calc.add(10, 20))
print("add(10,20,30) :", calc.add(10, 20, 30))

print("\n--- multiply() with *args ---")
print("multiply(5, 4)       :", calc.multiply(5, 4))
print("multiply(2, 3, 4, 5) :", calc.multiply(2, 3, 4, 5))
print("multiply()           :", calc.multiply())


"""
===========================
Expected Output:
===========================
=== Method Overloading in Python ===
Python achieves method overloading using default arguments or *args.

--- add() with different number of arguments ---
add()         : 0
add(10)       : 10
add(10, 20)   : 30
add(10,20,30) : 60

--- multiply() with *args ---
multiply(5, 4)       : 20
multiply(2, 3, 4, 5) : 120
multiply()           : 0
===========================
"""
