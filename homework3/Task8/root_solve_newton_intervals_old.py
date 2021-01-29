'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 22 2019
written for:        Homework3 Task7
course:             Math 4610

purpose:            Write code that implements bisection iteration

'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import root_solve_newton
import math

def root_solve_newton_intervals(f,f_prime, a, b, divisions, tol, maxiter):
    solutions = []
    step_size = (b-a)/divisions
    i=a
    while i < b:
        solution = root_solve_newton(f,f_prime, i+0.5*step_size, tol,maxiter)
        if (abs(f(solution)) <= tol):
            solution = round(solution,math.floor(abs(math.log(tol))))
            if (solution not in solutions):
                solutions.append(solution)
        i += step_size
    return solutions

#The code below is used just for testing.
def function(x):
    return math.cos(x ** 2)
def function_prime(x):
   return - 2*x*math.sin(x ** 2)
print(root_solve_newton_intervals(function, function_prime, 0, 5, 100,0.000001,20))




