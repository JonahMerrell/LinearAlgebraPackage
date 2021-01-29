'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 2 2019
written for:        Homework3 Task1
course:             Math 4610

purpose:            Write code that implements the Secant iteration

'''
import math

def root_solve_secant(f, x_0, x_1, tol, maxiter,getIterCount=False):
    #Check to see if a or b are already the solution
    if (f(x_0) == 0) :
        return x_0
    if (f(x_1) == 0) :
        return x_1

    error = 10*tol
    iter = 0
    while(error > tol and iter < maxiter):
        iter += 1
        x_2 = x_1 - f(x_1)*(x_1-x_0)/(f(x_1)-f(x_0))
        error = abs(x_2 - x_1)

        x_0 = x_1
        x_1 = x_2

    if getIterCount == False:
        return x_2
    else:
        return (x_2, iter)

#The code below is used just for testing.
#def function(x):
#    return math.cos(x) - x
#print(root_solve_secant(function, 1.0, 1.1, 0.000001,20))





