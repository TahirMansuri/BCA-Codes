"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 2 - Basic of Python Programming
Program Name : 02_list_manipulations_and_methods.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates Python List operations: creation, slicing,
               traversing, concatenation, list methods, and functions.
===================================================================
"""

# Creating and initializing lists
numbers = [10, 20, 30, 40, 50]
names = ["Amit", "Priya", "Rahul"]

print("--- Initial Lists ---")
print("Numbers List :", numbers)
print("Names List   :", names)

# Accessing and Traversing
print("\n--- Accessing & Traversing ---")
print("First element of numbers :", numbers[0])
print("Last element of numbers  :", numbers[-1])

print("Traversing names list using loop:")
for name in names:
    print("Hello", name)

# List Operations
print("\n--- List Operations ---")
list_a = [1, 2]
list_b = [3, 4]
print("Concatenation (list_a + list_b) :", list_a + list_b)
print("Repetition (list_a * 3)         :", list_a * 3)
print("List Slicing (numbers[1:4])     :", numbers[1:4])

# List Methods
print("\n--- List Methods ---")
my_list = [20, 10, 40, 30]
print("Original my_list :", my_list)

# append() and extend()
my_list.append(50)
print("After append(50)  :", my_list)

my_list.extend([60, 70])
print("After extend()    :", my_list)

# insert()
my_list.insert(1, 15)
print("After insert(1,15):", my_list)

# remove() and pop()
my_list.remove(40)
print("After remove(40)  :", my_list)

popped_val = my_list.pop()
print("Popped value      :", popped_val)
print("After pop()       :", my_list)

# sort() and reverse()
my_list.sort()
print("After sort()      :", my_list)

my_list.reverse()
print("After reverse()   :", my_list)

# Built-in Functions
print("\n--- List Built-in Functions ---")
scores = [10, 20, 30, 40]
print("Scores List :", scores)
print("Length      :", len(scores))
print("Maximum     :", max(scores))
print("Minimum     :", min(scores))
print("Sum         :", sum(scores))


"""
===========================
Expected Output:
===========================
--- Initial Lists ---
Numbers List : [10, 20, 30, 40, 50]
Names List   : ['Amit', 'Priya', 'Rahul']

--- Accessing & Traversing ---
First element of numbers : 10
Last element of numbers  : 50
Traversing names list using loop:
Hello Amit
Hello Priya
Hello Rahul

--- List Operations ---
Concatenation (list_a + list_b) : [1, 2, 3, 4]
Repetition (list_a * 3)         : [1, 2, 1, 2, 1, 2]
List Slicing (numbers[1:4])     : [20, 30, 40]

--- List Methods ---
Original my_list : [20, 10, 40, 30]
After append(50)  : [20, 10, 40, 30, 50]
After extend()    : [20, 10, 40, 30, 50, 60, 70]
After insert(1,15): [20, 15, 10, 40, 30, 50, 60, 70]
After remove(40)  : [20, 15, 10, 30, 50, 60, 70]
Popped value      : 70
After pop()       : [20, 15, 10, 30, 50, 60]
After sort()      : [10, 15, 20, 30, 50, 60]
After reverse()   : [60, 50, 30, 20, 15, 10]

--- List Built-in Functions ---
Scores List : [10, 20, 30, 40]
Length      : 4
Maximum     : 40
Minimum     : 10
Sum         : 100
===========================
"""
