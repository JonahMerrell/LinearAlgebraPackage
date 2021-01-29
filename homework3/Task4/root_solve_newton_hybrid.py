'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 2 2019
written for:        Homework3 Task4
course:             Math 4610

purpose:            For this ask, we were asked to implement a hybrid method for approximate solution of root
                    finding problems using Newtons method and the bisection method.
'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import root_solve_bisection, root_solve_newton
import math


def root_solve_newton_hybrid(function, function_prime, a, b, tol,maxiter):
    c = root_solve_bisection(function, a, b, tol, 4)
    if c == None:
        return None
    solution = root_solve_newton(function, function_prime, c, tol, maxiter)
    return solution


#def function(x):
#    return x * math.cosh(x) + pow(x, 3) - math.pi
#def function_prime(x):
#    return math.cosh(x) + x * math.sinh(x) + 3 * pow(x, 2)
#print(root_solve_newton_hybrid(function, function_prime, 0, 2, 0.000001,20))