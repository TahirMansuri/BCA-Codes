"""
===================================================================
Assignment   : Assignment 01 - Python Basics (SYBCA Sem-III)
Question 01  : Temperature Converter (Celsius <-> Fahrenheit)
Institution  : IMRD, Shahada
===================================================================
"""

print("=== Temperature Converter ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Result:", celsius, "degrees Celsius =", fahrenheit, "degrees Fahrenheit")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Result:", fahrenheit, "degrees Fahrenheit =", celsius, "degrees Celsius")
else:
    print("Invalid choice! Please select 1 or 2.")
