#!/usr/bin/python3

tuple = ( 'abcd', 786 , 2.23, 'Venu', 70.2  )
tinytuple = (123, 'Venu')

print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple


# lists Vs tuples: lists are enclosed [ ]  and their elements and size can be changed,
# tuples are enclosed  ( ) their elements and size can NOT be changed. read-only lists

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
# tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

noparens = 'abcd', 786 , 2.23, 'Venu', 70.2
print (noparens)   # Prints tuple two times
