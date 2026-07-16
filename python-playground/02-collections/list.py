# ------------------------------------
# Lists
# ------------------------------------

# Lists are indexed and mutable collection

#  []

# ------------------------------------
# Ways for creating a list
# ------------------------------------

letters=['a','b','c','d','e']
print(type(letters))
print(letters)

matrix=[[0,1],[2,3]]
print(matrix)

zeros= [0]*10
print(zeros)

print("-"*30)

numbers=list(range(1,11))
print(numbers)

combined=letters+zeros
print(combined)

organzation="Neueda"
chars=list(organzation)
print(chars)

print("-"*30)
# ------------------------------------
# Access Elements in List
# ------------------------------------

letters=['a','b','c','d','e']
print("List:",letters)

# Access the first element
print("First:",letters[0])

# Access the last element
print("Last:",letters[-1])

# Access in Range [:]

print(letters[0:2])
print(letters[:3])
print(letters[2:])
print(letters[:])

print("-"*30)
# ------------------------------------
# Steppers in List
# ------------------------------------

numbers=list(range(1,21))
print(numbers[::2])
print(numbers[0:12:3])
print(numbers[::-1])


print("-"*30)
# ------------------------------------
# List Unpacking
# ------------------------------------

numbers=[1,2,3,4,5,6]
# Traditoinal Way

first=numbers[0]
second=numbers[1]
third=numbers[2]
fourth=numbers[3]
second_last=numbers[-2]
last=numbers[-1]

print("List:",numbers)
print("First",first)
print("Second",second)
print("Third",third)
print("Second Last",second_last)
print("Last",last)

print("---- List Unpacking ----")
numbers=[10,20,30,40,50,60]
first,second,third,fourth,second_last,last=numbers

print("List:",numbers)
print("First",first)
print("Second",second)
print("Third",third)
print("Second Last",second_last)
print("Last",last)

numbers=[1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,6,7]
f,s,t,*others,sl,l=numbers

print("List:",numbers)
print("First",f)
print("Second",s)
print("Third",t)
print("Others",others)
print("Second Last",sl)
print("Last",l)

print("-"*30)
# ------------------------------------
# Iterations in a list
# ------------------------------------

for letter in letters:
    print(letter)
    
for letter in enumerate(letters):
    print(letter)
    
# element=[0,'a']

# index
# value

index,value=(0,'a')

print("Index:",index)
print("Value:",value)

print("-"*30)

for key,value in enumerate(letters):
    print("Key:",key)
    print("Value:",value)
    
print("-"*30)
# ------------------------------------
#Adding and Removing elements from a list
# ------------------------------------

letters=["a","b","c","e"]

print("Original:",letters)

# Add an element
letters.append("f");
print("Append:",letters)

letters.insert(3,"d")
print("Insert:",letters)

# Remove an elements

# pop
poppped=letters.pop(0);
print("Value removed from list:",poppped)
print("After pop:",letters)

# remove
letters.remove("e")
print("After remove:",letters)

print("-"*30)
# ------------------------------------
# Find elements in a list
# ------------------------------------

letters=["d","a","b","e","c"]
print("Letters",letters)

print("Index of a",letters.index("a"))
# print("Index of a",letters.index("f"))

if 'f' in letters:
    print("Index of f",letters.index("f"))
else:
    print("f is not in the list")
    
count=letters.count("d")
print("Count of d is ",count)

print("-"*30)
# ------------------------------------
# Sort elements in a list
# ------------------------------------

numbers=[3,51,45,34,90,4,43]
print("Original:",numbers)

numbers.sort()
print("S:",numbers)

numbers.sort(reverse=True)
print("R:",numbers)

print("Original:",numbers)
print("----------Sorted using sorted()------------")
other_numbers=[10,43,23,56,23,89]
print("Original Other Numbers:",other_numbers)

sorted_list=sorted(other_numbers)
print("S:",sorted_list)

sorted_list=sorted(other_numbers,reverse=True)
print("S:",sorted_list)

print("Original Other Numbers:",other_numbers)




