# bring in the Python modules needed for doing math functions and getting random numbers
# get a random integer between 1 and 10 and assign it to a.
    # hint: look up randint() in Python's random module documentation:
    # https://docs.python.org/3/library/random.html#module-random
    # make sure it's not possible to get 0 for a, but is possible to get 10
# get a random floating point number between 0 and 20; assign it to b.
    # hint: try this in the shell a few times >>>random.random() * 5
    # what's going on there? Is it ever more than 5? Ever less than 0?
# round b to two decimal places
    # hint: https://docs.python.org/3/library/functions.html?#round
    # hint: try this in the shell for a way to modify a variable:
        # >>> x = 64
        # >>> x = math.sqrt(x)
        # >>> print(x)
        # can you explain what happened there?
# print out a and b in the terminal
    # Ex: print("a is ", a)
# ask the user to enter the c coefficient (assume: user will always enter a valid number)
# make sure Python considers the user's input as a float data type (not a string.)
# make sure c is negative. Consider using module's absolute value function.
    # hint: https://docs.python.org/3/
    # ...click Global Module Index. Look for math module. Look for absolute value
# print out the quadratic equation we will be solving (ex: 3x^2 + 13.89x - 12.0 = 0)
    # Hint: you can mix data types in the print() function if you separate them with commas
    # Ex: >>>print("stuff", 4, True)
    # Hint: you can concatenate strings in the print() function with the + operator
    # Hint: print("stuff" + str(4) + str(True))
# solve for x. Remember, there are two different x values, so really solve for x_1 and x_2.
    # Quadratic formula: x = -b ± √(b^2 - 4ac)/2a
# use the math modules sqrt() function to evaluate the √(b^2 - 4ac) expression in the formula
# print out the two roots (ex: x =  0.7442850471964851 and -5.3742850471964845)
import math
import random

a = random.randint(1, 10)
b = random.uniform(0, 20)
b = round(b, 2)
print("a is ", a)
print("b is ", b)
c = float(input("Enter the c coefficient: "))
if c >= 0:
    c = float(input("Enter a negative value for the c coefficient: "))

print(str(a)+"x^2 +", str(b)+"x", c, "= 0")

s = math.sqrt(((b**2) - ((4*a)*c)))
x = s/(2*a)
x_1 = (-1*b) + x
x_2 = (-1*b) - x
print("x =", x_1, "and", x_2)


