'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       September 3 2019
written for:        Homework1 Task9
course:             Math 4610

purpose:            Using the central difference quotient, we compute the derivative of the exponential function e^x at
                    the point x= pi. The absolute and relative error are also computed.
'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import rel_error, abs_error
from math import exp

def compute_exp_pi():
    h = .000003814697265625 # This is the bext value for h that results in the most precise copmuation (As discovered from task 6).
    pi = 3.14159265358979323846264338327
    true_value = 23.140692632779269

    f_prime = (exp(pi + h) - exp(pi - h))/(2*h)
    relError = rel_error(true_value,f_prime)
    absError = abs_error(true_value, f_prime)

    print("e^pi = " + str(f_prime))
    print("The relative error is " + str(relError))
    print("The absolute error is " + str(absError))

#The code below is used just for testing.
compute_exp_pi()

