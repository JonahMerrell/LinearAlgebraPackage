'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 29 2019
written for:        Homework4 Task2
course:             Math 4610

purpose:            Calculate the 1-norm of a vector
'''

def vector_1norm(vector):
    sum = 0.0
    for i in range(len(vector)):
        sum += abs(vector[i])

    return sum

#The code below is used just for testing.
#vector = [5,7,9,2,5]
#print(vector_1norm(vector))

