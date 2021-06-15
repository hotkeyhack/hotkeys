#print is in the inbuilt library

import random #using this method from pythons built in library, random is also a librbary, also doesn't need any parameters

print(random.random()) #produces a random number >0 <1

print(random.random()*100)

print(random.uniform(1, 10)) #generates a random number between 1 & 10, inclusive

print(random.randint(1,10)) #generates a random integer between 1 & 10, in

from random import random, uniform, randint #this is another cleaner way to right the random imorts

print(random())
print(uniform(2,20))
print(randint(20,2000))

#data types are none, boolean, string, dot notation


# a = "|"
# b = " "
# c = "-"

# print(b *3, a, b*3, a)
# print(b *3, a, b*3, a)
# print(b *3, a, b*3, a)
# print(c *15)
# print(b *3, a, b*3, a)
# print(b *3, a, b*3, a)
# print(b *3, a, b*3, a)
# print(c *15)
# print(b *3, a, b*3, a)
# print(b *3, a, b*3, a)
# print(b *3, a, b*3, a)
# print(c *15)

# a = "         \n" 
# b = "  |  |   \n" 
# c = "---------\n"

# print(a,b,c) 

# a = "         \n" 
# b = "  |  |   \n" 
# c = "---------\n"
# print(a,b,b,c,b,b,c,b,b)

#ctrl /turn text in to comments when highlighted

#activity2 Methods
# var1 = i am supreme
# #.upper()
# print("var1".upper())
# #.lower()
# print("var1".lower())
# #.capitalize()
# print("i am supreme".capitalize())
# #.count()
# print("i am supreme"
# #.find()
# print("i am supreme".find())
# #.replace()
# print("i am supreme".replace())
# #.strip()
# print("i am supreme".strip())

#Activity3: Methods
#other useful methods from built-in library are
#also from random library

#append: adding a new variables to a list
#int: turns a string into an integer
#str: turns an integer into a string
#time: records to time past since printing a specific statement

list_1 = [
    "one"
    "two"
    "three"
]
int_1 = "123456789"
print(random.choice(list_1))