# If - Else  - Elif 

if True:
    print("Hello")
    print("This statement is under if block")

print("We are out of if statement here ");

if False:
    print("Hello")
    print("This statement is under if block")

print("We are out of if statement here "); 

x=2

if x>3:
    print("Number is greater than 3")
else:
    print("Number is lesser than 3")
    
#  && -- and
#  || -- or


# m=int(input("Enter First Number:"))
# n=int(input("Enter Second Number:"))
# o=int(input("Enter Third Number:"))

# if (m>n and m>o):
#     print(f"{m} is greater than {n} and {o}")
# elif (n>m and n>o):
#      print(f"{n} is greater than {m} and {o}")
# else:
#      print(f"{o} is greater than {n} and {m}")
     
# ---Loan Processing System--
high_income=False
good_credit=True
is_student=True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")
    
if (high_income or good_credit) and is_student:
    print("Eligible")
else:
    print("Not Eligible")
    
# Ternary Operator 

age=19
message=""

if age >18:
    message="Can Vote"
else:
    message="Cannot Vote"

print(message)

age=7
# variable = Output if condition is True if condition else Output if condition is False

message= "Can Vote" if age>18 else "Cannot Vote"
print(message)

# Assign Grades 
# If score is 90 or above : A
# If score is 80 to 89 : B
# If score is 70 to 79 : C
# Otherwise : F

score =86

grade = "A" if score >=90 else "B" if score>=80 else "C" if score >= 70 else "F"

print(score,"--",grade)

# Loops 

# while 

# 1. Initialization
# 2. Condition
# 3. Increment/ Decrement 

number=1

while number<=10:
    print(number)
    number+=1

print("-"*60)
number=100

while number>0:
    print(number)
    number=number//2
# / Divide
# // Floor Divide -- nearest smallest whole number
print("-"*60)
command=""

while command.lower() !='quit':
    command=input(">>")
    print("ECHO:",command)
    
# for loop

#  for element in collection:

# for item in items:
print("-"*60)
numbers=[1,2,3,4,5,6]

for number in numbers:
    print("Number is ",number)
    
print("-"*60)
animals=['Dog','Cat','Mouse','Duck']

for animal in animals:
    print(animal)

print("-"*60)

for number in range(1,6):
    print(number)
    
print("-"*60)

success=True
for attempt in range(1,6):
    print("Attempt:",attempt)
    print("Attempting to send a message");
    if(attempt==3 and success):
        print("Message Sent Successfully")
        break
else:  # Will only be reached if the preceeding loop completed without breaking
    print("####Attempted sending 5 times, but failed####")
    
print("-"*60)
# Switch
value=int(input("Enter a number:"))
match value:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print("Three")
    case _:
        print("Unknown")
    
    
    
    



 













    