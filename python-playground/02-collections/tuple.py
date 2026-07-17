# --------------------------------
# -- Tuples
# --------------------------------

# Tuples are read only list
#  ()

# Multiple ways of creating a Tuple

point =(1,2)
print(type(point))
print(point)

point =1,
print(type(point))
print(point)

point =1,2,3
print(type(point))
print(point)

point =(1,2) + (3,4)
print(type(point))
print(point)


point =(1,2)* 3
print(type(point))
print(point)


point =("Neueda",) * 4
print(type(point))
print(point)

# ----------------Access elements in Tuples ---------

point=(1,2,3)

print("Point:",point)


print("Index[1] : ",point[1])
print("Range : ",point[0:])
print("Range : ",point[0:2])

x,y,z= point
print("X:",x)
print("Y:",y)
print("Z:",z)

if 10 in point:
    print("10 is in the point tuple")
else:
    print("10 is not in the point tuple")
    
# point[1]=10
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment