'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 21 2019
written for:        Homework7 Task2
course:             Math 4610

purpose:            This method tests the QR steepest_descent method on various hilbert matrices.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_steepest_descent, matrix_mult, matrix_transpose, abs_error_2norm, matrix_mult, convert_vec_mat

def hilbert_matrix_steepest_descent_test():

    selection = [4,8,16,32,64,128,]
    hilbert_matrix = []
    solution = []
    # Create the hilbert matrices and their corresponding Q factorization matrix.
    for n in selection:
        hilbert_matrix.append([[1/(1+i+j) for i in range(n)] for j in range(n)])  # Hilbert Matrix generator
        b = [sum([1 / (1 + i + j) for i in range(n)]) for j in range(n)] #the solution should be a vector of 1s.
        solution.append(matrix_solve_steepest_descent(hilbert_matrix[-1],b,0.0001,10000))

        print("Absolute error for " + str(n) + "x" + str(n) + ": " + str(abs_error_2norm([1] * n,solution[-1])))
        print(solution[-1])

hilbert_matrix_steepest_descent_test()

