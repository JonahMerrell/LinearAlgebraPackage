'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 22 2019
written for:        Homework3 Task9
course:             Math 4610

purpose:            Write code that implements the secant method over multiple sub-intervals, in order to find multiple roots

'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import root_solve_secant_hybrid
import math

def root_solve_secant_intervals(f, a, b, divisions, tol, maxiter):
    start_time = time.time()  #
    solutions = []
    step_size = (b-a)/divisions
    i=a
    while i < b:
        solution = root_solve_secant_hybrid(f, i, i+step_size, tol,maxiter)
        if (solution != None):
            #solution = round(solution,math.floor(abs(math.log(tol))))
            #if (solution not in solutions):
            solutions.append(solution)
        i += step_size
    return solutions

#The code below is used just for testing.
#def function(x):
#    return math.sin(math.pi* (x ** 2) + 3.7)
#print(root_solve_secant_intervals(function, 1.1, 68.3, 10000,0.000001,20))




