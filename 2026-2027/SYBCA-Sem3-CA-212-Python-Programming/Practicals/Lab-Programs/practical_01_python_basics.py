"""
===================================================================
Practical No : Practical 01
Course Code  : CA - 212 (Python Programming Practical)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Aim          : Calculate Simple Interest and Total Maturity Amount
               using user inputs, type casting, and formatted output.
===================================================================
"""

# Accepting User Input
principal = float(input("Enter Principal Amount (Rs): "))
rate = float(input("Enter Annual Interest Rate (%): "))
time_years = float(input("Enter Time Period (in years): "))

# Mathematical Calculation
simple_interest = (principal * rate * time_years) / 100
total_amount = principal + simple_interest

# Formatted Output Display
print("\n" + "=" * 40)
print("     IMRD SHAHADA - PRACTICAL 01 OUTPUT")
print("=" * 40)
print(f"Principal Amount : Rs. {principal:,.2f}")
print(f"Interest Rate    : {rate}% per annum")
print(f"Time Period      : {time_years} years")
print("-" * 40)
print(f"Simple Interest  : Rs. {simple_interest:,.2f}")
print(f"Total Amount     : Rs. {total_amount:,.2f}")
print("=" * 40)
