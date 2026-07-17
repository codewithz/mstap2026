# ----------------------------------
# Sorting a complex list
# -----------------------------------

# cart=[(Name,Price,Qty)]

cart=[('Bread',15,2),('Butter',
                      7,3),('Eggs',3,1)]
print(cart)
print(type(cart))

cart.sort()
print("Sorted:",cart)

sorted_cart=sorted(cart)
print("Sorted other way:",sorted_cart)

def key_for_cart_sorting(item):
    return item[1]

cart.sort(key=key_for_cart_sorting)
print("Sorted:",cart)

# Lambda Function 

# Anonymous Functions 

# lambda parameters: expression
# def key_for_cart_sorting(item):
#     return item[1]



lambda item : item[1]

cart.sort(key=lambda item: item[2])
print("Sorted on Qty",cart)
#---------------------------------------------------------------
# -- filter
# ---------------------------------------------------------------------

# Filter those products whose price is greater than 5$

cart=[('Bread',15,2),('Butter',
                      7,3),('Eggs',3,1)]

#  filtered_list=list(filter(funciton_where_filter_logic_is_written,source_collection))


# def filter_price_above_5(cart_item):
#     return cart_item[1]>5

# lambda cart_item : cart_item[1]>5

filtered_cart=list(filter(lambda cart_item : cart_item[1]>5,cart))

print("Filtered Cart:",filtered_cart)

print(30*"-")
#---------------------------------------------------------------
# -- map
# ---------------------------------------------------------------------

numbers=[1,2,3,4,5]

# mapped_list=list(map(function_where_transformation_logic_is_written,source_collection))

def square_of_the_number(number):
    return pow(number,2)

lambda number: pow(number,2)

squared_numbers=list(map(square_of_the_number,numbers))

print("O:",numbers)
print("M:",squared_numbers)

# -------------------------- Exercise ------------------
# (Name,Price,Qty)  ---> (Name,Price,Qty,Total)
cart=[('Bread',15,2),('Butter',7,3),('Eggs',3,1)]

