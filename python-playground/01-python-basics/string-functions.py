
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

