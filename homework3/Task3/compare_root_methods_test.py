'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 2 2019
written for:        Homework3 Task3
course:             Math 4610

purpose:            For this ask, we were asked to compare the 4 methods for root finding
                    (functional iteration, bisection, Newton's method, and the secant method)
'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import root_solve_bisection, root_solve_fixed_point, root_solve_newton, root_solve_secant
import math
def function(x):
    return x  * math.cosh(x)+ pow(x,3) - math.pi
def function_prime(x):
    return math.cosh(x)+ x*math.sinh(x) + 3*pow(x,2)

print("The true root to the equation x * cosh(x)+ x^3 - pi is 1.0963278")
try:
    solution, maxiter = root_solve_fixed_point(function, 1, 0.000001, 1000,True)
except:
    solution, maxiter = "N/A","N/A"
print(f"Using the fixed point iteration, the solution was {solution}, which took {maxiter} iterations.")
solution, maxiter = root_solve_bisection(function, 0, 2, 0.000001,getIterCount=True)
print(f"Using the bisection iteration, the solution was {solution}, which took {maxiter} iterations.")
solution, maxiter = root_solve_newton(function, function_prime, 1, 0.000001,30,True)
print(f"Using the newton iteration, the solution was {solution}, which took {maxiter} iterations.")
solution, maxiter = root_solve_secant(function, 1.0, 1.2, 0.000001,30,True)
print(f"Using the secant iteration, the solution was {solution}, which took {maxiter} iterations.")
