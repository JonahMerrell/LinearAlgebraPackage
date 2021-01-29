'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       September 3 2019
written for:        Homework1 Task6
course:             Math 4610

purpose:            Using the  central difference quotient, document how the error reduces as h decreases
                    until machine precision causes problems.
'''
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import rel_error
from math import exp

def test_computation_error():
    h = 1.0
    true_value = 23.140692632779269
    error = 1
    x = 3.14159265358979323846264338327
    print("f'(x) = " + str(true_value))
    for i in range(0,40):
        f_prime = (exp(x + h) - exp(x - h))/(2*h)
        error = rel_error(true_value,f_prime)
        print("when h=" + format(h,"30.29") + ", f'(x) = " + str(f_prime) + ", with an error of " + str(error))
        h /= 2


#The code below is used just for testing.
test_computation_error()

