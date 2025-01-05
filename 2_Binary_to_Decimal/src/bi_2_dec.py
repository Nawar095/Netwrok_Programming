'''
Question 2: Convert from Binary to Decimal
- Write a Python program that converts a Binary number into its equivalent Decimal number.
- The program should start reading the binary number from the user. Then the decimal equivalent number must be calculated. 
- Finally, the program must display the equivalent decimal number on the screen.
Tips: solve input errors.

# ---------Step by Step Algorithm ------
1. Prompt the user to enter a binary number.
2. Validate the input to ensure it is a binary number.
3. Convert the valid binary number to a decimal number.
4. Display the decimal equivalent.

# ----------Formula --------------
Decimal = binary x 2^power
* binary: refers to the individual bits (0 or 1) of the binary number, read from right to left.
* power: is the position of each bit, starting from 0 on the rightmost side and increasing by 1 for each bit moving to the left.
# ---------Example Calculation: Let's use the binary number "10101" as an example:
1. Rightmost bit: For the rightmost bit (1), the power is 0, so the calculation is: 1 x 2^0 = 1.
2. Next bit: Moving one position to the left, the bit is 0, and the power is 1, so the calculation is: 0 x 2^1 = 0.
3. Next bit: Moving one more position to the left, the bit is 1, and the power is 2, so the calculation is: 1 x 2^2 = 4.
4. Next bit: Moving further left, the bit is 0, and the power is 3, so the calculation is: 0 x 2^3 = 0.
5. Leftmost bit: Finally, for the leftmost bit, the bit is 1, and the power is 4, so the calculation is: 1 x 2^4 = 16.
6. Sum: Finally, sum up all the calculated values: 1 + 0 + 4 + 0 + 16 = 21.
'''

# ------ Check the input: ----------
def CheckTheValidationOfInput(n):
    for i in n: 
        if i not in '01':
            return False
        
    return True

# -------- function to convert binary to decimal: --------
def binaryToDecimal(binary_str):
    # Convert binary string to decimal
    decimal_number = 0
    power = len(binary_str) - 1
    
    for bit in binary_str:
        decimal_number += int(bit) * (2 ** power)
        power -= 1
    
    return decimal_number


binary = input("Enter a binary number: ")

while (CheckTheValidationOfInput(binary)==False):
    binary = input("Input is not a valid binary number, Enter a binary number: ")

else: 
    decimal = binaryToDecimal(binary)

print("Decimal equivalent:", decimal)

