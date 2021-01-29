'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 14 2019
written for:        Homework6 Task1
course:             Math 4610

purpose:            Implement a method that performs the Cholesky factorization method for square matrices
'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_check_sym

def matrix_cholesky_fac(matrix):
    if (not matrix_check_sym(matrix)):
        return False
    width = len(matrix)
    L_matrix = [[0 for i in range(width)] for j in range(width)]
    for k in range(0, width):
        for i in range(0, k):
            temp_sum = matrix[k][i]
            for j in range(0, i):
                temp_sum -= L_matrix[i][j] * L_matrix[k][j]
            L_matrix[k][i] = temp_sum/L_matrix[i][i]

        temp_sum = matrix[k][k]
        for j in range(0,k):
            temp_sum -= pow(L_matrix[k][j],2)
        L_matrix[k][k] = pow(temp_sum,0.5)

    return L_matrix

#The code below is used just for testing.
#A_ = matrix_cholesky_fac([[3,-1,0],[-1,2,-1],[0,-1,2]])
#print(A_)

