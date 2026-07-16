# ----------------------------------------------------------------------
# What is a Higher-Order Function?
# ----------------------------------------------------------------------
# A higher-order function is simply a function that does at least one of:
#   1. Takes another function as an argument, OR
#   2. Returns a function as its result
#
# This works in Python because functions are "first-class objects" --
# you can assign them to variables, store them in lists, and pass them
# around exactly like a number or a string.
 
def greet():
    print("Hello there!")
 
say_hello = greet   # no parentheses -- we're pointing at the function, not calling it
say_hello()          # NOW we call it, via the new name
print(type(greet))
# Output:
# Hello there!
# <class 'function'>
 
# ----------------------------------------------------------------------
# Lambda functions -- small, unnamed, "throwaway" functions
# ----------------------------------------------------------------------
# lambda parameters: expression
# A lambda is a function with no name, limited to ONE expression, and
# an implicit return -- useful when you need a quick function for a
# single use, especially as an argument to another function.
 
square = lambda number: number ** 2
print(square(5))
# Output:
# 25
 
# Equivalent, written as a normal function -- same result, more typing:
def square_normal(number):
    return number ** 2
print(square_normal(5))
# Output:
# 25
 
# Multiple parameters work too:
add = lambda a, b: a + b
print(add(3, 4))
# Output:
# 7
 
# Rule of thumb: if you need to give it a name and reuse it, write a normal
# "def" function. If it's quick, disposable, and only used once (usually
# as an argument to another function), a lambda keeps things compact.
 
# ----------------------------------------------------------------------
# map() -- a higher-order function that TRANSFORMS every item
# ----------------------------------------------------------------------
# map(function, iterable) -- applies function to every item, returns a map object
# (wrap it in list(...) to see/use the results)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda n: n ** 2, numbers))
print("Squared:", squared)
# Output:
# Squared: [1, 4, 9, 16, 25]
 
cart = [("Bread", 15, 2), ("Jam", 3, 1), ("Butter", 7, 3)]
prices = list(map(lambda item: item[1], cart))
print("Prices via map:", prices)
# Output:
# Prices via map: [15, 3, 7]
 
# ----------------------------------------------------------------------
# filter() -- a higher-order function that KEEPS items matching a condition
# ----------------------------------------------------------------------
# filter(function, iterable) -- keeps items where function(item) is True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print("Evens via filter:", evens)
# Output:
# Evens via filter: [2, 4, 6, 8, 10]
 
expensive_items = list(filter(lambda item: item[1] > 5, cart))
print("Items over $5 via filter:", expensive_items)
# Output:
# Items over $5 via filter: [('Bread', 15, 2), ('Butter', 7, 3)]
 
# ----------------------------------------------------------------------
# sorted() -- a higher-order function that takes a "key" function
# ----------------------------------------------------------------------
# The key function tells sorted() WHAT to sort by, instead of sorting
# items directly. sorted() calls your key function once per item, then
# sorts based on what it returns.
names = ["Tom", "Alexandra", "Jo", "Mohammed"]
by_length = sorted(names, key=lambda name: len(name))
print("Sorted by length:", by_length)
# Output:
# Sorted by length: ['Jo', 'Tom', 'Mohammed', 'Alexandra']
 
cart_by_price = sorted(cart, key=lambda item: item[1], reverse=True)
print("Cart sorted by price, highest first:", cart_by_price)
# Output:
# Cart sorted by price, highest first: [('Bread', 15, 2), ('Butter', 7, 3), ('Jam', 3, 1)]