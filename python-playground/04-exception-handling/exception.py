numbers=[1,2]

try:
    print(numbers[1])
    print(numbers[4])
except IndexError as ex:
    print("IndexError :",ex)


print("I am here .....")

print("-"*30)

try:
        age=int(input("Enter Age:"))
        print(f"Age is {age}")
except ValueError as ex:
    print("You have entered an invalid age")
    print(ex)
    print(type(ex))
else:
    print("Else after a try executes only when there is no exception")
    
    
print("-"*30)
# Handling Multiple Exception
    
try:
    age=int(input("Enter Age:"))
    xfactor=10/age
    print(f"Age is {age}")
    print(f"Xfactor is {xfactor}")
    numbers=[1,2,3]
    print(numbers[5])

except ValueError as ex:
    print("Value Error: Invalid Age Entered")
except ZeroDivisionError as ex:
    print("ZDE Error:You seem to have added age as zero")
except Exception as ex:
    print("Sone Exception have occured")
    print("Reason:",ex)

    

    
    
print("\n\n Execution continues....")
