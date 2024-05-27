''' '
Question_1 : 
B- Write a Python program that calculates the factorial of a given number entered by user.
'''

# Note: A recursive function is a function that calls itself within its own definition. 
# It solves a problem by breaking it down into smaller, simpler subproblems and calling itself 
# to solve each subproblem until a base case is reached.

# Define a function to calculate the factorial recursively.
def factorial(number):
    # Check if the number is negative, return an error message.
    if number < 0:
        return "Factorical is not defined for negative numbers, Please Enter non-negative integer!"
    # calculate factorial:
    return 1 if (number ==1 or number ==0) else number * factorial(number-1) 
    '''
    - Note about previous line: `return 1 if (number ==1 or number ==0) else number * factorial(number-1)`
    - it equals to :    
    if number == 0 or number == 1:      
        return 1      
    return number * factorial(number - 1)      
    
- Base case: If the number is 0 or 1, return 1.
- Recursive case: Calculate the factorial by multiplying the number with the factorial of (number-1).'''
number = int(input("Enter a number to calculate its factorical: "))
## Calculate the factorial using the factorial() function: 
fact = factorial(number) # Initialize a variable to store the factorial result
# Check if the number is negative, print the error message returned by the factorial() function:
if number < 0 :
    print(fact)
else: 
    print(f"Factorial of {number} is: {fact}") # Print the calculated factorial.
