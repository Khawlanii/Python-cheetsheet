# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# my cheetsheet in python 1.2

#!/bin/python3

# ++++++++++ Importing ++++++++++ #
print("Importing is Important:")

from email.quoprimime import quote
import sys #systeem functions and parameters
from datetime import datetime
print(datetime.now())

from datetime import datetime as dt # importing with an alias
print(dt.now()) # it will wirk the same as before 

def newLine():  #this is a function of making a new line
    print('\n')

newLine()


# ++++++++++ Advanced Strings ++++++++++ #
print("Advanced String:")

myName = "Mohammed"
print(myName[0]) #first initial
print(myName[-1]) #last letter  ( -1 always get the last thing (object, letter, thing... ) )

sentence = "This is a sentence."
print(sentence[:4]) #first word
print(sentence[-9:]) #last word
print(sentence[-9:-1]) #to remove the period(dot)
print(sentence.split()) #split the sentence by delimiter (space) {each eord in it's own}

sentenceSplit = sentence.split()  #variable to spilt the sentence
print(sentenceSplit)

sentenceJoin = ' '.join(sentenceSplit) #this a way of adding the sentence (joining them together)
print(sentenceJoin)

print('\n'.join(sentenceSplit)) #to make each word in it's line

quoteception = "I said, 'give me all the money' "
print(quoteception)
quoteception2 = "I said, \"give me all the money\" "  #to display " " in a string use \"
print(quoteception2)

print("A" in "Apple") #This will return boolean (If you have the letter in the word it's true if not it's false)

letter = "A" #case sensitive
word = "Apple"
print(letter.lower() in word.lower()) #Improved - case insensitive

wordTwo = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in wordTwo.lower()))

tooMuchSpace = "          hello          "
print(tooMuchSpace.strip()) # strip function will remove all space

fullName = "ohammed Khawlan" #letter missing
print(fullName.replace("ohammed", "Mohammed")) #this will replace the missing letter word with the the coorect word
print(fullName.find("Khawlan")) #Tell the start point of the word (or letter) you typed in the brackets

movie = "The Hangover"
print("My favourite movie is {}.".format(movie)) # {} is called a placeholder

def favouriteBook(title, author):
    fav = "My favourite book is \"{}\", which is writtin by \"{}\".".format(title, author)  # ( \"{}\" )is just to add double quotes before and after the string
    return fav

print(favouriteBook("The great Gatsby", "F. Scott Fitzgerald"))

newLine()


# ++++++++++ Dictionaries ++++++++++ #
print("Dictionaries are keys and values:")
# [] are list
# () are tuples
# {} are dictionaries

drinks = {"White Russians": 7, "Old Fashion": 10, "Lemon Drop": 8, "Buttery Nipples": 6} # drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
print(employees["Finance"]) #if you want to call specific list use []

employees["Legal"] = ["Mr. Froud"] #add new key: value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #another way of adding new key: value pai
print(employees)

drinks["White Russians"] = 8 #change the value
print(drinks) 

print(drinks.get("White Russians")) #to get a value of specific item
print(drinks.get("Martini")) #if the item is not found in list it will return "none"

newLine()


# ++++++++++ List and dictionaries ++++++++++ #

movies = ["when Harry Met Sally", "The Hangover", "The Perks Of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Jake", "Leah", "Jeff"]
combined = zip(movies, person)
movieDictionaries = {key: value for key, value in combined} #this is how you you make combined list into dictionaries

print(movieDictionaries)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #