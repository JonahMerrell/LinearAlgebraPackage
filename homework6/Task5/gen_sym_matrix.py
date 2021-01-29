'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 14 2019
written for:        Homework6 Task5
course:             Math 4610

purpose:            Create a n*n symmetric  matrix (the size is inputted from the user) with random entries from 0 to 1.
'''
import random

def gen_sym_matrix(width=5):
    A = [[0 for i in range(width)] for j in range(width)]
    for i in range(0, width):
        for j in range(i+1, width):
            value = random.random()
            A[j][i] = value
            A[i][j] = value
    for i in range(0, width):
        A[i][i] = random.random()
    return A

#The code below is used just for testing.
#A_ = gen_sym_matrix()
#for i in range(len(A_)):
#    print(A_[i])


