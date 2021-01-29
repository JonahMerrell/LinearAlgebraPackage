'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       September 3 2019
written for:        Homework1 Task7
course:             Math 4610

purpose:            Determine the absolute error of an approximation of the number.
'''

def abs_error(true_value,appr_value):
    abs_error_value = abs(true_value - appr_value)
    return abs_error_value

#The code below is used just for testing.
#print(abs_error(1.0,1.0000132))

