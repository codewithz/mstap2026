
name= "Neueda Inc"
print(name)

# print(dir(name))

#String in python can be enclosed in 
# " "
# ' '
#  ''' multi 
#      line
#  '''

# ""  ''

sentence= "I don't know where they are"
print(sentence)

paragraph = '''
                Variables are containers that store values.
                In Python, they are dynamically typed, 
                meaning you don't have to declare their type explicitly — 
                the interpreter figures it out at runtime. 
                This is similar to JavaScript but with different syntax and conventions.
                Python variables can hold primitive values (such as numbers and strings)
                or references to objects (such as lists, dictionaries, functions, or user-defined objects).
                '''
                
print(paragraph)


#                       0  1  2  3  4  5                     0- based 
#                       K  i  t  k  a  t
#                       1  2  3  4  5  6                     1- based



word= 'Kitkat'
print(word)
print(word[1])
print(word[2])
print("Word [1:3] -- ", word[1:3])
# print(word[8])   IndexError: string index out of range

print(word[0:20])

print(word[:5])

print(word[:])

# Length

print("Length: ", len(word))

# Trimming -- strip()
word_with_spaces ="    Hello World    "
print(word_with_spaces)
print("Lenght before using strip:",len(word_with_spaces))

word_with_spaces=word_with_spaces.strip();
print(word_with_spaces)
print("Lenght after using strip:",len(word_with_spaces))

print(name)

print("Upper Case:",name.upper())
print("Lower Case: ",name.lower())

sentence =" I AM HAPPY"
print("Title:",sentence.title())
sentence=" i am happy"
print("Capitalize:",sentence.strip().capitalize())

#  Split a String

line1="1,Tom,IT,Developer,20000"
data1=line1.split(",")
print("Line1:",line1);
print("Data1:",data1)
print(type(line1))
print(type(data1))

line2="Hello How are you?"
data2=line2.split(" ")
print("Line2:",line2);
print("Data2",data2)
print(type(line2))
print(type(data2))

# Formatted String 
# format()

line="My name is {} ,my age is {}"
name="Zartab"
age=36

fline=line.format(name,age)

print("O:",line)
print("F:",fline)

other_line=f"My name is {name}, my age is {age}"
print("Other Line:",other_line)

# numbered and named formatting

line="{0} {1} sat on a wall, {0} {1} had a great fall"
fline=line.format("Humpty","Dumpty")
print("F:",fline)

line="{person1} {person2} sat on a wall, {person1} {person2} had a great fall"
fline=line.format(person1="Humpty",person2="Dumpty")
print("F:",fline)

# Escape Characters

# \n -- New Line
# \t -- Tab
# \\ -- backslash
#  \" -- double quotes 

text ="This is a backslash \\"
print(text)

text ="These are twobackslashes \\\\"
print(text)

text="I work for \" Neueda \" "
print(text)

# in

weather ="Weather is quite hot now"
check_if_hot="ot" in weather
print("Is it hot:",check_if_hot)


