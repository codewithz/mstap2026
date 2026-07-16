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