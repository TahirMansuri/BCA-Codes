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
print("Single Line String :", single_line)
print("Multiline String   :")
print(multiline)

# Indexing and Slicing
print("\n--- Indexing and Slicing ---")
word = "Python"
print("Word             :", word)
print("First character  :", word[0])
print("Last character   :", word[-1])
print("Slice [0:4]      :", word[0:4])
print("Slice [2:]       :", word[2:])

# String Methods
print("\n--- String Methods ---")
text = "  Python Programming Language  "
print("Original Text :", text)

# lower() and upper()
print("Lowercase     :", text.lower())
print("Uppercase     :", text.upper())

# strip() to remove whitespaces
stripped_text = text.strip()
print("Stripped      :", stripped_text)

# count() of a character or substring
print("Count of 'n'  :", stripped_text.count("n"))

# find() and index() to search
print("Find 'Pro'    :", stripped_text.find("Pro"))
print("Index of 'P'  :", stripped_text.index("P"))

# replace() to replace a substring
print("Replace 'Language' with 'Code':", stripped_text.replace("Language", "Code"))


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
