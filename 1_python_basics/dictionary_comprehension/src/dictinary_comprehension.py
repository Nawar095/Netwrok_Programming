''' 
Question 1: Python Basics?
D- Using Dictionary comprehension, Generate this dictionary d={0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11}
##################### -- Understanding the problem -- #########################
The problem involves creating a dictionary where each key is a number from 0 to 10 and each value is the key plus one.
Step-by-Step Algorithm:
1. Initialize a range of keys: The keys are numbers from 0 to 10.
2. Calculate the value for each key: For each key i, the value is i + 1.
3. Construct the dictionary using comprehension:
   - Use a loop within a dictionary comprehension to iterate through the range of keys.
   -  For each key in the range, assign the value as key + 1.
''' 
# Create the dictionary using dictionary comprehension
d = {i: i + 1 for i in range(11)}
# Print the resulting dictionary to verify
print(d)