"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 2 - Basic of Python Programming
Program Name : 01_string_operations_and_methods.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates string operations: literals, indexing,
               slicing, and string methods.
===================================================================
"""

# String literals and multiline string
single_line = "Welcome to IMRD Shahada"
multiline = """This is a multiline string.
It can span multiple lines.
We are learning Python Programming."""

print("--- String Literals ---")
print("Single Line String :", single_line)  # Output: Welcome to IMRD Shahada
print("Multiline String   :")
print(multiline)
# Output of multiline print:
# This is a multiline string.
# It can span multiple lines.
# We are learning Python Programming.

# Indexing and Slicing
print("\n--- Indexing and Slicing ---")
word = "Python"
print("Word             :", word)          # Output: Python
print("First character  :", word[0])       # Output: P
print("Last character   :", word[-1])      # Output: n
print("Slice [0:4]      :", word[0:4])     # Output: Pyth
print("Slice [2:]       :", word[2:])      # Output: thon

# String Methods
print("\n--- String Methods ---")
text = "  Python Programming Language  "
print("Original Text :", text)             # Output:   Python Programming Language  

# lower() and upper()
print("Lowercase     :", text.lower())     # Output:   python programming language  
print("Uppercase     :", text.upper())     # Output:   PYTHON PROGRAMMING LANGUAGE  

# strip() to remove whitespaces
stripped_text = text.strip()
print("Stripped      :", stripped_text)     # Output: Python Programming Language

# count() of a character or substring
print("Count of 'n'  :", stripped_text.count("n"))  # Output: 3

# find() and index() to search
print("Find 'Pro'    :", stripped_text.find("Pro"))  # Output: 7
print("Index of 'P'  :", stripped_text.index("P"))  # Output: 0

# replace() to replace a substring
print("Replace 'Language' with 'Code':", stripped_text.replace("Language", "Code"))  # Output: Python Programming Code


"""
===========================
Expected Output:
===========================
--- String Literals ---
Single Line String : Welcome to IMRD Shahada
Multiline String   :
This is a multiline string.
It can span multiple lines.
We are learning Python Programming.

--- Indexing and Slicing ---
Word             : Python
First character  : P
Last character   : n
Slice [0:4]      : Pyth
Slice [2:]       : thon

--- String Methods ---
Original Text :   Python Programming Language  
Lowercase     :   python programming language  
Uppercase     :   PYTHON PROGRAMMING LANGUAGE  
Stripped      : Python Programming Language
Count of 'n'  : 3
Find 'Pro'    : 7
Index of 'P'  : 0
Replace 'Language' with 'Code': Python Programming Code
===========================
"""
