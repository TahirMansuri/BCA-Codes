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
basic_salary = float(input("Enter Basic Salary (Rs): "))

# Allowances: HRA = 20%, DA = 40%
hra = 0.20 * basic_salary
da = 0.40 * basic_salary
gross_salary = basic_salary + hra + da

print("\n--- Salary Slip Summary ---")
print("Employee ID   :", emp_id)
print("Employee Name :", emp_name)
print("Basic Salary  : Rs.", basic_salary)
print("HRA (20%)     : Rs.", hra)
print("DA (40%)      : Rs.", da)
print("---------------------------")
print("Gross Salary  : Rs.", gross_salary)
