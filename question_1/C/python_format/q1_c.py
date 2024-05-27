'''
C- L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
In this exercise, you will implement a Python program that reads the items of the previous list 
and identifies the items that starts with 'B' letter, then print it on screen.
Tips: using loop, 'len ()' , startswith() methods.
''' 
# Algorithm: 
'''
1. Start with the given list L = ['Network', 'Bio', 'Programming', 'Physics', 'Music'].
2. Iterate over each item in the list using a loop and the range() function.
3. Get the current item from the list using indexing with L[i].
4. Check if the current item starts with the letter 'B' using the startswith() method.
5. If the condition is true (the current item starts with 'B') print the item.
6. Repeat steps 3-5 for each item in the list.
7. After the loop finishes, the program will have printed all the items from the list that start with the letter 'B'.
'''
# Given list
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
# Iterate over each item in the list
for i in range(len(L)):
    # Check if the current item L[i] starts with 'B'
    if L[i].startswith('B'):
        print(L[i]) # Print the item if it starts with 'B'