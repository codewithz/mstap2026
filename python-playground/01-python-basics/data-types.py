# python file --> data-types.py
#  For executing the file : python name_of_the_file.py

x='Neueda'
print(type(x))
print(x)

print("-------------------------------------------------")

x=10
print(type(x))
print(x)

print("-------------------------------------------------")

x=9223372036854775809
print(type(x))
print(x)

print("-------------------------------------------------")

x=15.7
print(type(x))
print(x)

print("-------------------------------------------------")
# Complex Number  -- real number  + 'imaginary number' j
x= 10 + 5j;
print(type(x))
print(x)

print("-------------------------------------------------")
# Boolean Values 
# True
# False
x=True
print(type(x))
print(x)

x=False
print(type(x))
print(x)

# Sequences  
# List -- [] -- mutable
# Tuple -- () -- immutable -- read only list
# Range -- range(from,to) -- iterable

x=['Hyundai','Kia','Toyota','Ford']
print(type(x))
print(x)

print("-------------------------------------------------")

x=('Hyundai','Kia','Toyota','Ford')
print(type(x))
print(x)

print("-------------------------------------------------")

x=range(1,10)
print(type(x))
print(x)

# Set and Dictionary
# Set -- {} -- no duplicates/unique || unordered
# Dictionary -- {key:value} || key cannot be duplicate

print("-------------------------------------------------")

x={'Hyundai','Ford','Kia','Ford','Toyota','Hyundai'}
print(type(x))
print(x)

print("-----------------------------------------")

x= {
    "key" : "value",
    "name":"Zartab M Nakhwa",
    "city": "Mumbai, India",
    "age":36,
    "married":True,
    "tech_stack":["Java","Python","SQL"],
    "car" :{
        "make":"Tucson",
        "build":"Hyundai"
    }
}
print(type(x))
print(x)