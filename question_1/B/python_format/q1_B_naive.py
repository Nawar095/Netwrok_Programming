''' '
Question_1 : 
B- Write a Python program that calculates the factorial of a given number entered by user.
'''


# Ask the user to enter a number:
number = int(input("Enter a number to calculate its factorical: "))
# Check if the input is a non-negative integer. If the input is invalid, display an error message.
if number < 0:
    print("Factorical is not defined for negative numbers, Please Enter non-negative integer!")
# # Check if the number is 0 or 1, as the factorial of both is 1
elif number == 0 or number == 1:
    print("Factorial of", number, "is:", 1)
# If the number is positive and greater than 1
else: 
    fact = 1 # Initialize a variable to store the factorial result
    # Loop from 1 to the number (inclusive) to calculate the factorial
    for i in range(1, number+1):
        # # Multiply the current value of 'fact' by each number in the range and update fact
        fact = fact * i 
    print(f"Factorial of {number} is: {fact}") 