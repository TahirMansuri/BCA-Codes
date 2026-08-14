"""
===================================================================
Practical No : Practical 07
Course Code  : CA - 214 (Practical based on Python Programming)
Class        : SYBCA (Semester-III) | Academic Year: 2026-2027
Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
Faculty      : Mr. Tahir Husen Najir Mansuri (HOD & Asst. Prof.)
Aim          : Write a program to demonstrate the use of Dictionary 
               & related functions.
===================================================================
"""

print("=== Dictionary and Related Functions ===")

# Dictionary - Country Name as Key, Capital as Value
country_capital = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

print("Country - Capital Dictionary :", country_capital)

print("\n--- Accessing Values ---")
print("Capital of India  :", country_capital["India"])
print("Capital of France :", country_capital.get("France"))

print("\n--- Adding a New Country ---")
country_capital["Germany"] = "Berlin"
print("After adding Germany :", country_capital)

print("\n--- Updating a Value ---")
country_capital["USA"] = "Washington"
print("After updating USA   :", country_capital)

print("\n--- Removing a Country ---")
country_capital.pop("Japan")
print("After removing Japan :", country_capital)

print("\n--- Dictionary Methods ---")
print("Keys   :", country_capital.keys())
print("Values :", country_capital.values())
print("Items  :", country_capital.items())

print("\n--- Looping through Dictionary ---")
for country, capital in country_capital.items():
    print("Country:", country, " --> Capital:", capital)


"""
===========================
Expected Output:
===========================
=== Dictionary and Related Functions ===
Country - Capital Dictionary : {'India': 'New Delhi', 'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo'}

--- Accessing Values ---
Capital of India  : New Delhi
Capital of France : Paris

--- Adding a New Country ---
After adding Germany : {'India': 'New Delhi', 'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Germany': 'Berlin'}

--- Updating a Value ---
After updating USA   : {'India': 'New Delhi', 'USA': 'Washington', 'France': 'Paris', 'Japan': 'Tokyo', 'Germany': 'Berlin'}

--- Removing a Country ---
After removing Japan : {'India': 'New Delhi', 'USA': 'Washington', 'France': 'Paris', 'Germany': 'Berlin'}

--- Dictionary Methods ---
Keys   : dict_keys(['India', 'USA', 'France', 'Germany'])
Values : dict_values(['New Delhi', 'Washington', 'Paris', 'Berlin'])
Items  : dict_items([('India', 'New Delhi'), ('USA', 'Washington'), ('France', 'Paris'), ('Germany', 'Berlin')])

--- Looping through Dictionary ---
Country: India  --> Capital: New Delhi
Country: USA  --> Capital: Washington
Country: France  --> Capital: Paris
Country: Germany  --> Capital: Berlin
===========================
"""
