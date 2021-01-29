'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       September 18 2019
written for:        Homework2 Task9
course:             Math 4610

purpose:            For this ask, compare the results of the functional iteration and Bisection iteration on
                    the problem x cosh(x) + x<sup>3</sup> = pi
'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import root_solve_bisection, root_solve_fixed_point
import math

def function(x):
    return x  * math.cosh(x) + pow(x,3) - math.pi

print("Attempting to solve equation with root_solve_fixed_point:")
try:
    print(root_solve_fixed_point(function, 1, 0.0001, 1000))
except OverflowError:
    print("An OverflowError occured")

print("")
print("Attempting to solve equation with root_solve_bisection:")
print(root_solve_bisection(function, 0, 2, 0.0001))


