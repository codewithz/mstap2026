
# ----------------------------------------------------------------------
# Working with JSON Data
# ----------------------------------------------------------------------
# JSON (JavaScript Object Notation) is a text format for exchanging data
# between systems -- APIs, config files, and data files all commonly use it.
# Good news: JSON objects map directly onto Python dicts and lists.

import json

# ----------------------------------------------------------------------
# Converting a JSON string INTO Python objects -- json.loads()
# ----------------------------------------------------------------------
json_string = '{"name": "James", "age": 29, "city": "London", "active": true}'
data = json.loads(json_string)
print(type(data))
print(data)
print("Name:", data["name"])
print("Age:", data["age"])
# Output:
# <class 'dict'>
# {'name': 'James', 'age': 29, 'city': 'London', 'active': True}
# Name: James
# Age: 29

# A JSON array becomes a Python list
json_array = '[1, 2, 3, 4, 5]'
number_list = json.loads(json_array)
print(type(number_list))
print(number_list)
# Output:
# <class 'list'>
# [1, 2, 3, 4, 5]

# Nested JSON becomes nested dicts/lists -- no extra work needed
json_nested = '''
{
    "customer": "TechCorp",
    "products": ["Laptop", "Monitor", "Keyboard"],
    "address": {"city": "New York", "country": "United States"}
}
'''
nested_data = json.loads(json_nested)
print(nested_data["customer"])
print(nested_data["products"])
print(nested_data["address"]["city"])
# Output:
# TechCorp
# ['Laptop', 'Monitor', 'Keyboard']
# New York

# ----------------------------------------------------------------------
# Converting Python objects INTO a JSON string -- json.dumps()
# ----------------------------------------------------------------------
customer = {
    "name": "Sarah",
    "age": 27,
    "subscribed": True,
    "plans": ["Broadband", "Mobile"],
}
json_output = json.dumps(customer)
print(type(json_output))
print(json_output)
# Output:
# <class 'str'>
# {"name": "Sarah", "age": 27, "subscribed": true, "plans": ["Broadband", "Mobile"]}

# Pretty-print with indentation, much easier to read
pretty_json = json.dumps(customer, indent=4)
print(pretty_json)
# Output:
# {
#     "name": "Sarah",
#     "age": 27,
#     "subscribed": true,
#     "plans": [
#         "Broadband",
#         "Mobile"
#     ]
# }

# ----------------------------------------------------------------------
# A common real-world pattern: read a JSON file, use the data, write it back
# ----------------------------------------------------------------------
# with open("customer.json", "r") as f:
#     data = json.load(f)          # note: json.load() (no 's') reads directly from a file
#
# with open("customer.json", "w") as f:
#     json.dump(data, f, indent=4) # note: json.dump() (no 's') writes directly to a file
# Output:
# Cart sorted by price, highest first: [('Bread', 15, 2), ('Butter', 7, 3), ('Jam', 3, 1)]