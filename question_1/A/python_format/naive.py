'''
If you have two lists, L1=['HTTP','HTTPS','FTP','DNS'] L2=[80,443,21,53], 
convert it to generate this dictionary d={'HTTP':80,'HTTPS':443,'FTP':21,'DNS':53 }
'''
#initializing two lists, L1 and L2 
# L1 contain different types of network protocols and L2 contain their corresponding port numbers:
L1=['HTTP','HTTPS','FTP','DNS'] 
L2=[80,443,21,53] 

# Create an empty dictionary to store the protocols and their corresponding port numbers:
d = {}
# Iterate over each element in the L1 list (network protocols).
for key in L1:
    # Iterate over each element in the L2 list (port numbers).
    for value in L2:
        d[key] = value # Assign the current protocol (key) as the key, and the current port number (value) as the value in the dictionary.
        L2.remove(value) # Remove the current port number from the L2 list to avoid duplicate assignments.
        break # Break out of the inner loop to move to the next protocol in the L1 list.

print(d)