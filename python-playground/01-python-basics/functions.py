# ---------------------------------
# SIMPLE FUNCTIONS
# ---------------------------------

# def name_of_function(parameters):
#     # statements
#     # statements
#     # return something
    
def greet():
    print("Hi There")
    print("Welcome Aboard!!")
    
greet()

# ---------------------------------
# Functions with Parameters
# ---------------------------------

def add_two_numbers(one,two):
    print(f"Addition of {one} and {two} is",(one+two))
    
add_two_numbers(3,6)

# ---------------------------------
# Functions which returns
# ---------------------------------

def get_greeting(name):
    greeting=f"Hi {name.upper()}"
    return greeting;

greeting_for_tom=get_greeting("Tom")

# ?Send in an email
# Store in Logs
# Send over in a Whatsapp API

print(greeting_for_tom)

# ---------------------------------
# Functions Keyword Arguments
# ---------------------------------

# Increment a number by 2 after its factorial has been calculated
import math
def increment_after_factorial(number,by):
    number=math.factorial(number)+by
    return number

print("Factorial of 5 plus 1 is",increment_after_factorial(5,1))
print("Factorial of 6 plus 2 is",increment_after_factorial(6,2))

print("Factorial of 4 plus 3 is",increment_after_factorial(number=4,by=3))

print("Factorial of 3 plus 4 is",increment_after_factorial(by=4,number=3))

# ---------------------------------
# Functions Default Keyword Arguments
# ---------------------------------

def increment(number,by=1):
    print(f"{number} incremeneted by {by} is",number+by)
    
increment(4,1)
increment(5)
increment(6,3)

# ---------------------------------
# Varying Arguments
# ---------------------------------

# Write a function which will multiply the numbers given to it 

def multiply(*numbers):
    print(numbers)
    print(type(numbers))
    total=1
    for number in numbers:
        total=total*number
    print(total)
    

multiply(1,2,3)
multiply(3,4,5,6)
multiply(5,6,7,8,9)


# ---------------------------------
# KWArgs Key Value Varying Arguments
# --------------------------------- 

def order_pizza(pizza,**details):
    print(f"Order recevied for {pizza}")
    for key,value in details.items():
        print(f"{key}:{value}")
    
order_pizza("Margerita Pizaa",size="medium",crust="Thin",extra_cheese=True)
order_pizza("Farm Fresh Pizza",crust="Thin",size="Large",toppings=["Onion,Tomato,Corns"]);