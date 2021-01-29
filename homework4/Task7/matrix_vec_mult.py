'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 29 2019
written for:        Homework4 Task6
course:             Math 4610

purpose:            Implement a method that returns the product of a matrices with a vector.
'''

def matrix_vec_mult(matrix1,vector2):
    iter_count = len(matrix1[0]) # = len(vector2)
    height = len(matrix1)
    final_matrix = [[0] for j in range(height)]


    for j in range(height):
        sum = 0
        for k in range(iter_count):
            sum += matrix1[j][k]*vector2[k][0]
        final_matrix[j][0] = sum

    return final_matrix


#The code below is used just for testing.
#vector1 = [[2,1,4],[0,1,1]]
#vector2 = [[6],[1],[-2]]
#print(matrix_vec_mult(vector1,vector2))
