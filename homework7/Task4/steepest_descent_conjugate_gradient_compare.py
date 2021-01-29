'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 21 2019
written for:        Homework7 Task4
course:             Math 4610

purpose:            This method compares the steepest descent method with the conjugate gradient method.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_steepest_descent, matrix_solve_conjugate_gradient, matrix_mult, gen_diagdom_sym_matrix, convert_vec_mat, abs_error_2norm

def steepest_descent_conjugate_gradient_compare():
    n=100;
    random_matrix = gen_diagdom_sym_matrix(n)
    b = convert_vec_mat(matrix_mult(random_matrix,[[1]] * n)) #the solution should be a vector of 1s.
    (solution1,iterCount1) = matrix_solve_steepest_descent(random_matrix,b,0.0001,10000,True)
    (solution2, iterCount2) = matrix_solve_conjugate_gradient(random_matrix, b, 0.0001, 10000, True)

    print("Steepest Descent " + str(n) + "x" + str(n) + ": Absolute Error=" + str(abs_error_2norm([1] * n,solution1)) + "  Iteration Count=" + str(iterCount1))
    print("Conjugate Gradient " + str(n) + "x" + str(n) + ": Absolute Error=" + str(abs_error_2norm([1] * n,solution2)) + "  Iteration Count=" + str(iterCount2))

steepest_descent_conjugate_gradient_compare()