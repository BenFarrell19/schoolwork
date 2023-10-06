# --------------------------------
# Joy and Beauty of Data
# Authors: Ryan Bockmon and John Paxton
# --------------------------------
# MadLib Exercise
# --------------------------------

'''
# Get User Input for MadLib Story

adjective_1 = input("Enter an adjective: ")
name_1 = input("Enter a name: ")
number = input("Enter a number: ")
name_2 = input("Enter another name: ")
town_1 = input("Enter a town name: ")
town_2 = input("Enter a different town name: ")
adjective_2 = input("Enter an adjective: ")

# Print Story

print()
print("A new and "+ adjective_1 + " movie is coming soon!")
print("It's about " + name_1 + " and the " + number + " Python programmers. ")
print(name_1 + " is a computing wizard whose talent threatens " + name_2 + ".")
print(name_1 + " is forced to flee from "+ town_1 + " and hides in nearby "+ town_2 + ".")
print("But " + name_2 + " finds " + name_1 + " and casts a " + adjective_2 + " spell.")
'''
# -------------------------------------------------------------------------

# user inputs
name_1 = input("Enter a name: ")
name_2 = input("Enter another name: ")
verb_1 = input("Enter a verb: ")
verb_2 = input("Enter a verb (past tense): ")
age = int(input("Enter an age: "))
temp = float(input("Enter a temperature: "))

# printing story

print()
print("One day two friends " + name_1 + " and " + name_2 + " were " + verb_1)
print("They were both " + str(age) + " years old")
print("After " + verb_1 + " for awhile they " + verb_2 + " home because the temperature was " + str(temp) + " degrees.")