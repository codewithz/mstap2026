#  --- dictionary

# Key-Value pairss
#  {key:value,key:value,.......}
# Contact book : Name --. Number

# --- mutiple ways of creating a dictionary 

point= {"x":1, "y":2}
print(point)
print(type(point))


point= dict(x=1,y=2)
print(point)
print(type(point))

details=dict(name="Zartab", city="Mumbai", age=36, 
             married=True,program_stack=["Java","Python","SQL"])
print(details)
print(type(details))


# ----- Accessing the elements in a Dictionary

print("Name:", details.get("name"))
print("Age:", details["age"])
print("Country:", details.get("country"))
# print("Country:", details["country"])
# KeyError: 'country'
print("Country:", details.get("country","UK"))
details["country"]="India"
print("Country:", details.get("country","UK"))

details["program_stack"].append("JS")
print(details)

del details["program_stack"]
print(details)

popped_element=details.pop("city")
print(popped_element)
print(details)

print("-"*30)


# ---- Iterate through a Dictionary ---
details=dict(name="Zartab", city="Mumbai", age=36, 
             married=True,program_stack=["Java","Python","SQL"])

for element in details:
    print(element)
    
print("-"*30)
for item in details.items():
    print(item)
    print("Key:",item[0])
    print("Value:",item[1])
    print("Type",type(item))
    
print("-"*30)

for key,value in details.items():
   
    print("Key:",key)
    print("Value:",value)
    
print("-"*30)

key_list=details.keys()
value_list=details.values()

print("Keys:",key_list)
print("Values:",value_list)


# ---- Sorting the dictionary
  
print("-"*30)

marks={"Tom":85,"Alex":92,"Penny":78,"Mike":92,"John":60}
print(marks)
print("-"*30)
sorted_by_key= dict(sorted(marks.items()))
print("Sorted By Name:",sorted_by_key)
print("-"*30)
sorted_by_value=dict(sorted(marks.items(),key=lambda item:item[1]))
print("Sorted By Value:",sorted_by_value)
print("-"*30)
sorted_by_value_desc=dict(sorted(marks.items(),key=lambda item:item[1],reverse=True))
print("Sorted By Value:",sorted_by_value_desc)
print("-"*30)