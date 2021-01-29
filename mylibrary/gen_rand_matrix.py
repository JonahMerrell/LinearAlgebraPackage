'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 12 2019
written for:        Homework1 Task9
course:             Math 5610

purpose:            Create a n*m matrix (the size is inputted from the user) with random entries from 0 to 1.
'''

import random

def gen_rand_matrix(width=5):
    A = [[0 for i in range(width)] for j in range(width)]
    for i in range(0,width):
        for j in range(0, width):
            A[j][i] = random.random()
    return A

#The code below is used just for testing.
#A_ = gen_rand_matrix()
#for i in range(len(A_)):
#    print(A_[i])



