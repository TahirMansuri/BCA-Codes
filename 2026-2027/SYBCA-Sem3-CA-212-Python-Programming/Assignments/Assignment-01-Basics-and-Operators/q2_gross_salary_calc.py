"""
===================================================================
Assignment   : Assignment 01 - Python Basics (SYBCA Sem-III)
Question 02  : Employee Gross Salary Calculator
Institution  : IMRD, Shahada
===================================================================
"""

print("=== Employee Gross Salary Calculation ===")

emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary (₹): "))

# Allowances: HRA = 20%, DA = 40%
hra = 0.20 * basic_salary
da = 0.40 * basic_salary
gross_salary = basic_salary + hra + da

print("\n--- Salary Slip Summary ---")
print(f"Employee ID   : {emp_id}")
print(f"Employee Name : {emp_name}")
print(f"Basic Salary  : ₹{basic_salary:.2f}")
print(f"HRA (20%)     : ₹{hra:.2f}")
print(f"DA (40%)      : ₹{da:.2f}")
print("---------------------------")
print(f"Gross Salary  : ₹{gross_salary:.2f}")
