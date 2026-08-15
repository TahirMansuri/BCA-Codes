"""
===================================================================
Course Code  : CA - 212 (Python Programming)
Subject      : Unit 2 - Basic of Python Programming
Program Name : 04_dictionary_operations_and_methods.py
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
Description  : Demonstrates Python Dictionary operations: key-value pairs,
               accessing, updating, traversing, and methods.
===================================================================
"""

# Creating a dictionary (using Country -> Capital as requested)
capitals = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "France": "Paris"
}
print("Original Dictionary :", capitals)
# Output: {'India': 'New Delhi', 'USA': 'Washington D.C.', 'France': 'Paris'}

# Accessing Elements
print("\n--- Accessing Elements ---")
print("Capital of India :", capitals["India"])  # Output: New Delhi
# Using get() method (prevents error if key does not exist)
print("Capital of Japan :", capitals.get("Japan"))  # Output: None
print("Capital of France:", capitals.get("France")) # Output: Paris

# Adding and Updating Elements
print("\n--- Adding & Updating ---")
# Adding new key-value pair
capitals["Japan"] = "Tokyo"
print("After adding Japan   :", capitals)
# Output: {'India': 'New Delhi', 'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo'}

# Updating an existing value
capitals["USA"] = "Washington"
print("After updating USA   :", capitals)
# Output: {'India': 'New Delhi', 'USA': 'Washington', 'France': 'Paris', 'Japan': 'Tokyo'}

# Dictionary Methods
print("\n--- Dictionary Methods ---")
# keys()
print("All Countries (Keys) :", list(capitals.keys()))  # Output: ['India', 'USA', 'France', 'Japan']

# values()
print("All Capitals (Values):", list(capitals.values())) # Output: ['New Delhi', 'Washington', 'Paris', 'Tokyo']

# items()
print("All Items (Pairs)    :", list(capitals.items()))
# Output: [('India', 'New Delhi'), ('USA', 'Washington'), ('France', 'Paris'), ('Japan', 'Tokyo')]

# update() - merging another dictionary
capitals.update({"Germany": "Berlin", "France": "Paris (Updated)"})
print("After update() method:", capitals)
# Output: {'India': 'New Delhi', 'USA': 'Washington', 'France': 'Paris (Updated)', 'Japan': 'Tokyo', 'Germany': 'Berlin'}

# pop() - removes specific key and returns value
popped_capital = capitals.pop("Germany")
print("Popped capital       :", popped_capital)        # Output: Berlin
print("After pop('Germany') :", capitals)
# Output: {'India': 'New Delhi', 'USA': 'Washington', 'France': 'Paris (Updated)', 'Japan': 'Tokyo'}

# Traversing
print("\n--- Traversing Dictionary ---")
for country, capital in capitals.items():
    print("Country:", country, " | Capital:", capital)
# Output:
# Country: India  | Capital: New Delhi
# Country: USA  | Capital: Washington
# Country: France  | Capital: Paris (Updated)
# Country: Japan  | Capital: Tokyo


"""
===========================
Expected Output:
===========================
Original Dictionary : {'India': 'New Delhi', 'USA': 'Washington D.C.', 'France': 'Paris'}

--- Accessing Elements ---
Capital of India : New Delhi
Capital of Japan : None
Capital of France: Paris

--- Adding & Updating ---
After adding Japan   : {'India': 'New Delhi', 'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo'}
After updating USA   : {'India': 'New Delhi', 'USA': 'Washington', 'France': 'Paris', 'Japan': 'Tokyo'}

--- Dictionary Methods ---
All Countries (Keys) : ['India', 'USA', 'France', 'Japan']
All Capitals (Values): ['New Delhi', 'Washington', 'Paris', 'Tokyo']
All Items (Pairs)    : [('India', 'New Delhi'), ('USA', 'Washington'), ('France', 'Paris'), ('Japan', 'Tokyo')]
After update() method: {'India': 'New Delhi', 'USA': 'Washington', 'France': 'Paris (Updated)', 'Japan': 'Tokyo', 'Germany': 'Berlin'}
Popped capital       : Berlin
After pop('Germany') : {'India': 'New Delhi', 'USA': 'Washington', 'France': 'Paris (Updated)', 'Japan': 'Tokyo'}

--- Traversing Dictionary ---
Country: India  | Capital: New Delhi
Country: USA  | Capital: Washington
Country: France  | Capital: Paris (Updated)
Country: Japan  | Capital: Tokyo
===========================
"""
