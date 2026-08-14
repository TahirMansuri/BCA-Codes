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

print("=== Method Overloading Demonstration ===\n")
print("Note: Python does not support method overloading by default like Java or C++.")
print("However, we can achieve it using default arguments or variable-length arguments (*args).\n")

class MathOperations:
    
    # 1. Overloading using default arguments
    def add(self, a=0, b=0, c=0):
        """This method acts differently based on how many arguments are passed."""
        return a + b + c
    
    # 2. Overloading using variable-length arguments (*args)
    def multiply(self, *args):
        """This method can take any number of arguments and multiply them."""
        result = 1
        # If no arguments passed, return 0
        if len(args) == 0:
            return 0
            
        for num in args:
            result *= num
        return result

# Create an object of the class
calc = MathOperations()

print("--- 1. Overloading using Default Arguments ---")
# Calling add() with different numbers of arguments
print(f"Calling add() with 0 arguments        : {calc.add()}")
print(f"Calling add(10) with 1 argument       : {calc.add(10)}")
print(f"Calling add(10, 20) with 2 arguments  : {calc.add(10, 20)}")
print(f"Calling add(10, 20, 30) with 3 args   : {calc.add(10, 20, 30)}")

print("\n--- 2. Overloading using *args ---")
# Calling multiply() with different numbers of arguments
print(f"Calling multiply(5, 4)                : {calc.multiply(5, 4)}")
print(f"Calling multiply(2, 3, 4, 5)          : {calc.multiply(2, 3, 4, 5)}")
print(f"Calling multiply()                    : {calc.multiply()}")
