'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 27 2019
written for:        Homework8 Task3
course:             Math 5610

purpose:            This method will approximate the condition number of a matrix by computing the largest and smallest eigenvalue.
'''

#I am not done yet

import sys, os, random
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_inverse_power_iteration, matrix_power_iteration, vector_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, matrix_transpose, matrix_solve_tridiagonal, matrix_add

def matrix_condition_number(matrix):
    smallest_eigenvalue = matrix_inverse_power_iteration(matrix,0,0.00000000000001,20000)
    largest_eigenvalue = matrix_power_iteration(matrix,0.0000000001,20000)
    return abs(largest_eigenvalue/smallest_eigenvalue)

#This is the original inverse power iteration code, but modified to include the tri-diagonal solver instead.
def matrix_inverse_power_iteration(matrix,alpha,tol,max_iter,getIterCount=False):
    error = tol * 10
    count = 0
    eigenvaluenew = 0
    I = [[-int(i == j)*alpha for i in range(len(matrix))] for j in range(len(matrix))]
    v_i = matrix[0]
    while error > tol and count < max_iter:

        eigenvalueold = eigenvaluenew
        v_i = matrix_solve_tridiagonal(matrix_add(matrix,I),v_i)
        v_i = vector_scal_mult(1/vector_2norm(v_i),v_i)
        eigenvaluenew = matrix_mult(matrix_transpose(convert_vec_mat(v_i)),matrix_mult(matrix,convert_vec_mat(v_i)))[0][0]
        count += 1
        error = abs(eigenvaluenew - eigenvalueold)
    if getIterCount == True:
        return eigenvaluenew,count
    else:
        return eigenvaluenew

def gen_tridiagonal_matrix(length=10):
    tridiagonal_matrix = [[0 for i in range(3)] for j in range(length)]
    for i in range(length):
        tridiagonal_matrix[i][1] =  2+random.random()
        tridiagonal_matrix[i][0] = random.random()
        tridiagonal_matrix[i][2] = tridiagonal_matrix[i][0]
    return tridiagonal_matrix

#The code below is used just for testing.
#matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
#matrix_example = [[1/(1+i+j) for i in range(6)] for j in range(6)]
#print(matrix_condition_number(matrix_example))


