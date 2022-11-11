#!/usr/bin/python3
from itertools import pairwise
def pascal_triangle(n):
    '''This takes in an integer 'n' and returns 
    the pascal triangle of n
    
    >>> pascal_triangle(3)
    >>> [1]
    ...[1,1]
    ...[1,2,1]
    ...[1,3,3,1]
    '''
    starting = [1]
    output = [starting]
    while len(output) < n +1 :
        pair_units = pairwise(starting) #group elements in twos succesively     
        returned_sum = [sum(i) for i in pair_units]
        returned_sum.insert(0,1) #pascals beginning element is one
        returned_sum.append(1) #pascals end element is one 
        starting = returned_sum
        output.append(returned_sum)
    return output
       
