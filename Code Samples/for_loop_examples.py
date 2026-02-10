#here is an example of a for loop

#problem: I want to do something a certain number of times

#example: I want to calculate the factorial of a number

# 5! = 5 * 4 * 3 * 2 * 1

# simplest example

"""
product = 1

for i in range(1,6,1):
    product = product * i
    print("Current product is ", product)

print("5 factorial is:", product)
"""

# we're going to ask the user for an integer
# and we're going to calculate the factorial of that

num = int(  input("Please enter an integer and we'll calculate its factorial"))

product = 1

for j in range(1,num+1,1):
    product = product * j

print("You entered: ", num, " and its factorial is: ", product)

