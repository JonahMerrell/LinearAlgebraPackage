'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 29 2019
written for:        Homework4 Task6
course:             Math 4610

purpose:            Implement a method that returns the dot product of two vectors of the same length.
'''

def vector_dot(vector1,vector2):
    vector_sum = 0
    for i in range(len(vector1)):
        vector_sum += vector1[i] * vector2[i]

    return vector_sum


#The code below is used just for testing.
#vector1 = [5,7,9,2,5]
#vector2 = [8,2,3,6,9]
#print(vector_dot(vector1,vector2))

