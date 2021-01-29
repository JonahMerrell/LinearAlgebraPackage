'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 29 2019
written for:        Homework4 Task5
course:             Math 4610

purpose:            scalar multipy the first vector, then add it to the second vector.
'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_add,vector_scal_mult


def vector_SAXPY(scalar,vector1,vector2):
    return vector_add(vector_scal_mult(scalar,vector1),vector2)

#The code below is used just for testing.
vector1 = [5,7,9,2,5]
vector2 = [8,2,3,6,9]
scalar = 6.0
print(vector_SAXPY(scalar,vector1,vector2))

