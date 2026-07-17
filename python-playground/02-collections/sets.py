# ________ SET _____________


# Set --> No Duplicates || Unordered
# Mutable

#  {}

# --------- Mulitples ways of creating a Set _

first= {1,4,5,6,7,4,5}
print(type(first))
print(first)

numbers= [1,2,3,4,5,6,1,2,3,4,5,7,8,9,10]

second=set(numbers)
print(type(second))
print(second)

third={*numbers}
print(type(third))
print(third)

# ------------------ Add and remove elements from a Set ---

third.add(11)
print("Add:",third)

third.remove(4)
print("Remove:",third)

# third.remove(4)
# print("Remove:",third)
# KeyError: 4

third.discard(5)
print("Discard:",third)

third.discard(5)
print("Discard:",third)

# -------------- Set Operations

# Union   |
# Intersection   &
# Difference   -
# Symmetric Difference   ^

first={1,2,3,4,5}
second={4,5,6,7,8}


union=first.union(second)
print("Union:",union)

union_n=first | second
print("Union Notation:",union_n)

intersection=first.intersection(second)
print("Intersection:",intersection)

intersection_n=first & second
print("Intersection Notation:",intersection_n)

difference=first.difference(second)
print("difference:",difference)

difference_n=first - second
print("difference Notation:",difference_n)

sym_difference=first.symmetric_difference(second)
print("sym_difference:",sym_difference)

sym_difference_n=first ^ second
print("sym_difference Notation:",sym_difference_n)