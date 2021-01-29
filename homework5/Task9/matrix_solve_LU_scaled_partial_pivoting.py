'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 9 2019
written for:        Homework5 Task9
course:             Math 4610

purpose:            This method will solve a system of linear equations by performing LU factorization with
                    scaled partial pivoting, followed with forward substitution and back substitution.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_upper_tri, matrix_solve_lower_tri,matrix_LU_factor_scaled_partial_pivoting


def matrix_solve_LU_scaled_partial_pivoting(matrix,vector):
    n=len(matrix)
    LU = matrix_LU_factor_scaled_partial_pivoting(matrix)
    U = [[(LU[i][j] if (i<=j) else 0.0) for j in range(n)] for i in range(n)]
    L = [[(LU[i][j] if (i>j) else (1.0 if (i == j) else 0.0)) for j in range(n)] for i in range(n)]

    solution_y = matrix_solve_lower_tri(L,vector)
    solution_x = matrix_solve_upper_tri(U,solution_y)
    return solution_x

#The code below is used just for testing.
#matrix_example = [[1,1,-1],[1,-2,3],[2,3,1]]
#vector_example = [4,-6,7]
#print(matrix_solve_LU_scaled_partial_pivoting(matrix_example,vector_example))


