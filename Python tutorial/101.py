# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# My Cheet Sheet in Python 101 !!


# ++++++++++ Strings ++++++++++ #
print("Strings and things:")

print("Hello World!")

print("""This is a,
multi-line string""")

print("Hi"+" there")

print("\n") #for a new line 


# ++++++++++ Maths ++++++++++ #
print("Math time:")

print(50 + 50) #addition
print(50 - 50) #subtraction
print(50 * 50) #multiplication
print(50 / 50) #divition
print(50 ** 2) #exponent (to the power of..)
print(50 // 6) #divide without leftover
print(50 % 6) #modulo (which means it will only give us the remain number)

print("\n") #new line


# ++++++++++ Variables & methods ++++++++++ #
print("Playing with Variables and methods:")

name = "Mohammed"
print(name)

age = 29 #int doesn't need quotes (( int(29) )) + it doesn't display decimal numbers
print(int(age))

age += 1
print(int(age)) # ( += ) addition to a variable value

birthday = 1
age += birthday #it's another way of adding to a variable

gpa = 3.7 #float(3.7) to display the decimal number
print(float(gpa))

color = "Red"
print(color)

celebrity = "Tom Cruise"
print(celebrity)

print("My name is "+ name +" and I'm "+ str(age) +" and my gpa is: "+ str(gpa)) #you should convert int into string to combine with text

quote = "All is fair in war and love"
print(len(quote)) #gives the length of the variable
print(quote.upper()) #capitalized all the string
print(quote.lower()) #lower case all the string
print(quote.title()) #capitalized the first letter

print("\n") #new line


# ++++++++++ Functions ++++++++++ #
print("Now, some functions:")

def who_am_i(): #you should leave some space before the variables and stuff in the function or it won't work !!!
    name1 = "Mohammed"
    age = 15
    print("Hello, my name is " + name1 + " and I'm " + str(age) + " years old!")

who_am_i() #that's how you call a variable
#the variables in the function only work inside the function.
#Example: { print(name1) } will give an error becuase it's only declaired in the function

print("\n") #for a new line


# ++++++++++ adding in parameter ++++++++++ #
print("adding one parameter")

def add_one_hundred(num):  #this function will add any number you put when you call the function by hundred
    print(num + 100)

add_one_hundred(100) #the answer will be 200

print("\n") #for a new line


# ++++++++++ add in multiple parameter ++++++++++ # 
print("adding multiple parameter")

def add(x, y):
    print(x + y)

add(15,10)

print("\n") #for a new line


# ++++++++++ Using return ++++++++++ #
print("Using return:")

def multiply(x, y): #this function will return the result 
    return x * y

print(multiply(5,5))  #this will print the answer

print("\n") #for a new line


# ++++++++++ Square Root ++++++++++ #
print("Square Root:")

def square_root(x): #this function will give the square root of a number
    return x ** .5

print(int(square_root(25)))  #this will print the answer ( you can remove the int function to display decimal numbers )

print("\n") #for a new line

# ++++++++++ Boolean ( True or False ) expressions  ++++++++++ #
print("Boolean expression my guy:")

bool1 = True
bool2 = 3*3 == 9 #if you put one ( = ) that will declaire a variable so you put ( == ) to give the answer ( to be like normal equal )
bool3 = False
bool4 = 3*3 != 9 #( != ) means does not equal 

print(bool1,bool2,bool3,bool4)
print(type(bool1)) #function ( type() ) will give the type of the thing in the barckets  ( it will give us bool { which mean boolean } )

bool5 = "True"
print(type(bool5)) #this will give us the type as ( str ) which means it's a string which means it's true

print("\n") #for a new line


# ++++++++++ Relational & Boolean Operatores ++++++++++ #

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to ,less_than_equal_to)

print("\n") #for a new line


# ++++++++++ Conditionals Statements ++++++++++ #
print("Conditional Statments:")

def soda(money):
    if money >= 2:
        return "You've got yourself a soda"
    else:
        return "No soda for you!"

print(soda(3))
print(soda(1))

def alcohol(age, money):
    if (age >= 21) and (money >= 5): # ( >= ) means more than of equal
        return "We're gettin tipsy!" # 1
    elif (age >= 21) and (money < 5): # ( < ) means less than
        return "Come back with more money" # 2
    elif (age < 21) and (money >= 5): 
        return "Nice try kido" # 3
    else: 
        return "You're too poor and too young!" # 4

print(alcohol(21, 5)) # 1
print(alcohol(21, 4)) # 2
print(alcohol(20, 5)) # 3
print(alcohol(20, 3)) # 4

print("\n") #new line


# ++++++++++ Lists ++++++++++ #
print("Lists have brackets:")

movies = ["when Harry Met Sally", "The Hangover", "The Perks Of Being a Wallflower", "The Exorcist"]

print(movies[0]) # (1-The numbers start from 0 not 1) (2-You should use [] when you specify a thing in list)
print(movies[0:3]) # ( 0:3 ) means the movies from 0 to 3 
print(movies[1:]) #This will type all the list starting from 1 (or the second item)
print(movies[:2]) #This will type all the list before item  number 2 (or the third item)
print(movies[-1]) #This will print the last item in the list ( -1 )
print(len(movies))#This will tell hoe many items in the list

movies.append("JAWS") #This will add new item to the list (It will be located in the last ( -1 ))
print(movies)

movies.pop() #This will delete items from the list ( if you don't specify an item it will delete the last item )
print(movies)

movies.pop(1) #This will remove the second item
print(movies)

movies = ["when Harry Met Sally", "The Hangover", "The Perks Of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Jake", "Leah", "Jeff"]

combined = zip(movies, person) #This command will combine the two list ( number 1 in movies list with number 1 in person list and so on..)
print(list(combined)) #That's how you call the combine list

print("\n") #new line


# ++++++++++ Tuples ++++++++++ #
print("Tuples have parentheses and cannot change:")

grades = ("A", "B", "C", "D", "E") #Static ( cannot be changed ) also tuples have parentheses while list have brackets 
print(grades[0])

print("\n") #new line


# ++++++++++ Looping ++++++++++ #
print("For loops - start to finish of iterates:")

vegetable = ["cucumber", "spinach", "cabbage"]
for x in vegetable:
    print(x)

print("While loops - Execute as long as True:")

i = 1
while i <= 10:
    print(i)
    i += 1

print("\n") #new line

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #