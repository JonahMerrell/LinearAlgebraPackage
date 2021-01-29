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
from _mymodules import root_solve_bisection, root_solve_secant
import math


def root_solve_secant_hybrid(function, a, b, tol,maxiter):
    c = root_solve_bisection(function, a, b, tol, 4)
    if c == None:
        return None
    #Find another point close to c, appropriate to the scale of a and b
    if abs(c-a) < abs(c-b) :#If c is closer to a
        d = c + ((b-a)/10.0)
    else:
        d = c - ((b-a) / 10.0)
    solution = root_solve_secant(function, c, d, tol, maxiter)
    return solution


#def function(x):
#    return x * math.cosh(x) + pow(x, 3) - math.pi
#print(root_solve_secant_hybrid(function, 0, 2, 0.000001,20))