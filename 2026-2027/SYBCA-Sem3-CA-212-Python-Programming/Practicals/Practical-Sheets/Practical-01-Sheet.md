# 📄 Practical Sheet 01: Python Fundamentals & Operators
**Course Code**: CA - 212 (Python Programming) | **Class**: SYBCA (Sem-III)  
**Academic Year**: 2026–2027 | **Institution**: IMRD, Shahada  

---

### 1. Aim:
Write a Python program to demonstrate standard data types, type casting, arithmetic calculations, and formatted output.

### 2. Objectives:
- To understand variable declaration and dynamic typing in Python.
- To practice taking input from user using `input()` and type conversion functions (`int()`, `float()`).
- To format console outputs using modern f-strings.

### 3. Algorithm:
- **Step 1**: Start.
- **Step 2**: Accept principal amount ($P$), rate of interest ($R$), and time period ($T$) in years from the user.
- **Step 3**: Convert input strings to floating point numbers.
- **Step 4**: Compute Simple Interest using formula: $SI = (P \times R \times T) / 100$.
- **Step 5**: Compute Total Maturity Amount using formula: $Total = P + SI$.
- **Step 6**: Display the calculated Simple Interest and Total Amount formatted up to 2 decimal places.
- **Step 7**: Stop.

---

### 4. Source Code:
*(Refer to executable file: [`../Lab-Programs/practical_01_python_basics.py`](../Lab-Programs/practical_01_python_basics.py))*

```python
# Simple Interest and Total Amount Calculator
principal = float(input("Enter Principal Amount (Rs): "))
rate = float(input("Enter Annual Interest Rate (%): "))
time_years = float(input("Enter Time Period (in years): "))

simple_interest = (principal * rate * time_years) / 100
total_amount = principal + simple_interest

print("\n--- Practical 01: Output Result ---")
print(f"Principal Amount : Rs. {principal:,.2f}")
print(f"Interest Rate    : {rate}% per annum")
print(f"Time Period      : {time_years} years")
print(f"Simple Interest  : Rs. {simple_interest:,.2f}")
print(f"Total Amount     : Rs. {total_amount:,.2f}")
```

---

### 5. Sample Input & Output:
```text
Enter Principal Amount (Rs): 50000
Enter Annual Interest Rate (%): 7.5
Enter Time Period (in years): 3

--- Practical 01: Output Result ---
Principal Amount : Rs. 50,000.00
Interest Rate    : 7.5% per annum
Time Period      : 3.0 years
Simple Interest  : Rs. 11,250.00
Total Amount     : Rs. 61,250.00
```

---

### 6. Viva Questions:
1. **Q**: What is dynamic typing in Python?  
   **A**: In Python, you do not need to explicitly declare variable types; the interpreter determines the type at runtime based on the assigned value.
2. **Q**: Why is `float(input())` required instead of just `input()`?  
   **A**: Because `input()` always returns user input as a string (`str`), so we must explicitly type-cast it to `float` for mathematical calculations.
3. **Q**: What is the difference between `/` and `//` operators in Python?  
   **A**: `/` performs standard float division (e.g. `7 / 2 = 3.5`), while `//` performs floor/integer division (e.g. `7 // 2 = 3`).
