"""
===================================================================
Practical No : Practical 01
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Simple statements like printing names ("Hello World"), 
               numbers, mathematical calculations, etc.
===================================================================
"""

# 1. Printing Names and "Hello World"
print("Hello World!")
print("Welcome to Python Programming at IMRD, Shahada.")

print("\n--- Student Details ---")
student_name = "Amit Sharma"
roll_number = 101
print("Student Name:", student_name)
print("Roll Number:", roll_number)

# 2. Printing Numbers
print("\n--- Numbers ---")
age = 20
height = 5.8
print("Age:", age)
print("Height:", height)

# 3. Simple Mathematical Calculations (Daily Example: Shopping Bill)
print("\n--- Shopping Bill Calculation ---")
item1_price = 150.50
item2_price = 300.00
item3_price = 50.25

# Calculating total
total_bill = item1_price + item2_price + item3_price
print(f"Item 1 Price: Rs. {item1_price}")
print(f"Item 2 Price: Rs. {item2_price}")
print(f"Item 3 Price: Rs. {item3_price}")

print("-" * 25)
print(f"Total Bill Amount: Rs. {total_bill}")

# Applying a discount of 10%
discount = total_bill * 0.10
final_amount = total_bill - discount

print(f"Discount (10%)   : Rs. {discount}")
print(f"Final Amount Pay : Rs. {final_amount}")
print("=" * 25)
