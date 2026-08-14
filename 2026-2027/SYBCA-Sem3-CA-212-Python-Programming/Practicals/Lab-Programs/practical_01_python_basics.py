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

print("Hello World!")
print("Welcome to Python Programming at IMRD, Shahada.")

print("\n--- Student Details ---")
student_name = "Amit Sharma"
roll_number = 101
print("Student Name:", student_name)
print("Roll Number :", roll_number)

print("\n--- Shopping Bill Calculation ---")
item1_price = 150.50
item2_price = 300.00
item3_price = 50.25

total_bill = item1_price + item2_price + item3_price
print("Item 1 Price : Rs.", item1_price)
print("Item 2 Price : Rs.", item2_price)
print("Item 3 Price : Rs.", item3_price)
print("---------------------------")
print("Total Bill   : Rs.", total_bill)

# Applying 10% discount
discount = total_bill * 0.10
final_amount = total_bill - discount

print("Discount(10%): Rs.", discount)
print("Final Amount : Rs.", final_amount)


"""
===========================
Expected Output:
===========================
Hello World!
Welcome to Python Programming at IMRD, Shahada.

--- Student Details ---
Student Name: Amit Sharma
Roll Number : 101

--- Shopping Bill Calculation ---
Item 1 Price : Rs. 150.5
Item 2 Price : Rs. 300.0
Item 3 Price : Rs. 50.25
---------------------------
Total Bill   : Rs. 500.75
Discount(10%): Rs. 50.075
Final Amount : Rs. 450.675
===========================
"""
