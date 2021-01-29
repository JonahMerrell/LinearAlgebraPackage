'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       September 3 2019
written for:        Homework1 Task8
course:             Math 4610

purpose:            Determine a machine epsilon for the computers I would like
                    work on computationally for single float precision.

                     smacsps - returns the single precision value for machine precision
                     dmacsps - returns the double precision value for machine precision
'''
import numpy as np

def calculate_single_float_precision():
    y = np.float32(1.0)
    x = np.float32(1.0)
    z = x + y
    error = abs(z - x)
    iteration_count = 0

    while (error > 0):
        y = y/np.float32(2)
        z = x + y
        error = abs(z - x)
        iteration_count += 1

    return [iteration_count, y]


#The code below is used just for testing.
#smaceps_data = calculate_single_float_precision()
#print("machine double float mantissa = " + str(smaceps_data[0]))
#print("machine double float precision = " + str(smaceps_data[1]))

