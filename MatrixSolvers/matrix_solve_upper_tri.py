'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 5 2019
written for:        Homework5 Task2
course:             Math 4610

purpose:            This method will compute the solution of a square linear system of equations where the coefficient matrix is upper triangular.
'''

def matrix_solve_upper_tri(matrix,vector):

    n = len(matrix)
    solution = [0]*len(vector)

    for i in range(n-1, -1, -1):
        temp_var = vector[i]
        for j in range(i+1, n):
            temp_var -= matrix[i][j] * solution[j]
        solution[i] = temp_var/matrix[i][i]

    return solution


#The code below is used just for testing.
#matrix = [[4,8,10,3,7],[0,2,5,7,2],[0,0,2,7,3],[0,0,0,3,1],[0,0,0,0,8]]
#vector = [12,25,38,27,48]
#print(matrix_solve_upper_tri(matrix,vector))
