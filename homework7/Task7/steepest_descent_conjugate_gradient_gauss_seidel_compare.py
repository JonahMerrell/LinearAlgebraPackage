'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 21 2019
written for:        Homework7 Task7
course:             Math 4610

purpose:            This method compares the steepest descent method, conjugate gradient method, and gauss-seidel method.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_steepest_descent, matrix_solve_conjugate_gradient, matrix_solve_gauss_seidel, matrix_mult, gen_diagdom_sym_matrix, convert_vec_mat, abs_error_2norm

import time

def steepest_descent_conjugate_gradient_gauss_seidel_compare():
    n=100;
    random_matrix = gen_diagdom_sym_matrix(n)
    b = convert_vec_mat(matrix_mult(random_matrix,[[1]] * n)) #the solution should be a vector of 1s.
    start_time = time.time()
    (solution1,iterCount1) = matrix_solve_steepest_descent(random_matrix,b,0.00000000001,10000,True)
    time1 = time.time() - start_time
    start_time = time.time()
    (solution2, iterCount2) = matrix_solve_conjugate_gradient(random_matrix, b, 0.00000000001, 10000, True)
    time2 = time.time() - start_time
    start_time = time.time()
    (solution3, iterCount3) = matrix_solve_gauss_seidel(random_matrix, b, 0.00000000001, 10000, True)
    time3 = time.time() - start_time
    print("Steepest Descent " + str(n) + "x" + str(n) + ": Absolute Error=" + str(abs_error_2norm([1] * n,solution1)) + "  Iteration Count=" + str(iterCount1) + " time=" + str(time1))
    print("Conjugate Gradient " + str(n) + "x" + str(n) + ": Absolute Error=" + str(abs_error_2norm([1] * n,solution2)) + "  Iteration Count=" + str(iterCount2) + " time=" + str(time2))
    print("Gauss Seidel " + str(n) + "x" + str(n) + ": Absolute Error=" + str(abs_error_2norm([1] * n,solution3)) + "  Iteration Count=" + str(iterCount3) + " time=" + str(time3))

steepest_descent_conjugate_gradient_gauss_seidel_compare()