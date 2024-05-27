'''
If you have two lists, L1=['HTTP','HTTPS','FTP','DNS'] L2=[80,443,21,53], 
convert it to generate this dictionary d={'HTTP':80,'HTTPS':443,'FTP':21,'DNS':53 }
'''
#We will use the Python map() function to pair the list element with other list elements at the corresponding index 
# map() function is a built-in function that allows to apply a given function to each item of an iterable
# (such as a list, tuple, or string) and returns a new list containing the results.
# syntax: map(function, iterable1, iterable2, ...)
####################################################################
# # initializing lists:
L1=['HTTP','HTTPS','FTP','DNS'] # L1 contain a different type of Network Protocols
L2=[80,443,21,53] # L2 contain corresponding port numbers

d = dict(map(lambda i,j : (i,j) , L1,L2))
# lambda i, j: (i, j) takes two arguments, i and j, representing the elements from L1 and L2, respectively. 
# It returns a tuple (i, j).
# The map() function applies the lambda function to each pair of elements from L1 and L2 and returns an iterator of tuples.
# The dict() function is used to convert the iterator of tuples into a dictionary. 
# Each tuple (i, j) represents a key-value pair, where i is the network protocol 
# and j is the corresponding port number.

print(d)
